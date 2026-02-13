from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from rag import get_response

# Updated Ollama imports (no deprecation warning)
from langchain_ollama import OllamaEmbeddings, ChatOllama

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

import os

# ===============================
# FastAPI App
# ===============================
app = FastAPI()

# ===============================
# Enable CORS (for frontend)
# ===============================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Later restrict to your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===============================
# Load Knowledge Base
# ===============================
DATA_PATH = "Data/profile.txt"

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"{DATA_PATH} not found")

with open(DATA_PATH, "r", encoding="utf-8") as f:
    text = f.read()

# ===============================
# Split Text into Chunks
# ===============================
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = splitter.create_documents([text])

# ===============================
# Embeddings (Local - Free)
# ===============================
embeddings = OllamaEmbeddings(model="nomic-embed-text")

# ===============================
# Vector Store
# ===============================
vectorstore = FAISS.from_documents(docs, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# ===============================
# Local LLM (Choose Model)
# ===============================
# Use "phi3" or "llama3"
llm = ChatOllama(model="phi3")

# ===============================
# Prompt Template
# ===============================
prompt = ChatPromptTemplate.from_template("""
You are an AI assistant for Amit Ranjan's portfolio website.

Answer ONLY using the context below.
If the answer is not in the context, say:
"I don't have that information in my knowledge base."

Keep answers concise and professional.

Context:
{context}

Question:
{question}
""")

# ===============================
# RAG Chain
# ===============================
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
)

# ===============================
# Request Schema
# ===============================
class Query(BaseModel):
    question: str

# ===============================
# Chat Endpoint
# ===============================
@app.post("/chat")
def chat(query: Query):
    answer = get_response(query.question)
    return {"answer": answer}

# ===============================
# Health Check
# ===============================
@app.get("/")
def root():
    return {"status": "Portfolio RAG chatbot is running "}
