# SmartResume AI 🚀

## Overview

SmartResume AI is a simple local tool I built to analyze how well a resume matches a given job description. The goal was to create something practical that can highlight strengths, identify missing skills, and give useful feedback — all running completely offline using open-source tools.

---

## What it does

* Calculates a match score between resume and job description
* Identifies matching skills (strengths)
* Highlights missing skills that can be improved
* Provides basic suggestions to improve the resume

---

## Tech Stack

This project is built entirely with open-source tools:

* Python
* Streamlit (for UI)
* spaCy (text processing)
* sentence-transformers (semantic similarity)
* pdfplumber (PDF parsing)

---

## Features

* Upload resume in PDF format
* Paste or input job description
* Computes similarity using embeddings
* Skill-based comparison with gap analysis
* Simple and clean interface

---

## How to run locally

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
streamlit run app.py
```

---

## Example output

* Match Score: ~50–60%
* Strengths: Python, Machine Learning
* Missing Skills: AWS, Docker, APIs

---

## Project structure

```
SmartResumeAI/
│── app.py
│── requirements.txt
│── utils/
│── README.md
```

---

## Notes

* Everything runs locally — no external APIs used
* Focus was on keeping the system simple and understandable
* Skill matching is rule-based with basic normalization

---

## Possible improvements

* Generate downloadable PDF reports
* Improve skill extraction using better NLP techniques
* Add support for multiple resumes (batch analysis)
* Enhance scoring logic for better accuracy
