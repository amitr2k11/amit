Perfect 😎🔥
Here is your **GitHub-optimized README.md with professional badges** — clean, modern, recruiter-friendly, and impressive.

You can copy-paste this directly into your `README.md`.

---

# 🚀 AI-Powered Portfolio Chatbot

### Retrieval-Augmented Generation (RAG) using FastAPI + Ollama

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green?logo=fastapi)
![LangChain](https://img.shields.io/badge/LangChain-RAG-purple)
![FAISS](https://img.shields.io/badge/FAISS-VectorStore-orange)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-black)
![Cloudflare](https://img.shields.io/badge/Cloudflare-Tunnel-F38020?logo=cloudflare)
![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Frontend-222?logo=github)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

</p>

---

## 🌐 Live Demo

* 🌍 **Portfolio Website:**
  👉 [https://amitr2k11.github.io/](https://amitr2k11.github.io/)

* 🤖 **AI Chatbot (Backend via Cloudflare Tunnel)**
  Dynamically answers questions about my experience using RAG.

---

## 🧠 Project Overview

This project integrates a **Retrieval-Augmented Generation (RAG)** chatbot directly into my personal portfolio website.

Instead of hardcoded responses, the chatbot:

1. Splits knowledge from `profile.txt`
2. Converts it into embeddings
3. Stores them in FAISS vector database
4. Retrieves relevant context
5. Generates intelligent answers using a local LLM (phi3 / llama3)

All powered locally — **no OpenAI API cost**.

---

## 🏗️ Architecture

```
User (Frontend - GitHub Pages)
        │
        ▼
JavaScript Fetch Request
        │
        ▼
FastAPI Backend (/chat)
        │
        ▼
FAISS Vector Store (RAG Retrieval)
        │
        ▼
Ollama LLM (phi3 / llama3)
        │
        ▼
Response → Typing Animation UI
```

---

## 🧩 Tech Stack

### 🔹 Frontend

* HTML
* CSS
* JavaScript
* GitHub Pages

### 🔹 Backend

* FastAPI
* LangChain
* FAISS
* Ollama (Local LLM)
* Cloudflare Tunnel

### 🔹 AI Models

* `phi3` or `llama3` → Response generation
* `nomic-embed-text` → Embeddings

---

## 📁 Project Structure

```
amit.github.io/
│
├── index.html
├── styles.css
├── README.md
│
└── chatbot-backend/
    ├── app.py
    ├── requirements.txt
    ├── Data/
    │   └── profile.txt
    └── .env (ignored)
```

---

## ⚙️ Local Setup

### 1️⃣ Install Ollama

Download:
👉 [https://ollama.com/](https://ollama.com/)

Pull required models:

```bash
ollama pull phi3
ollama pull nomic-embed-text
```

---

### 2️⃣ Run Backend

```bash
cd chatbot-backend
pip install -r requirements.txt
uvicorn app:app --reload
```

Runs at:

```
http://127.0.0.1:8000
```

---

### 3️⃣ Expose Backend (Cloudflare Tunnel)

```bash
cloudflared tunnel --url http://127.0.0.1:8000
```

Copy generated URL and update in:

```js
fetch("https://your-tunnel-url/chat")
```

---

## 🔐 Security

* `.env` excluded via `.gitignore`
* No API keys committed
* GitHub secret scanning enabled
* Fully local LLM (no external API dependency)

---

## 🎯 Why This Project Is Impressive

✔ End-to-end AI system
✔ Real RAG implementation
✔ Local LLM deployment
✔ Production debugging (Git conflicts, secret scanning, tunnel setup)
✔ Frontend + Backend integration
✔ No paid API usage

This demonstrates:

* AI Engineering skills
* Full-stack capability
* Deployment understanding
* Secure development practices

---

## 🚀 Future Improvements

* Persistent backend hosting (Railway / Render alternative)
* Streaming token responses
* Chat memory support
* Admin dashboard for knowledge updates
* SaaS-ready chatbot widget

---

## 👨‍💻 About Me

**Amit Ranjan**
Product Consultant | AI Builder | Data-Driven Problem Solver

🔗 LinkedIn:
[https://www.linkedin.com/in/amitrnjan/](https://www.linkedin.com/in/amitrnjan/)

🌐 Portfolio:
[https://amitr2k11.github.io/](https://amitr2k11.github.io/)

---

## ⭐ If You Like This Project

Give it a ⭐ on GitHub — it motivates further AI builds!
