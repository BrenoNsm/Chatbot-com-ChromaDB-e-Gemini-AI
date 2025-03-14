from chromadb import PersistentClient

class Database:
    def __init__(self, config):
        """
        Inicializa o banco de dados usando ChromaDB.

        Parâmetros:
        - config: Instância da classe Config contendo as configurações do banco.
        """
        self.client = PersistentClient(path=config.db_path)  # 🚀 Correção aqui
        self.collection = self.client.get_or_create_collection(name="chatbot_context")

    def add_context(self, context_id, context):
        """
        Adiciona um novo contexto ao banco de dados.
        """
        self.collection.add(documents=[context], ids=[context_id])

    def get_context(self, context_id):
        """
        Recupera o contexto salvo para um usuário específico.
        """
        result = self.collection.get(ids=[context_id])
        return result['documents'][0] if result['documents'] else None
