from flask import Flask, render_template, request, jsonify, session
import google.generativeai as genai
import os
from datetime import datetime
import json
import uuid
import requests
from urllib.parse import quote
import markdown
import re

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-here')

# Configuração da API do Gemini
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', 'your-gemini-api-key-here')
genai.configure(api_key=GEMINI_API_KEY)

# Configuração do modelo Gemini
model = genai.GenerativeModel('gemini-1.5-flash')

class ChatManager:
    def __init__(self):
        self.conversations = {}
    
    def create_conversation(self, user_id):
        """Cria uma nova conversa para o usuário"""
        conversation_id = str(uuid.uuid4())
        self.conversations[conversation_id] = {
            'user_id': user_id,
            'messages': [],
            'created_at': datetime.now(),
            'context': ""
        }
        return conversation_id
    
    def add_message(self, conversation_id, role, content):
        """Adiciona uma mensagem à conversa"""
        if conversation_id in self.conversations:
            message = {
                'role': role,
                'content': content,
                'timestamp': datetime.now().isoformat()
            }
            self.conversations[conversation_id]['messages'].append(message)
            return True
        return False
    
    def get_conversation(self, conversation_id):
        """Recupera uma conversa"""
        return self.conversations.get(conversation_id, None)
    
    def get_conversation_history(self, conversation_id, limit=10):
        """Recupera o histórico da conversa formatado para o Gemini"""
        if conversation_id not in self.conversations:
            return []
        
        messages = self.conversations[conversation_id]['messages']
        history = []
        
        for msg in messages[-limit:]:
            if msg['role'] == 'user':
                history.append({'role': 'user', 'parts': [msg['content']]})
            elif msg['role'] == 'assistant':
                history.append({'role': 'model', 'parts': [msg['content']]})
        
        return history

chat_manager = ChatManager()

class WebSearcher:
    def __init__(self):
        self.search_api_key = os.environ.get('SEARCH_API_KEY', '')
        self.search_engine_id = os.environ.get('SEARCH_ENGINE_ID', '')
    
    def search_web(self, query, num_results=5):
        """Realiza busca na web usando Google Custom Search API"""
        if not self.search_api_key or not self.search_engine_id:
            return []
        
        try:
            url = f"https://www.googleapis.com/customsearch/v1"
            params = {
                'key': self.search_api_key,
                'cx': self.search_engine_id,
                'q': query,
                'num': num_results
            }
            
            response = requests.get(url, params=params)
            data = response.json()
            
            results = []
            if 'items' in data:
                for item in data['items']:
                    results.append({
                        'title': item.get('title', ''),
                        'snippet': item.get('snippet', ''),
                        'link': item.get('link', ''),
                        'displayLink': item.get('displayLink', '')
                    })
            
            return results
        except Exception as e:
            print(f"Erro na busca web: {e}")
            return []

web_searcher = WebSearcher()

