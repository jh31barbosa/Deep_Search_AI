#!/usr/bin/env python3
"""
Script de execução para Deep Search AI
Facilita a execução em diferentes ambientes
"""

import os
import sys
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

def check_requirements():
    """Verifica se todos os requisitos estão instalados"""
    try:
        import flask
        import google.generativeai as genai
        import requests
        import markdown
        print("✅ Todas as dependências estão instaladas")
        return True
    except ImportError as e:
        print(f"❌ Dependência não encontrada: {e}")
        print("Execute: pip install -r requirements.txt")
        return False

def check_api_keys():
    """Verifica se as chaves de API estão configuradas"""
    gemini_key = os.environ.get('GEMINI_API_KEY')
    
    if not gemini_key or gemini_key == 'sua-chave-api-gemini-aqui':
        print("❌ Chave da API Gemini não configurada")
        print("Configure GEMINI_API_KEY no arquivo .env")
        return False
    
    print("✅ Chave da API Gemini configurada")
    
    # Verificação opcional da API de busca
    search_key = os.environ.get('SEARCH_API_KEY')
    search_id = os.environ.get('SEARCH_ENGINE_ID')
    
    if search_key and search_id:
        print("✅ API de busca web configurada")
    else:
        print("⚠️  API de busca web não configurada (opcional)")
    
    return True

def run_app():
    """Executa a aplicação"""
    if not check_requirements():
        sys.exit(1)
    
    if not check_api_keys():
        sys.exit(1)
    
    print("\n🚀 Iniciando Deep Search AI...")
    print(f"🌐 Acesse: http://localhost:{os.environ.get('PORT', 5000)}")
    print("📝 Use Ctrl+C para parar o servidor\n")
    
    # Importar e executar a aplicação
    from app import app
    
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', '127.0.0.1')
    
    app.run(debug=debug_mode, host=host, port=port)

if __name__ == '__main__':
    run_app()