def test_deep_search_ai_should_search_web():
    assert deep_search_ai.should_search_web("Qual a notícia mais atual?") is True
    assert deep_search_ai.should_search_web("Qual o preço do dólar hoje?") is True
    assert deep_search_ai.should_search_web("Explique a teoria da relatividade") is False

def test_deep_search_ai_enhance_query_with_search():
    search_results = [
        {
            'title': 'Título 1',
            'snippet': 'Descrição 1',
            'link': 'http://exemplo.com/1',
            'displayLink': 'exemplo.com'
        }
    ]
    enhanced = deep_search_ai.enhance_query_with_search("Pergunta original", search_results)
    assert "Pergunta original" in enhanced
    assert "Título 1" in enhanced
    assert "exemplo.com" in enhanced

def test_deep_search_ai_generate_response_no_search(mock_gemini):
    mock_model, mock_chat = mock_gemini
    
    result = deep_search_ai.generate_response("Pergunta que não requer busca")
    assert result['success'] is True
    assert "Resposta simulada da IA" in result['response']
    assert result['search_performed'] is False
    mock_chat.send_message.assert_called_once()

def test_deep_search_ai_generate_response_with_search(mock_gemini, mock_search):
    mock_model, mock_chat = mock_gemini
    web_searcher.search_api_key = 'test-key'
    web_searcher.search_engine_id = 'test-id'
    
    result = deep_search_ai.generate_response("Qual a notícia mais atual?")
    assert result['success'] is True
    assert "Resposta simulada da IA" in result['response']
    assert result['search_performed'] is True
    mock_search.assert_called_once()
    mock_chat.send_message.assert_called_once()

def test_deep_search_ai_generate_response_error(mock_gemini):
    mock_model, mock_chat = mock_gemini
    mock_chat.send_message.side_effect = Exception("Erro simulado")
    
    result = deep_search_ai.generate_response("Pergunta qualquer")
    assert result['success'] is False
    assert "Erro simulado" in result['error']