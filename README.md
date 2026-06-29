#  Resumer — AI Resume Analyzer

> Upload your resume, enter your target job role, and get instant AI-powered feedback in seconds.

---

##  What is this?

**Resumer** is an AI-powered resume analyzer that reads your resume (PDF) and tells you:

- How well it scores on ATS (Applicant Tracking Systems)
- What you are doing right
- What needs improvement
- Which keywords are missing for your target role
- Specific suggestions to make your resume stronger

---

##  Features

-  **PDF Upload** — Just drag and drop your resume
-  **Role-Based Analysis** — Enter any job role (e.g. GenAI Analyst, Data Scientist)
-  **ATS Score** — Know how recruiter-friendly your resume is
-  **Strengths & Weaknesses** — Honest, detailed feedback
-  **Missing Keywords** — Know exactly what to add
-  **Improvement Suggestions** — 5 actionable steps to improve

---

##  Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Streamlit | Web UI |
| Groq API | AI brain (LLaMA 3) |
| pdfplumber | Read PDF files |
| python-dotenv | Manage API keys securely |

---


##  How to Use

1. Open the app in your browser
2. Type your **target job role** (e.g. GenAI Analyst)
3. Upload your **resume as PDF**
4. Click **Analyze Resume →**
5. Get your detailed feedback instantly!

---

##  Project Structure

```
ai-resume-analyzer/
│
├── app.py              ← Main application file
├── requirements.txt    ← All dependencies
├── .env                ← Your API key (never share this!)
├── .gitignore          ← Files excluded from GitHub
└── README.md           ← You are here!
```


