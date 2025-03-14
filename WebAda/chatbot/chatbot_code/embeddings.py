from sentence_transformers import SentenceTransformer

class Embeddings:
    def __init__(self, config):
        """
        Inicializa o modelo de embeddings.

        Parâmetros:
        - config: Instância da classe Config contendo configurações do modelo.
        """
        self.model = SentenceTransformer(config.model_name)  # 🚀 Correção aqui!

    def encode(self, text):
        """
        Converte um texto em um vetor de embeddings.
        """
        return self.model.encode(text)
