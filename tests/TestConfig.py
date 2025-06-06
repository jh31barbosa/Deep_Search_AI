import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime
import uuid
import json
from app import app, chat_manager, web_searcher, deep_search_ai

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client

@pytest.fixture
def mock_gemini():
    with patch('google.generativeai.GenerativeModel') as mock_model:
        mock_chat = MagicMock()
        mock_model.return_value.start_chat.return_value = mock_chat
        mock_chat.send_message.return_value.text = "Resposta simulada da IA"
        yield mock_model, mock_chat

@pytest.fixture
def mock_search():
    with patch('requests.get') as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'items': [
                {
                    'title': 'Resultado 1',
                    'snippet': 'Descrição do resultado 1',
                    'link': 'http://exemplo.com/1',
                    'displayLink': 'exemplo.com'
                }
            ]
        }
        mock_get.return_value = mock_response
        yield mock_get