import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embeddings():
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def create_or_load_vector_store(documents=None, index_path="models/faiss_index"):
    embeddings = get_embeddings()
    
    if documents:
        vector_store = FAISS.from_documents(documents, embeddings)
        vector_store.save_local(index_path)
        return vector_store
        
    if os.path.exists(index_path):
        return FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)
        
    raise FileNotFoundError("Indice FAISS nao encontrado. Forneca documentos para criar um novo.")