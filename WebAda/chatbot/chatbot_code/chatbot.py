import google.generativeai as genai

class Chatbot:
    def __init__(self, config, database, embeddings):
        """
        Inicializa o Chatbot com configurações, banco de dados e modelo de embeddings.

        Parâmetros:
        - config: Instância da classe Config, contendo API_KEY, banco de dados e embeddings.
        - database: Instância da classe Database para gerenciar contexto do usuário.
        - embeddings: Instância da classe Embeddings para gerar vetores semânticos.
        """
        self.config = config
        self.database = database
        self.embeddings = embeddings
        self.model = genai.GenerativeModel("gemini-2.0-flash")  # 🔥 Correção aqui!

    def get_response(self, user_message, user_id="default"):
        """
        Processa a mensagem do usuário, busca contexto e gera uma resposta.

        Parâmetros:
        - user_message: Mensagem enviada pelo usuário.
        - user_id: Identificador do usuário (para gerenciar contexto).

        Retorna:
        - Resposta gerada pelo chatbot.
        """
        # Obtém o contexto armazenado do usuário
        context = self.database.get_context(user_id)

        # Gera embeddings da mensagem do usuário
        user_embedding = self.embeddings.encode(user_message)

        # Se houver contexto armazenado, concatena para gerar uma melhor resposta
        if context:
            prompt = f"Histórico: {context}\nUsuário: {user_message}\nChatbot:"
        else:
            prompt = f"Usuário: {user_message}\nChatbot:"

        # Chama a API Gemini AI para gerar uma resposta
        response = self._generate_response(prompt)

        # Atualiza o contexto armazenado no banco de dados
        new_context = f"{context} {user_message} {response}" if context else f"{user_message} {response}"
        self.database.add_context(user_id, new_context)

        return response

    def _generate_response(self, prompt):
        """
        Usa o Gemini AI para gerar uma resposta baseada no prompt.

        Parâmetros:
        - prompt: Texto de entrada com o contexto da conversa.

        Retorna:
        - Resposta gerada pelo modelo AI.
        """
        try:
            response = self.model.generate_content(prompt)  # 🔥 Correção aqui!
            return response.text.strip() if response and response.text else "Não entendi, pode reformular?"
        except Exception as e:
            return f"Erro ao gerar resposta: {str(e)}"
