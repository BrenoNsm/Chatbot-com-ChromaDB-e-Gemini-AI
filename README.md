# Chatbot com ChromaDB e Gemini AI

Bem-vindo ao **Chatbot com Memória**, um assistente inteligente que utiliza o **Gemini AI** para responder perguntas e o **ChromaDB** para armazenar contexto e histórico de conversas.

## 🚀 Funcionalidades
- Utiliza **Google Gemini AI** para gerar respostas inteligentes.
- **ChromaDB** para memória e recuperação de contexto.
- **Embeddings** gerados com `sentence-transformers`.
- Modularização para fácil manutenção.

## 🛠️ Instalação
### 1️⃣ Clone este repositório
```bash
git clone https://github.com/BrenoNsm/Chatbot-com-ChromaDB-e-Gemini-AI.git
cd chatbot-gemini
```

### 2️⃣ Crie um ambiente virtual (opcional, mas recomendado)
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
```

### 3️⃣ Instale as dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure a API Key do Gemini AI
Crie um arquivo `.env` no diretório raiz e adicione sua chave da API:
```bash
echo "GEMINI_API_KEY=SUAS_CHAVE_AQUI" > .env
```
Ou edite manualmente o arquivo `.env`:
```
GEMINI_API_KEY=SUAS_CHAVE_AQUI
```

## ▶️ Como Executar
```bash
python chatbot.py
```
Após iniciar, basta interagir digitando no terminal. Para sair, digite `sair`.

## 📂 Estrutura do Projeto
```
chatbot-gemini/
│-- chatbot.py           # Arquivo principal
│-- config.py            # Configuração do Gemini API
│-- database.py          # Gerenciamento do ChromaDB
│-- embeddings.py        # Funções para embeddings
│-- requirements.txt     # Dependências do projeto
│-- .env                 # (Criado pelo usuário) Armazena a chave da API
```

## 🤝 Contribuição
Sinta-se à vontade para contribuir! Abra uma issue ou envie um PR com melhorias.

---
🚀 **Divirta-se explorando a IA!**
