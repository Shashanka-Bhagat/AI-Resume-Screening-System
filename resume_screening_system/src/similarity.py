from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def calculate_similarity(resume_text,job_text):
    resume_embedding = model.encode([resume_text])
    job_embedding = model.encode([job_text])

    score = cosine_similarity(resume_embedding,job_embedding)

    return score[0][0]