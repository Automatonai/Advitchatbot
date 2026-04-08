# On-Premise Chatbot (Llama 3.2 + Streamlit + Docker)

A simple chatbot UI built with **Streamlit** and powered by **Meta Llama 3.2** using Hugging Face Transformers.

The bot responds in the same way as the user wants it or defined in the system_prompt and supports continuous conversation.

---

## 🚀 Features

- 🧠 LLM: Llama-3.2
- 💬 Continuous chat (multi-turn memory)
- ⚡ Streamlit chat UI
- 🐳 Dockerized setup
- 💾 Persistent model cache (no repeated downloads)

---

## 📁 Project Structure
```
├── app.py
├── Dockerfile
├── docker-compose.yaml
├── requirements.txt
└── README.md
```

---

## 🛠️ Prerequisites

- Docker
- Docker Compose
- A HuggingFace account for fetching model with finegrained access token

---

## ▶️ Run with Docker Compose

```bash
docker compose up -d --build


Then open:

👉 http://localhost:8501

```

## 🧠 How it works
- Loads the model using Hugging Face pipeline
- Stores chat history in Streamlit session state
- Sends full conversation context on each request
- Generates personlisted responses

## ⚙️ Configuration

Streamlit runs with:

```bash
streamlit run ui.py \
  --server.address=0.0.0.0 \
  --server.port=8501 \
  --server.headless=True \
  --server.enableCORS=False
```

## 🧪 Local Development (without Docker)

1. Install dependencies

```bash
pip install -r requirements.txt
```

2. Run app

```bash
streamlit run app.py
```

## 🚀 Future Improvements
- Streaming responses (typing effect)
- Chat reset button
- Model selection
- Deployment (AWS / GCP / Render)
