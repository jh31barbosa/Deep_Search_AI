Deep Search AI - Chat Inteligente com Flask

Um chat de IA avançado que integra o Google Gemini com capacidades de busca inteligente na web, construído com Flask.

🚀 Características Principais

Chat Inteligente: Interface de conversação natural com IA usando Google Gemini
Busca Web Inteligente: Detecta automaticamente quando precisa buscar informações atuais na web

Múltiplas Conversas: Gerenciamento de conversas simultâneas com histórico

Interface Moderna: Design responsivo e intuitivo com animações suaves

Citação de Fontes: Referências automáticas quando usa informações da web

Exportação: Capacidade de exportar conversas para arquivo texto

🛠️ Tecnologias Utilizadas

Backend: Python 3.8+ com Flask
IA: Google Gemini API
Frontend: HTML5, CSS3, JavaScript (Vanilla)
Busca Web: Google Custom Search API (opcional)
Styling: CSS Grid, Flexbox, Animations

📋 Pré-requisitos

Python 3.8 ou superior
Conta Google Cloud com Gemini API habilitada
(Opcional) Google Custom Search API para busca web

🔧 Instalação
1. Clone o repositório

bash
git clone https://github.com/seu-usuario/deep-search-ai.git

cd deep-search-ai

2. Crie um ambiente virtual
bash
python -m venv venv
source venv/bin/activate  # Linux/Mac

# ou
venv\Scripts\activate  # Windows

3. Instale as dependências
bash
pip install -r requirements.txt

4. Configure as variáveis de ambiente
bash
cp .env.example .env

Edite o arquivo .env com suas chaves de API:
env# Obrigatório
GEMINI_API_KEY=sua-chave-api-gemini-aqui

# Opcional (para busca web)
SEARCH_API_KEY=sua-chave-google-custom-search-api
SEARCH_ENGINE_ID=seu-id-do-mecanismo-de-busca

# Configurações
SECRET_KEY=uma-chave-secreta-forte
FLASK_DEBUG=True
PORT=5000

5. Obtenha a chave da API do Gemini

Acesse Google AI Studio
Crie uma nova chave de API
Copie a chave para o arquivo .env

6. (Opcional) Configure busca web
Para funcionalidade de busca web:

Acesse Google Cloud Console
Habilite a Custom Search JSON API
Crie credenciais (chave de API)
Configure um mecanismo de busca personalizado em Programmable Search

🚀 Execução

Desenvolvimento
bash
python app.py

Produção
bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app

Acesse http://localhost:5000 no seu navegador.

📁 Estrutura do Projeto

deep-search-ai/
├── app.py                 # Aplicação Flask principal
├── templates/
│   └── index.html        # Interface do chat
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── requirements.txt       # Dependências Python
├── .env.example          # Template de variáveis de ambiente
├── .gitignore           # Arquivos ignorados pelo Git
└── README.md            # Este arquivo

🎯 Como Usar

Interface Principal

Nova Conversa: Clique em "Nova Conversa" na barra lateral

Digite sua Pergunta: Use o campo de entrada na parte inferior

Busca Automática: O sistema detecta automaticamente quando precisa buscar informações atuais

Histórico: Todas as conversas ficam salvas na barra lateral

Exportar: Clique duplo em mensagens para copiar ou use as opções de exportação

Funcionalidades Especiais

Busca Inteligente: O sistema detecta palavras-chave como "atual", "hoje", "preço" e realiza buscas automáticas

Citação de Fontes: Quando usa informações da web, cita as fontes automaticamente

Contexto Mantido: Mantém o contexto da conversa para respostas mais precisas
Atalhos de Teclado:

Ctrl + Enter: Enviar mensagem
Ctrl + N: Nova conversa
Duplo clique: Copiar mensagem



🔧 Configuração Avançada

Personalização do Sistema Prompt
Edite a variável system_prompt na classe DeepSearchAI para personalizar o comportamento da IA.

Configuração de Busca Web
Ajuste os search_indicators no método should_search_web() para personalizar quando realizar buscas.

Estilização
Modifique o CSS no template HTML para personalizar a aparência.

🐛 Troubleshooting
Erro: "API Key inválida"

Verifique se a chave do Gemini está correta no arquivo .env
Certifique-se de que a API está habilitada no Google Cloud

Erro: "Busca web não funciona"

Verifique as configurações da Google Custom Search API
Confirme se as chaves SEARCH_API_KEY e SEARCH_ENGINE_ID estão corretas

Erro: "Conversa não carrega"

Verifique se o navegador suporta localStorage
Limpe o cache do navegador

🔒 Segurança

Use SECRET_KEY forte em produção
Configure HTTPS em produção
Limite taxa de requisições se necessário
Monitore uso da API para evitar custos excessivos

📈 Melhorias Futuras

 - Autenticação de usuários
 - Banco de dados persistente
 - Cache de respostas
 - Suporte a upload de arquivos
 - API REST completa
 - Webhooks para integrações
 - Análise de sentimentos
 - Suporte multilíngue

## Testes
 - Gerenciamento de conversas
 - Integração com a API do Gemini
 - Busca na web
 - Rotas da API Flask
 - Tratamento de erros
 - Gerenciamento de sessão

# Instale as dependências necessárias:
 - pip install pytest pytest-mock requests-mock

# Execute os testes:
 - pytest -v

🤝 Contribuição

Fork o projeto
Crie uma branch para sua feature (git checkout -b feature/AmazingFeature)
Commit suas mudanças (git commit -m 'Add some AmazingFeature')
Push para a branch (git push origin feature/AmazingFeature)
Abra um Pull Request

📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
👨‍💻 Autor
Desenvolvido com ❤️ para demonstrar integração entre Flask e Google Gemini API.
🙏 Agradecimentos

Google pela API Gemini
Comunidade Flask
Contribuidores de código aberto


⚠️ Importante: Mantenha suas chaves de API seguras e nunca as commite no repositório!