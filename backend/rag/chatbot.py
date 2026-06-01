from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.chat_models import ChatOllama
from langchain.chains import ConversationalRetrievalChain

VECTOR_DB_PATH = "backend/rag/vector_store"

# Memory store
chat_history = []

# Embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Vector DB
db = Chroma(
    persist_directory=VECTOR_DB_PATH,
    embedding_function=embeddings
)

retriever = db.as_retriever()

# LLM
llm = ChatOllama(model="llama3")

# Conversational Chain
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever
)

def ask_question(question: str):

    global chat_history

    result = qa_chain.invoke({
        "question": question,
        "chat_history": chat_history
    })

    chat_history.append((question, result["answer"]))

    return result["answer"]
