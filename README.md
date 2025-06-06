# Deep Search AI

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

*Um chat de IA avançado que integra o Google Gemini com capacidades de busca inteligente na web*

[Demonstração](#demonstração) • [Instalação](#instalação) • [Documentação](#documentação) • [Contribuição](#contribuição)

</div>

---

## 📖 Sobre o Projeto

O **Deep Search AI** é uma aplicação de chat inteligente construída com Flask que combina o poder do Google Gemini com capacidades avançadas de busca na web. O sistema detecta automaticamente quando informações atuais são necessárias e realiza buscas inteligentes para fornecer respostas precisas e atualizadas.

### ✨ Características Principais

- **🤖 Chat Inteligente**: Interface de conversação natural powered by Google Gemini
- **🔍 Busca Web Automática**: Detecção inteligente de necessidade de informações atuais
- **💬 Múltiplas Conversas**: Gerenciamento de sessões simultâneas com histórico completo
- **🎨 Interface Moderna**: Design responsivo com animações suaves e UX intuitiva
- **📚 Citação de Fontes**: Referenciamento automático de informações obtidas da web
- **📄 Exportação**: Capacidade de exportar conversas para arquivos de texto
- **⚡ Performance**: Otimizado para respostas rápidas e eficientes

---

## 🛠️ Stack Tecnológica

### Backend
- **Python 3.8+** - Linguagem principal
- **Flask** - Framework web
- **Google Gemini API** - Modelo de IA conversacional

### Frontend
- **HTML5/CSS3** - Estrutura e estilização
- **JavaScript (Vanilla)** - Interatividade e dinamismo
- **CSS Grid & Flexbox** - Layout responsivo

### APIs & Integrações
- **Google Custom Search API** - Busca web (opcional)
- **Google AI Studio** - Gerenciamento de chaves API

---

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter:

- ✅ Python 3.8 ou superior instalado
- ✅ Conta Google Cloud com acesso ao Gemini API
- ✅ (Opcional) Google Custom Search API configurada

---

## 🚀 Instalação e Configuração

### 1. Clone o Repositório

```bash
git clone https://github.com/seu-usuario/deep-search-ai.git
cd deep-search-ai
```

### 2. Configuração do Ambiente Virtual

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Linux/Mac:
source venv/bin/activate

# Windows:
venv\Scripts\activate
```

### 3. Instalação de Dependências

```bash
pip install -r requirements.txt
```

### 4. Configuração de Variáveis de Ambiente

```bash
# Copiar template de configuração
cp .env.example .env
```

Edite o arquivo `.env` com suas credenciais:

```env
# ✅ Obrigatório
GEMINI_API_KEY=sua-chave-api-gemini-aqui

# 🔍 Opcional (para busca web)
SEARCH_API_KEY=sua-chave-google-custom-search-api
SEARCH_ENGINE_ID=seu-id-do-mecanismo-de-busca

# ⚙️ Configurações da aplicação
SECRET_KEY=uma-chave-secreta-forte
FLASK_DEBUG=True
PORT=5000
```

### 5. Obtenção das Chaves de API

#### Gemini API (Obrigatório):
1. Acesse [Google AI Studio](https://makersuite.google.com/)
2. Crie uma nova chave de API
3. Copie a chave para o arquivo `.env`

#### Google Custom Search (Opcional):
1. Acesse [Google Cloud Console](https://console.cloud.google.com/)
2. Habilite a **Custom Search JSON API**
3. Crie credenciais (chave de API)
4. Configure um mecanismo de busca em [Programmable Search](https://cse.google.com/)

---

## 🎯 Como Executar

### Desenvolvimento
```bash
python app.py
```

### Produção
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

🌐 **Acesse**: `http://localhost:5000`

---

## 📁 Estrutura do Projeto

```
deep-search-ai/
├── 📄 app.py                 # Aplicação Flask principal
├── 📁 templates/
│   └── 📄 index.html        # Interface principal do chat
├── 📁 static/
│   ├── 📁 css/              # Estilos customizados
│   ├── 📁 js/               # Scripts JavaScript
│   └── 📁 images/           # Assets visuais
├── 📄 requirements.txt       # Dependências Python
├── 📄 .env.example          # Template de configuração
├── 📄 .gitignore           # Arquivos ignorados
└── 📄 README.md            # Documentação
```

---

## 🎮 Como Usar

### Interface Principal

| Ação | Descrição |
|------|-----------|
| **Nova Conversa** | Clique no botão da barra lateral para iniciar nova sessão |
| **Digite sua Pergunta** | Use o campo de entrada inferior para interagir |
| **Busca Automática** | Sistema detecta automaticamente necessidade de busca |
| **Histórico** | Todas as conversas ficam salvas na barra lateral |
| **Exportar** | Duplo clique em mensagens ou use opções de exportação |

### Funcionalidades Especiais

- **🔍 Busca Inteligente**: Detecta palavras-chave como "atual", "hoje", "preço"
- **📖 Citação Automática**: Referencia fontes quando usa informações da web
- **🧠 Contexto Mantido**: Preserva contexto para respostas mais precisas

### ⌨️ Atalhos de Teclado

- `Ctrl + Enter` → Enviar mensagem
- `Ctrl + N` → Nova conversa
- `Duplo clique` → Copiar mensagem

---

## ⚙️ Configuração Avançada

### Personalização do Sistema Prompt
```python
# Edite a variável system_prompt na classe DeepSearchAI
system_prompt = "Seu prompt personalizado aqui..."
```

### Configuração de Busca Web
```python
# Ajuste os indicadores no método should_search_web()
search_indicators = ["atual", "hoje", "preço", "notícias"]
```

### Customização Visual
Modifique os estilos CSS no template HTML para personalizar a aparência.

---

## 🐛 Troubleshooting

<details>
<summary><strong>❌ Erro: "API Key inválida"</strong></summary>

- ✅ Verifique se a chave do Gemini está correta no `.env`
- ✅ Confirme se a API está habilitada no Google Cloud
- ✅ Teste a chave diretamente no Google AI Studio
</details>

<details>
<summary><strong>❌ Erro: "Busca web não funciona"</strong></summary>

- ✅ Verifique configurações da Google Custom Search API
- ✅ Confirme `SEARCH_API_KEY` e `SEARCH_ENGINE_ID`
- ✅ Teste as credenciais na API diretamente
</details>

<details>
<summary><strong>❌ Erro: "Conversa não carrega"</strong></summary>

- ✅ Verifique suporte do navegador ao localStorage
- ✅ Limpe cache e cookies do navegador
- ✅ Teste em modo incógnito
</details>

---

## 🔒 Segurança

### Recomendações de Produção

- 🔐 Use `SECRET_KEY` forte e única
- 🌐 Configure HTTPS obrigatório
- 🚦 Implemente rate limiting
- 📊 Monitore uso das APIs para controlar custos
- 🔍 Configure logs de auditoria

### Práticas de Segurança

```bash
# Exemplo de configuração de produção
export FLASK_ENV=production
export SECRET_KEY=$(python -c 'import secrets; print(secrets.token_hex())')
```

---

## 🧪 Testes

### Executar Suite de Testes

```bash
# Instalar dependências de teste
pip install pytest pytest-mock requests-mock

# Executar testes
pytest -v
```

### Cobertura de Testes

- ✅ Gerenciamento de conversas
- ✅ Integração Gemini API
- ✅ Funcionalidade de busca web
- ✅ Rotas Flask
- ✅ Tratamento de erros
- ✅ Gerenciamento de sessões

---

## 🗺️ Roadmap

### 📈 Próximas Funcionalidades

- [ ] **Autenticação** - Sistema de usuários
- [ ] **Banco de Dados** - Persistência com PostgreSQL
- [ ] **Cache Inteligente** - Redis para otimização
- [ ] **Upload de Arquivos** - Análise de documentos
- [ ] **API REST** - Endpoints completos
- [ ] **Webhooks** - Integrações externas
- [ ] **Análise de Sentimentos** - Insights emocionais
- [ ] **Multilíngue** - Suporte internacional

---

## 🤝 Contribuição

Contribuições são sempre bem-vindas! Veja como participar:

### Como Contribuir

1. **Fork** o projeto
2. **Crie** uma branch (`git checkout -b feature/MinhaFeature`)
3. **Commit** suas alterações (`git commit -m 'Adiciona MinhaFeature'`)
4. **Push** para a branch (`git push origin feature/MinhaFeature`)
5. **Abra** um Pull Request

### Diretrizes

- 📝 Descreva claramente suas mudanças
- 🧪 Inclua testes para novas funcionalidades
- 📖 Atualize a documentação quando necessário
- 🎨 Siga as convenções de código existentes

---

## 📄 Licença

Este projeto está licenciado sob a **MIT License** - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

## 👨‍💻 Autor

**Desenvolvido com ❤️ para demonstrar integração entre Flask e Google Gemini API**

- 🐙 GitHub: [@seu-usuario](https://github.com/seu-usuario)
- 📧 Email: seu.email@exemplo.com
- 💼 LinkedIn: [Seu Nome](https://linkedin.com/in/seu-perfil)

---

## 🙏 Agradecimentos

Agradecimentos especiais para:

- 🔍 **Google** - Pela API Gemini e Custom Search
- 🌶️ **Comunidade Flask** - Pelo framework incrível
- 🌟 **Contribuidores** - Por todas as melhorias e sugestões
- 💡 **Comunidade Open Source** - Por tornar projetos como este possíveis

---

<div align="center">

**⚠️ Importante: Mantenha suas chaves de API seguras e nunca as commite no repositório!**

---

⭐ **Se este projeto foi útil, deixe uma estrela!** ⭐

</div>