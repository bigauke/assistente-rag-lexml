import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embeddings():
    # Inicializa o modelo de embedding da HuggingFace
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def create_or_load_vector_store(documents=None, index_path="models/faiss_index"):
    embeddings = get_embeddings()
    
    # Se documentos forem passados, cria um novo índice
    if documents:
        vector_store = FAISS.from_documents(documents, embeddings)
        vector_store.save_local(index_path)
        return vector_store
        
    # Caso contrário, tenta carregar um índice existente
    if os.path.exists(index_path):
        return FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)
        
    raise FileNotFoundError("Índice FAISS não encontrado. Forneça documentos para criar um novo.")