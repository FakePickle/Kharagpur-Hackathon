from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from transformers import pipeline
import faiss
import numpy as np

# Step 1: Load models
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
generator = pipeline("text2text-generation", model="t5-small")

# Step 2: Prepare corpus and create FAISS index
corpus = [
    "Document 1 content about drones and clustering techniques.",
    "Document 2 talks about applications of machine learning.",
    "Document 3 explores natural language processing for text classification."
]
corpus_embeddings = embedding_model.encode(corpus, convert_to_tensor=False)

d = corpus_embeddings.shape[1]
index = faiss.IndexFlatL2(d)  # L2 distance metric
index.add(np.array(corpus_embeddings))

# Step 3: Define RAG pipeline
def rag_pipeline(query):
    # Retrieve relevant documents
    query_embedding = embedding_model.encode(query, convert_to_tensor=False)
    D, I = index.search(np.array([query_embedding]), k=3)
    retrieved_docs = [corpus[i] for i in I[0]]
    
    # Generate response
    context = " ".join(retrieved_docs)
    prompt = f"Based on the following documents: {context}. Answer the question: {query}"
    response = generator(prompt, max_length=100)
    return response[0]["generated_text"]

# Define input schema using Pydantic
class Query(BaseModel):
    query: str

# Step 4: Set up FastAPI
app = FastAPI()

@app.post("/rag")
def run_rag(query: Query):
    response = rag_pipeline(query.query)
    return {"query": query.query, "response": response}