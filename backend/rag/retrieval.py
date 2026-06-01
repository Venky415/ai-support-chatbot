from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

VECTOR_DB_PATH = "backend/rag/vector_store"

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory=VECTOR_DB_PATH,
    embedding_function=embeddings
)

query = "How can I reset my password?"

results = db.similarity_search(query, k=2)

print("\nQuery:", query)
print("----- Retrieved Documents -----")

for i, doc in enumerate(results):
    print(f"\nResult {i+1}:")
    print(doc.page_content)