class DeepSearchAI:
    def __init__(self):
        self.system_prompt = """
        Você é um assistente de IA avançado chamado Deep Search AI. Suas principais características:
        
        1. PESQUISA PROFUNDA: Quando necessário, você pode realizar buscas na web para obter informações atualizadas
        2. ANÁLISE CONTEXTUAL: Você analisa profundamente as perguntas e fornece respostas abrangentes
        3. CITAÇÃO DE FONTES: Sempre que usar informações de fontes externas, cite-as adequadamente
        4. RACIOCÍNIO ESTRUTURADO: Apresente seu raciocínio de forma clara e organizada
        5. MULTILÍNGUE: Responda no idioma da pergunta do usuário
        
        Para perguntas que requerem informações atuais ou específicas, indique se uma busca web seria útil.
        """
    
    def should_search_web(self, query):
        """Determina se a consulta requer busca na web"""
        search_indicators = [
            'atual', 'recente', 'hoje', 'agora', 'últimas notícias',
            'preço', 'cotação', 'weather', 'tempo', 'clima',
            'notícias', 'events', 'eventos', 'stock', 'ações'
        ]
        
        query_lower = query.lower()
        return any(indicator in query_lower for indicator in search_indicators)
    
    def enhance_query_with_search(self, query, search_results):
        """Enriquece a consulta com resultados da busca web"""
        if not search_results:
            return query
        
        search_context = "\n\nInformações da web encontradas:\n"
        for i, result in enumerate(search_results, 1):
            search_context += f"{i}. {result['title']}\n"
            search_context += f"   {result['snippet']}\n"
            search_context += f"   Fonte: {result['displayLink']}\n\n"
        
        enhanced_query = f"{query}{search_context}"
        enhanced_query += "\nPor favor, use essas informações para fornecer uma resposta mais completa e atual. Cite as fontes quando apropriado."
        
        return enhanced_query
    
    def generate_response(self, query, conversation_id=None):
        """Gera resposta usando Gemini com contexto da conversa"""
        try:
            # Verificar se deve fazer busca web
            if self.should_search_web(query):
                search_results = web_searcher.search_web(query)
                query = self.enhance_query_with_search(query, search_results)
            
            # Configurar o contexto da conversa
            chat_session = None
            if conversation_id:
                history = chat_manager.get_conversation_history(conversation_id)
                if history:
                    chat_session = model.start_chat(history=history[:-1])  # Excluir a última mensagem
            
            if not chat_session:
                chat_session = model.start_chat()
            
            # Gerar resposta
            response = chat_session.send_message(f"{self.system_prompt}\n\nUsuário: {query}")
            
            return {
                'success': True,
                'response': response.text,
                'search_performed': self.should_search_web(query)
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'response': f"Desculpe, ocorreu um erro ao processar sua solicitação: {str(e)}"
            }

deep_search_ai = DeepSearchAI()

@app.route('/')
def index():
    """Página principal do chat"""
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """Endpoint principal do chat"""
    try:
        data = request.json
        message = data.get('message', '').strip()
        conversation_id = data.get('conversation_id')
        
        if not message:
            return jsonify({'error': 'Mensagem não pode estar vazia'}), 400
        
        # Criar nova conversa se necessário
        if not conversation_id:
            user_id = session.get('user_id', str(uuid.uuid4()))
            session['user_id'] = user_id
            conversation_id = chat_manager.create_conversation(user_id)
        
        # Adicionar mensagem do usuário
        chat_manager.add_message(conversation_id, 'user', message)
        
        # Gerar resposta
        result = deep_search_ai.generate_response(message, conversation_id)
        
        if result['success']:
            # Adicionar resposta do assistente
            chat_manager.add_message(conversation_id, 'assistant', result['response'])
            
            # Converter markdown para HTML
            response_html = markdown.markdown(result['response'])
            
            return jsonify({
                'response': result['response'],
                'response_html': response_html,
                'conversation_id': conversation_id,
                'search_performed': result.get('search_performed', False)
            })
        else:
            return jsonify({'error': result['response']}), 500
            
    except Exception as e:
        return jsonify({'error': f'Erro interno: {str(e)}'}), 500

@app.route('/api/conversation/<conversation_id>')
def get_conversation(conversation_id):
    """Recupera uma conversa específica"""
    conversation = chat_manager.get_conversation(conversation_id)
    if conversation:
        return jsonify(conversation)
    return jsonify({'error': 'Conversa não encontrada'}), 404

@app.route('/api/conversations')
def list_conversations():
    """Lista todas as conversas do usuário"""
    user_id = session.get('user_id', '')
    user_conversations = []
    
    for conv_id, conv_data in chat_manager.conversations.items():
        if conv_data['user_id'] == user_id:
            user_conversations.append({
                'id': conv_id,
                'created_at': conv_data['created_at'].isoformat(),
                'message_count': len(conv_data['messages']),
                'last_message': conv_data['messages'][-1]['content'][:100] if conv_data['messages'] else ''
            })
    
    return jsonify(user_conversations)

@app.route('/api/new-conversation', methods=['POST'])
def new_conversation():
    """Cria uma nova conversa"""
    user_id = session.get('user_id', str(uuid.uuid4()))
    session['user_id'] = user_id
    conversation_id = chat_manager.create_conversation(user_id)
    
    return jsonify({'conversation_id': conversation_id})

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })

if __name__ == '__main__':
    # Configurações para desenvolvimento
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    port = int(os.environ.get('PORT', 5000))
    
    app.run(debug=debug_mode, host='0.0.0.0', port=port)