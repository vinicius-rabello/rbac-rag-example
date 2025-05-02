import numpy as np
from langchain_community.embeddings import OllamaEmbeddings

def generate_embedding_with_roles(documents, model_name="phi3:mini"):
    # Inicializa o modelo de embeddings
    embedding_model = OllamaEmbeddings(model=model_name)
    embedding_vectors = []

    for doc in documents:
        # Gera o embedding para o conteúdo do documento
        embedding = embedding_model.embed_query(doc.page_content)
        
        # Inicializa o valor do papel
        role_value = 0
        
        # Adiciona valores baseados nos papéis presentes na metadata
        if "TI" in doc.metadata["role"]:
            role_value += 1
        if "Financeiro" in doc.metadata["role"]:
            role_value += 2
        
        # Concatena o embedding com o valor do papel
        extended_vector = np.concatenate([embedding, [role_value]])
        embedding_vectors.append(extended_vector)

    # Converte a lista de vetores em um array numpy
    return np.array(embedding_vectors)