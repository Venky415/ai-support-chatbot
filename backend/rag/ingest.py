import os
import glob
from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Load environment variables
load_dotenv()

# Path to data folder
DATA_PATH = "data"

# Vector DB path
VECTOR_DB_PATH = "backend/rag/vector_store"


def ingest_documents():
    documents = []

    # Load all txt files automatically
    for file in glob.glob(f"{DATA_PATH}/*.txt"):
        loader = TextLoader(file)
        documents.extend(loader.load())

    # Split text into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    # Create embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Store in vector DB
    Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=VECTOR_DB_PATH
    )

    print("✅ Documents ingested successfully into vector database")


if __name__ == "__main__":
    ingest_documents()
