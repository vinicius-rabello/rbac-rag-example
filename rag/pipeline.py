from rag.document_loader import load_documents
from rag.embedder import generate_embedding_with_roles
from rag.retriever import MetadataFAISSRetriever
from rag.prompt_builder import build_prompt_from_file
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain.chains.combine_documents import create_stuff_documents_chain
import faiss

def run_query(user_role: str, query: str) -> str:
    # Carregar documentos e gerar embeddings
    documents = load_documents()
    embedding_array = generate_embedding_with_roles(documents)
    embedding_dim = embedding_array.shape[1] - 1
    index = faiss.IndexFlatL2(embedding_dim + 1)
    index.add(embedding_array)
    embedding_model = OllamaEmbeddings(model="phi3:mini")

    # Configurando o Retriever
    retriever = MetadataFAISSRetriever(index, embedding_model, embedding_dim, documents)
    retrieved_docs = retriever.retrieve(query, user_role)
    most_relevant_docs = retriever.score_documents(query, retrieved_docs)

    # Construindo o prompt
    prompt_template = build_prompt_from_file("resources/base_prompt.txt", user_role)

    # Rodando o modelo LLM
    llm = Ollama(model="phi3:mini", temperature=0.0)
    document_chain = create_stuff_documents_chain(llm, prompt_template)
    response = document_chain.invoke({"input": query, "context": most_relevant_docs})

    return response