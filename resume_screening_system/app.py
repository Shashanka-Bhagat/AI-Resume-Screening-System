import streamlit as st
import os
from src.parser import extract_text
from src.similarity import calculate_similarity
from src.insights import calculate_skills_insights

st.set_page_config(page_title = "AI RESUME SCREENING", page_icon = "📄")

st.markdown("""
<style>

/* Background */

.stApp{
    background-color:#0F172A;
}

/* Main Title */

.title{
    font-size:45px;
    font-weight:bold;
    color:#38BDF8;
    text-align:center;
}

/* Subtitle */

.subtitle{
    text-align:center;
    color:white;
    font-size:18px;
    margin-bottom:30px;
}

/* Section Header */

.section{
    color:#FACC15;
    font-size:25px;
    font-weight:bold;
}

/* Footer */

.footer{
    text-align:center;
    color:gray;
    margin-top:40px;
}

</style>
""", unsafe_allow_html=True)



st.markdown(
"""
<div class="title">
🤖 AI Resume Screening System
</div>

<div class="subtitle">
Semantic Resume Ranking using NLP & Sentence Transformers
</div>
""",
unsafe_allow_html=True
)

with st.sidebar:

    st.header("📌 Project")

    st.write("Developer")
    st.success("Shashanka Bhagat")

    st.write("Model")
    st.info("all-MiniLM-L6-v2")

    st.write("Similarity")
    st.info("Cosine Similarity")

    st.markdown("---")
    st.header("⚙️ Ranking Settings")

    semantic_weight=st.slider(
        "🧠 Semantic Similarity Weight",
        min_value=0,
        max_value=100,
        value=70,
        step=5
    )
    skill_weight=100 - semantic_weight
    st.write(f"🛠 Skill Match Weight: **{skill_weight}%**")


st.info(
    "Upload a Job Description and one or more resumes. The system will rank candidates using Sentence Transformers and Cosine Similarity."
)

job_file=st.file_uploader("upload job file description",type=["txt"])
uploaded_resumes=st.file_uploader( "📂 Upload Resume(s)",type=["pdf"],accept_multiple_files=True)


if st.button(
    "🚀 Analyze Resumes",
    use_container_width=True
):
    if job_file is None:
        st.warning("📄 Upload Job Description")
    elif len(uploaded_resumes) == 0:
        st.warning("📂 Upload Resume PDFs")
    else:
        job_description=job_file.read().decode("utf-8")
        results = []

        for uploaded_resume in uploaded_resumes:
            resume_text=extract_text(uploaded_resume)
            semantic_score=calculate_similarity(resume_text,job_description)
            matched,missing,skill_score=calculate_skills_insights(job_description,resume_text)
            overall_score=(
                semantic_score * (semantic_weight / 100)
                +
                skill_score * (skill_weight / 100)
            )
            results.append((uploaded_resume.name,overall_score,semantic_score,skill_score,matched,missing))


        results.sort(key=lambda x: x[1],reverse=True)

        with st.spinner("Analyzing resumes..."):

            col1,col2,col3=st.columns(3)

            col1.metric(
                "📄 Resumes",
                len(results)
            )
            col2.metric(
                "🏆 Best Match",
                f"{results[0][1]*100:.2f}%"
            )
            col3.metric(
                "🤖 Model",
                "MiniLM"
            )

            top_resume=results[0]
            st.success(
                    f"🏆 Top Candidate: {top_resume[0]}"
                )
                          
            
            st.subheader("🏆 Candidate Rankings")

            for rank,(resume,overall_score,semantic_score,skill_score,matched,missing) in enumerate(results,start=1):

                if rank==1:
                    medal="🥇"
                elif rank==2:
                    medal="🥈"
                else:
                    medal="🥉"

                st.write(f"{medal} **{resume}**")

                st.progress(float(overall_score))

                col1,col2,col3=st.columns(3)
                with col1:
                    st.metric("🧠 Semantic", f"{semantic_score*100:.2f}%")

                with col2:
                    st.metric("🛠️ Skills", f"{skill_score*100:.2f}%")

                with col3:
                    st.metric("🏆 Overall", f"{overall_score*100:.2f}%")

                 
                st.write("### ✅ Matched Skills")
                if matched:
                    for skill in matched:
                        st.success(skill)
                else:
                    st.info("No matching skills found.")
                
                st.write("### ❌ Missing Skills")
                if missing:
                    for skill in missing:
                        st.error(skill)
                else:
                    st.info("No missing skills found.")

                if overall_score > 0.75:

                    st.success("Excellent Candidate - highly recommended for interview")

                elif overall_score > 0.50:

                    st.info("Good candidate - Consider for further evaluation")

                else:

                    st.warning("Needs Improvement - limited allignment with job description")

            st.divider()
st.markdown("---")

st.caption(
    "Built using Python • Streamlit • NLP • Sentence Transformers"
)