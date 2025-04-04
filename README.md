# fastapi-langchain-sample
🚀 A FastAPI-powered LangChain server that generates essays and poems based on user prompts.

# FastAPI + LangChain Sample 🚀

This repository showcases a minimal example of using **FastAPI** together with **LangChain** to build a local server that generates **essays** and **poems** from user prompts. It demonstrates how to create multiple routes for different types of LLM outputs.

## 🧠 Features

- `/essay`: Generates an essay based on a given topic.
- `/poem`: Returns a poem related to the prompt.
- `/openai`: Directly interacts with the base OpenAI chat model.

## 🔧 Tech Stack

- [LangChain](https://www.langchain.com/)
- [OpenAI API](https://platform.openai.com/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [LangServe](https://python.langchain.com/docs/guides/production/langserve)
- Python 3.10+

## ▶️ How to Run

```bash
# Activate your environment
source venv/bin/activate  # or .\venv\Scripts\activate on Windows

# Run the FastAPI app
python app.py
