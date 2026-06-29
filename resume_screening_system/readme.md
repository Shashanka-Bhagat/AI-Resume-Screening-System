# 📄 AI-Powered Resume Screening System using NLP and Sentence Transformers

An AI-powered Resume Screening System that compares multiple resumes against a job description using **Natural Language Processing (NLP)**, **Sentence Transformers**, and **Cosine Similarity**. The application ranks candidates based on semantic similarity and provides an intuitive web interface built with Streamlit.

---

## 📌 Project Overview

Recruiters often spend significant time manually reviewing resumes to identify suitable candidates. This project automates the initial screening process by leveraging transformer-based language models to compare resumes with a given job description.

The system extracts text from PDF resumes, preprocesses the content, generates semantic embeddings using a pre-trained transformer model, and ranks candidates according to their similarity score.

---

## 🎯 Objectives

- Automate resume screening.
- Reduce manual effort in candidate selection.
- Compare resumes using semantic understanding instead of simple keyword matching.
- Provide an easy-to-use web interface for recruiters.

---

## ✨ Features

- 📄 Upload Job Description (.txt)
- 📂 Upload Multiple Resume PDFs
- 📑 Automatic PDF Text Extraction
- 🧹 NLP Text Preprocessing
- 🤖 Sentence Transformer Embeddings
- 📊 Cosine Similarity Based Matching
- 🏆 Automatic Resume Ranking
- 🌐 Interactive Streamlit Web Application

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | Web Application |
| pdfplumber | PDF Text Extraction |
| NLTK | NLP Preprocessing |
| Sentence Transformers | Text Embeddings |
| Scikit-Learn | Cosine Similarity |
| PyTorch | Deep Learning Backend |

---

## 📂 Project Structure

```text
resume_screening_system/
│
├── app.py                      # Streamlit Application
├── main.py                     # Backend Testing
├── requirements.txt
├── README.md
├── .gitignore
│
├── data
│   ├── sample_job_description.txt
│   └── sample_resumes
│
├── src
│   ├── parser.py
│   ├── preprocessing.py
│   ├── similarity.py
│   ├── insights.py
│   └── utils.py
│
├── screenshots
│
├── notebooks
│
└── models
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/resume_screening_system.git
```

### Navigate to the project folder

```bash
cd resume_screening_system
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## 🚀 Workflow

```text
Upload Job Description
          │
          ▼
Upload Resume(s)
          │
          ▼
Extract Text from PDFs
          │
          ▼
NLP Preprocessing
          │
          ▼
Generate Sentence Embeddings
          │
          ▼
Cosine Similarity
          │
          ▼
Rank Candidates
          │
          ▼
Display Results
```

---

## 🧠 AI Model Used

### Sentence Transformer

Model:

```
all-MiniLM-L6-v2
```

The model converts textual information into dense vector embeddings that capture semantic meaning. These embeddings allow the system to compare resumes and job descriptions based on context rather than simple keyword matching.

---

## 📈 Similarity Algorithm

The project uses **Cosine Similarity** to measure semantic similarity between resume embeddings and job description embeddings.

Similarity Score:

```
1.0  → Perfect Match

0.0  → No Similarity

-1.0 → Completely Opposite
```

Higher scores indicate a better match.

---


## 📌 Example Output

```text
Resume Screening Results

🥇 Resume_1.pdf → 85.42%

🥈 Resume_3.pdf → 72.81%

🥉 Resume_2.pdf → 61.33%
```

---

## 🚀 Future Improvements

- Explainable AI (Matched & Missing Skills)
- ATS Score Prediction
- Support for DOCX Resumes
- Candidate Recommendation System
- Resume Summarization using LLMs
- Recruiter Dashboard
- Database Integration
- Authentication System

---

## 👨‍💻 Author

**Shashanka Bhagat**

B.Tech Computer Science Engineering

AI Capstone Project

2026

---

## 📄 License

This project is developed for educational and learning purposes.