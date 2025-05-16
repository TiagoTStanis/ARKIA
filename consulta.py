from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from utils.leitor_arquivos import load_and_process_files
from langchain.llms import Ollama
import os

# Configurações
DB_DIR = "./db"
DOCS_DIR = "./docs"

def initialize_db():
    # Carrega e processa arquivos
    documents = load_and_process_files(DOCS_DIR)
    
    # Cria o banco de vetores
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma.from_documents(
        documents,
        embeddings,
        persist_directory=DB_DIR
    )
    return db

def query_llama(query, db):
    # Busca documentos similares
    docs = db.similarity_search(query)
    context = "\n".join([doc.page_content for doc in docs])
    
    # Consulta o Llama3
    llm = Ollama(model="llama3")
    prompt = f"""Contexto:\n{context}\n\nPergunta: {query}\nResposta:"""
    return llm(prompt)

# Exemplo de uso
if __name__ == "__main__":
    if not os.path.exists(DB_DIR):
        db = initialize_db()
    else:
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        db = Chroma(persist_directory=DB_DIR, embedding_function=embeddings)
    
    resposta = query_llama("O que foi discutido no documento X?", db)
    print(resposta)