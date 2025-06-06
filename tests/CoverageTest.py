def test_markdown_conversion_in_chat_response(client, mock_gemini):
    mock_model, mock_chat = mock_gemini
    mock_chat.send_message.return_value.text = "**Texto em negrito**"
    
    response = client.post('/api/chat', json={'message': 'Teste markdown'})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert '<strong>' in data['response_html']

def test_session_management(client):
    # Primeira requisição deve criar um user_id na sessão
    response = client.post('/api/chat', json={'message': 'Teste sessão'})
    assert 'user_id' in session
    
    # Segunda requisição deve manter o mesmo user_id
    user_id = session['user_id']
    response = client.post('/api/chat', json={'message': 'Segunda mensagem'})
    assert session['user_id'] == user_id

def test_error_handling_in_chat_route(client):
    with patch('app.deep_search_ai.generate_response') as mock_generate:
        mock_generate.side_effect = Exception("Erro simulado")
        response = client.post('/api/chat', json={'message': 'Mensagem que causa erro'})
        assert response.status_code == 500
        data = json.loads(response.data)
        assert 'error' in data