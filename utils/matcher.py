from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

def get_similarity(resume_text, jd_text):
    model = load_model()
    embeddings = model.encode([resume_text, jd_text])
    score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    return round(score * 100, 2)