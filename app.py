import streamlit as st
import pdfplumber
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="Resume Analyzer", page_icon="📄", layout="centered")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .header { text-align: center; padding: 3rem 0 2rem 0; border-bottom: 1px solid #f0f0f0; margin-bottom: 2.5rem; }
    .header h1 { font-size: 1.8rem; font-weight: 600; color: #111111; letter-spacing: -0.5px; margin-bottom: 0.4rem; }
    .header-badge { display: inline-block; background: #16a34a; color: white; font-size: 0.7rem; font-weight: 600; padding: 0.25rem 0.75rem; border-radius: 4px; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 1rem; }
    .header h1 { font-size: 3rem; font-weight: 700; color: #ffffff; letter-spacing: -1px; margin-bottom: 0.2rem; }
    .header-sub { font-size: 1rem; color: #16a34a; font-weight: 500; margin-bottom: 0.3rem; letter-spacing: 2px; text-transform: uppercase; }
    .header p { font-size: 0.95rem; color: #888888; font-weight: 300; }
    .section-label { font-size: 0.75rem; font-weight: 500; color: #999999; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.5rem; }
    .stButton > button { background-color: #16a34a; color: white; border: none; border-radius: 4px; padding: 0.6rem 1.8rem; font-size: 0.9rem; font-weight: 500; width: 100%; }
    .stButton > button:hover { background-color: #15803d; color: white; }
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header">
    <div class="header-badge">AI Powered</div>
    <h1>Resume Analyzer</h1>
    <p class="header-sub"> Check Your ATS </p>
    <p>Upload your resume and get instant AI-powered feedback</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-label">Target Role</div>', unsafe_allow_html=True)
job_role = st.text_input("", placeholder="e.g. GenAI Analyst, Data Scientist", label_visibility="collapsed")

st.markdown('<br>', unsafe_allow_html=True)

st.markdown('<div class="section-label">Resume (PDF)</div>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=["pdf"], label_visibility="collapsed")

st.markdown('<br>', unsafe_allow_html=True)

def extract_text(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def analyze_resume(resume_text, role):
    prompt = f"""
You are a professional ATS resume reviewer and career coach.

Analyze the resume below for the role: {role}

Resume:
{resume_text}

Provide a structured analysis with the following sections:

1. **ATS Score** — Score out of 100 with a one-line reason
2. **Strengths** — 3 to 5 key strengths of this resume
3. **Weaknesses** — 3 to 5 areas that need improvement
4. **Missing Keywords** — Important keywords missing for the target role
5. **Improvement Suggestions** — 5 actionable, specific suggestions

Keep the tone professional, concise, and constructive.
"""
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

if uploaded_file and job_role:
    if st.button("Analyze Resume →"):
        with st.spinner("Analyzing your resume..."):
            resume_text = extract_text(uploaded_file)
            if resume_text.strip() == "":
                st.error("Could not extract text from this PDF. Please try a different file.")
            else:
                result = analyze_resume(resume_text, job_role)
                st.markdown("---")
                st.markdown(result)

elif uploaded_file and not job_role:
    st.info("Please enter a target job role to begin analysis.")

elif not uploaded_file and job_role:
    st.info("Please upload your resume PDF to continue.")