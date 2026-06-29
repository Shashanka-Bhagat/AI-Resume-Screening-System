import os

from src.parser import extract_text
from src.similarity import calculate_similarity

with open("data/job_desc/job_description.txt",'r',encoding="utf-8") as file:
    job_description=file.read()

result=[]

resume_folder="data/resumes"

for resume_file in os.listdir(resume_folder):
    if resume_file.endswith('.pdf'):
        resume_path=os.path.join(resume_folder,resume_file)
        resume_text=extract_text(resume_path)
        score=calculate_similarity(resume_text,job_description)

        result.append((resume_file,score))
result.sort(key = lambda x: x[1],reverse=True)

print("=" * 40)
print("Resume Screening Results")
print("=" * 40)

for i,(resume,score) in enumerate(result, start=1):
    print(f"{i}. {resume} --> {score * 100:.2f}%")