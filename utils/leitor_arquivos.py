import os
from langchain.document_loaders import (
    UnstructuredFileLoader,
    UnstructuredPDFLoader,
    UnstructuredWordDocumentLoader,
    UnstructuredExcelLoader,
    UnstructuredPowerPointLoader,
)
from langchain.text_splitter import RecursiveCharacterTextSplitter
import easyocr
import whisper
from moviepy.editor import VideoFileClip
from langchain.schema import Document

# Configurações
SUPPORTED_EXTENSIONS = {
    ".pdf": UnstructuredPDFLoader,
    ".docx": UnstructuredWordDocumentLoader,
    ".xlsx": UnstructuredExcelLoader,
    ".pptx": UnstructuredPowerPointLoader,
    ".txt": UnstructuredFileLoader,
    ".png": "ocr",
    ".jpg": "ocr",
    ".mp4": "video",
}

reader = easyocr.Reader(['pt'])  # OCR para imagens
whisper_model = whisper.load_model("base")  # Transcrição de vídeos

def extract_text_from_image(image_path):
    result = reader.readtext(image_path, detail=0)
    return " ".join(result)

def extract_text_from_video(video_path):
    video = VideoFileClip(video_path)
    video.audio.write_audiofile("temp_audio.mp3")
    result = whisper_model.transcribe("temp_audio.mp3", language="pt")
    os.remove("temp_audio.mp3")  # Limpeza
    return result["text"]

def load_and_process_files(docs_dir):
    documents = []
    for root, _, files in os.walk(docs_dir):
        for file in files:
            file_path = os.path.join(root, file)
            ext = os.path.splitext(file)[1].lower()
            
            if ext in SUPPORTED_EXTENSIONS:
                try:
                    if SUPPORTED_EXTENSIONS[ext] == "ocr":
                        text = extract_text_from_image(file_path)
                        doc = Document(page_content=text, metadata={"source": file_path})
                        documents.append(doc)
                    elif SUPPORTED_EXTENSIONS[ext] == "video":
                        text = extract_text_from_video(file_path)
                        doc = Document(page_content=text, metadata={"source": file_path})
                        documents.append(doc)
                    else:
                        loader = SUPPORTED_EXTENSIONS[ext](file_path)
                        docs = loader.load()
                        documents.extend(docs)
                except Exception as e:
                    print(f"Erro ao processar {file_path}: {e}")
    
    # Divide os textos em chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n", "\n", " ", ""]
    )
    return text_splitter.split_documents(documents)