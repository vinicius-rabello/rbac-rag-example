import numpy as np
from langchain_ollama import OllamaEmbeddings

def generate_embedding_with_roles(documents, model_name="phi3:mini"):
    # Inicializa o modelo de embeddings
    embedding_model = OllamaEmbeddings(model=model_name)
    embedding_vectors = []

    for doc in documents:
        # Gera o embedding para o conteúdo do documento
        embedding = embedding_model.embed_query(doc.page_content)
        embedding_vectors.append(embedding)

    # Converte a lista de vetores em um array numpy
    return np.array(embedding_vectors)