import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

# ---------------------------------------------------
# Load Profile Data Safely (No path errors)
# ---------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "Data", "profile.txt")

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"{DATA_PATH} not found")

with open(DATA_PATH, "r", encoding="utf-8") as f:
    text = f.read()

# ---------------------------------------------------
# Split Text into Chunks
# ---------------------------------------------------

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = splitter.create_documents([text])

# ---------------------------------------------------
#  Local Embeddings (FREE - Ollama)
# ---------------------------------------------------

embeddings = OllamaEmbeddings(model="nomic-embed-text")

# ---------------------------------------------------
# Create FAISS Vector Store
# ---------------------------------------------------

vectorstore = FAISS.from_documents(docs, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# ---------------------------------------------------
#  Local LLM (Choose Model)
# ---------------------------------------------------

# Option A (Recommended – Fast & Lightweight)
llm = ChatOllama(model="phi3")

# Option B (Stronger but heavier)
# llm = ChatOllama(model="llama3")

# ---------------------------------------------------
# Prompt Template
# ---------------------------------------------------

prompt = ChatPromptTemplate.from_template("""
You are a helpful AI assistant for Amit Ranjan's portfolio website.

Answer strictly using the context below.
If the answer is not present in the context, say:
"I don't have that information."

Keep answers concise and professional.

Context:
{context}

Question:
{question}
""")

# ---------------------------------------------------
#   Build RAG Chain
# ---------------------------------------------------

rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
)

# ---------------------------------------------------
#  Function to Call from FastAPI
# ---------------------------------------------------

def get_response(question: str) -> str:
    result = rag_chain.invoke(question)
    return result.content
