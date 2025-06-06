def test_chat_manager_create_conversation():
    user_id = str(uuid.uuid4())
    conversation_id = chat_manager.create_conversation(user_id)
    
    assert conversation_id in chat_manager.conversations
    assert chat_manager.conversations[conversation_id]['user_id'] == user_id
    assert len(chat_manager.conversations[conversation_id]['messages']) == 0

def test_chat_manager_add_message():
    user_id = str(uuid.uuid4())
    conversation_id = chat_manager.create_conversation(user_id)
    
    result = chat_manager.add_message(conversation_id, 'user', 'Olá')
    assert result is True
    assert len(chat_manager.conversations[conversation_id]['messages']) == 1
    assert chat_manager.conversations[conversation_id]['messages'][0]['content'] == 'Olá'

def test_chat_manager_add_message_invalid_id():
    result = chat_manager.add_message('invalid-id', 'user', 'Olá')
    assert result is False

def test_chat_manager_get_conversation():
    user_id = str(uuid.uuid4())
    conversation_id = chat_manager.create_conversation(user_id)
    chat_manager.add_message(conversation_id, 'user', 'Olá')
    
    conversation = chat_manager.get_conversation(conversation_id)
    assert conversation is not None
    assert conversation['user_id'] == user_id
    assert len(conversation['messages']) == 1

def test_chat_manager_get_conversation_history():
    user_id = str(uuid.uuid4())
    conversation_id = chat_manager.create_conversation(user_id)
    chat_manager.add_message(conversation_id, 'user', 'Olá')
    chat_manager.add_message(conversation_id, 'assistant', 'Oi! Como posso ajudar?')
    
    history = chat_manager.get_conversation_history(conversation_id)
    assert len(history) == 2
    assert history[0]['role'] == 'user'
    assert history[1]['role'] == 'model'