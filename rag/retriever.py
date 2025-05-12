import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Essa classe é responsável por recuperar documentos relevantes com base em um índice FAISS e um modelo de incorporação.
class MetadataFAISSRetriever:
    def __init__(self, index, embedding_model, embedding_dim, documents):
        self.index = index
        self.embedding_model = embedding_model
        self.embedding_dim = embedding_dim
        self.documents = documents
    
    # O método retrieve busca os documentos mais relevantes com base na consulta e no papel do usuário.
    def retrieve(self, query, user_role):
        query_embedding = self.embedding_model.embed_query(query)
        
        if user_role == "TI":
            query_role_value = 1
        elif user_role == "Financeiro":
            query_role_value = 2
        else:
            query_role_value = 3
        
        query_vector = np.array(query_embedding)
        distances, indices = self.index.search(query_vector.reshape(1, self.embedding_dim), k=5)
        
        retrieved_docs = []
        for i in indices[0]:
            if i < len(self.documents) and i >=0:
                doc_role_value = 0
                if "TI" in self.documents[i].metadata["role"]:
                    doc_role_value += 1
                if "Financeiro" in self.documents[i].metadata["role"]:
                    doc_role_value += 2
                if query_role_value & doc_role_value:
                    retrieved_docs.append(self.documents[i])
        
        return retrieved_docs
    
    # O método score_documents classifica os documentos recuperados com base na similaridade do cosseno entre a consulta e os documentos.
    def score_documents(self, query, retrieved_docs):
        query_embedding = np.array(self.embedding_model.embed_query(query)).reshape(1, -1)
        
        doc_embeddings = []
        for doc in retrieved_docs:
            doc_embedding = np.array(self.embedding_model.embed_query(doc.page_content))
            doc_embeddings.append(doc_embedding)
        doc_embeddings = np.array(doc_embeddings)
        
        similarities = cosine_similarity(query_embedding, doc_embeddings).flatten()
        scored_docs = [(doc, similarity) for doc, similarity in zip(retrieved_docs, similarities)]
        scored_docs.sort(key=lambda x: x[1], reverse=True)
        
        
        top_docs = [doc for doc, _ in scored_docs[:10]]
        return top_docs