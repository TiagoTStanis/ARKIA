import gradio as gr
from consulta import query_llama, initialize_db
import os
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

DB_DIR = "./db"

def respond(query, history):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma(persist_directory=DB_DIR, embedding_function=embeddings)
    return query_llama(query, db)

if not os.path.exists(DB_DIR):
    initialize_db()

gr.ChatInterface(respond).launch()