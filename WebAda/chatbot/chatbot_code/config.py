import google.generativeai as genai
import chromadb
from sentence_transformers import SentenceTransformer

class Config:
    def __init__(self, api_key, db_path="./chroma_db", model_name="all-MiniLM-L6-v2"):
        """
        Classe responsável pela configuração do chatbot.

        Parâmetros:
        - api_key: Chave da API do Gemini AI
        - db_path: Caminho para o banco de dados do ChromaDB
        - model_name: Nome do modelo de embeddings a ser carregado
        """
        self.api_key = api_key
        self.db_path = db_path
        self.model_name = model_name

        # Configura a API do Gemini AI
        self.configure_gemini()

        # Inicializa o ChromaDB
        self.chroma_client = self.get_chroma_client()

        # Carrega o modelo de embeddings
        self.embedding_model = self.load_embedding_model()

    def configure_gemini(self):
        """
        Configura a API do Gemini AI com a chave fornecida.
        """
        genai.configure(api_key=self.api_key)

    def get_chroma_client(self):
        """
        Retorna um cliente do ChromaDB para armazenamento persistente.
        """
        return chromadb.PersistentClient(path=self.db_path)

    def load_embedding_model(self):
        """
        Carrega o modelo de embeddings especificado.
        """
        return SentenceTransformer(self.model_name)
