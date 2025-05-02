from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

# Define os papéis para cada documento (isso pode ser passado em um arquivo de configuração ou variável de ambiente)
text_files = {
    "doc1.txt": ["TI"],
    "doc2.txt": ["TI", "Financeiro"],
    "doc3.txt": ["Financeiro"],
    "doc4.txt": ["TI"],
}

def load_documents(data_path="data", chunk_size=1000, chunk_overlap=100):
    docs = []
    
    # Carrega todos os arquivos .txt na pasta data
    for filename in os.listdir(data_path):
        if filename.endswith(".txt"):
            loader = TextLoader(os.path.join(data_path, filename))
            loaded_docs = loader.load()
            for doc in loaded_docs:
                # Adiciona o nome do arquivo como fonte na metadata
                doc.metadata["source"] = filename

            docs.extend(loaded_docs)

    # Divide os documentos em pedaços menores
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    documents = text_splitter.split_documents(docs)

    # Adiciona o papel correspondente a cada documento, mapeando o nome do arquivo para o papel
    for doc in documents:
        doc.metadata["role"] = text_files[doc.metadata["source"]]
    
    return documents