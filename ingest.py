from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# import os

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TEXT_PATH = "backend/data/sample.txt"
DB_PATH = "backend/vectorstore"

loader = TextLoader(TEXT_PATH)
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=DB_PATH
)

print(f"Indexed {len(chunks)} chunks successfully.")