import os
import xml.etree.ElementTree as ET
from langchain_core.documents import Document

def load_lexml_documents(raw_dir="data/raw"):
    documents = []
    
    if not os.path.exists(raw_dir):
        return documents
        
    for filename in os.listdir(raw_dir):
        if filename.endswith(".xml"):
            filepath = os.path.join(raw_dir, filename)
            # Parse do XML e extração de texto limpo
            tree = ET.parse(filepath)
            root = tree.getroot()
            
            text = " ".join(root.itertext()).strip()
            
            if text:
                doc = Document(page_content=text, metadata={"source": filename})
                documents.append(doc)
                
    return documents