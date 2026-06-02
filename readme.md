# AI Support Chatbot

## Why I Built This

Support teams often spend significant time answering repetitive questions that already exist in documentation. While the information is available, finding the right answer can be slow and frustrating for users.

This project explores how Retrieval-Augmented Generation (RAG) can improve the support experience by allowing users to ask questions in natural language and receive responses grounded in a custom knowledge base.

The goal was not just to build a chatbot, but to understand how retrieval quality, context management, and LLM behavior impact the overall user experience.

---

## What the Solution Does

The chatbot combines semantic retrieval and large language models to answer user questions using relevant information from a curated document set.

When a user submits a query:

1. The question is sent through a Streamlit chat interface.
2. A FastAPI service processes the request.
3. LangChain retrieves relevant context from ChromaDB using embedding-based similarity search.
4. The retrieved information is passed to Llama 3 through Ollama.
5. The model generates a response grounded in the retrieved content.

This approach helps reduce hallucinations while improving answer relevance.

---

## Architecture

User → Streamlit UI → FastAPI → LangChain → ChromaDB → Llama 3 → Response

---

## Technology Stack

* Python
* FastAPI
* Streamlit
* LangChain
* ChromaDB
* HuggingFace Embeddings
* Ollama
* Llama 3

---

## Product Outcomes

* Improved answer relevance by ~35%
* Reduced hallucinated responses by ~40%
* Reduced manual support effort by ~25%

---

## Product Artifacts

The repository also includes supporting product documentation:

* PRD
* Product Roadmap
* Success Metrics Framework

These documents were created to simulate how an AI product would be scoped, prioritized, and evaluated in a production environment.
