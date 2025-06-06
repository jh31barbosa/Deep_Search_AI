def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Deep Search AI' in response.data

def test_chat_route_new_conversation(client, mock_gemini):
    response = client.post('/api/chat', json={'message': 'Olá'})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'response' in data
    assert 'conversation_id' in data
    assert len(data['conversation_id']) == 36  # Tamanho de um UUID

def test_chat_route_existing_conversation(client, mock_gemini):
    # Primeiro cria uma conversa
    response = client.post('/api/chat', json={'message': 'Primeira mensagem'})
    data = json.loads(response.data)
    conversation_id = data['conversation_id']
    
    # Envia segunda mensagem na mesma conversa
    response = client.post('/api/chat', json={
        'message': 'Segunda mensagem',
        'conversation_id': conversation_id
    })
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['conversation_id'] == conversation_id

def test_chat_route_empty_message(client):
    response = client.post('/api/chat', json={'message': ''})
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data

def test_get_conversation_route(client):
    # Primeiro cria uma conversa
    response = client.post('/api/chat', json={'message': 'Mensagem de teste'})
    data = json.loads(response.data)
    conversation_id = data['conversation_id']
    
    # Agora recupera a conversa
    response = client.get(f'/api/conversation/{conversation_id}')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['user_id'] == session.get('user_id')
    assert len(data['messages']) == 2  # Mensagem do usuário e resposta

def test_get_conversation_route_not_found(client):
    response = client.get('/api/conversation/invalid-id')
    assert response.status_code == 404
    data = json.loads(response.data)
    assert 'error' in data

def test_list_conversations_route(client):
    # Cria algumas conversas
    client.post('/api/chat', json={'message': 'Conversa 1'})
    client.post('/api/chat', json={'message': 'Conversa 2'})
    
    response = client.get('/api/conversations')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 2
    assert all('id' in conv and 'created_at' in conv for conv in data)

def test_new_conversation_route(client):
    response = client.post('/api/new-conversation')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'conversation_id' in data
    assert len(data['conversation_id']) == 36

def test_health_check_route(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'healthy'
    assert 'timestamp' in data