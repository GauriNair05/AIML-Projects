# Retrieval-Augmented Generation (RAG) Project

An end-to-end implementation of a Retrieval-Augmented Generation (RAG) pipeline designed to ground Large Language Model (LLM) responses using custom document context.

## Overview

This project implements a RAG architecture that extracts context from external documents, converts them into vector embeddings, and injects relevant chunks into prompt context to generate factual answers.

## Tech Stack

* Python
* LangChain / LlamaIndex
* ChromaDB / FAISS
* OpenAI API / HuggingFace Transformers

## Getting Started

1. Navigate to the project directory:
   cd rag_project

2. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate

3. Install dependencies:
   pip install -r requirements.txt

4. Create a .env file and add your API key:
   OPENAI_API_KEY=your_api_key_here

## Usage

Run the main pipeline:
python main.py
