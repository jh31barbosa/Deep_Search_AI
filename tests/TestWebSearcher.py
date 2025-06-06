def test_web_searcher_search_web(mock_search):
    # Configura ambiente para permitir busca
    web_searcher.search_api_key = 'test-key'
    web_searcher.search_engine_id = 'test-id'
    
    results = web_searcher.search_web('test query')
    assert len(results) == 1
    assert results[0]['title'] == 'Resultado 1'
    mock_search.assert_called_once()

def test_web_searcher_search_web_no_api_key():
    # Configura ambiente sem chave API
    web_searcher.search_api_key = ''
    web_searcher.search_engine_id = 'test-id'
    
    results = web_searcher.search_web('test query')
    assert len(results) == 0

def test_web_searcher_search_web_error(mock_search):
    web_searcher.search_api_key = 'test-key'
    web_searcher.search_engine_id = 'test-id'
    
    mock_response = MagicMock()
    mock_response.json.side_effect = Exception("Erro simulado")
    mock_search.return_value = mock_response
    
    results = web_searcher.search_web('test query')
    assert len(results) == 0