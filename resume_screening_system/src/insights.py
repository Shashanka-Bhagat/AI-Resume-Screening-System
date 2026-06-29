import pandas as pd

def load_skills():
    return pd.read_csv("data/skills.csv")

def extract_skills(job_description):
    skills_df=load_skills()
    required=[]
    job_lower=job_description.lower()
    for _, row in skills_df.iterrows():
        skill=str(row["Skill"]).strip().lower()
        if skill in job_lower:
            required.append(row)
    return required


def calculate_skills_insights(job_description,resume_text):

    required_skills=extract_skills(job_description)

    matched=[]
    missing=[]


    resume_lower=resume_text.lower()

    for skill in required_skills:
        skill_name=str(skill["Skill"]).strip()
        if skill_name.lower() in resume_lower:
            matched.append(skill_name)
        else:
            missing.append(skill_name)

    if len(required_skills) == 0:
        skill_score=0
    else:
        skill_score= len(matched)/len(required_skills)
    return matched,missing,skill_score