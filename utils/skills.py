import spacy
nlp = spacy.load("en_core_web_sm")


COMMON_SKILLS = {
    "python": ["python"],
    "machine learning": ["machine learning", "ml"],
    "deep learning": ["deep learning", "dl"],
    "nlp": ["nlp", "natural language processing"],
    "tensorflow": ["tensorflow"],
    "pytorch": ["pytorch"],
    "sql": ["sql"],
    "data analysis": ["data analysis", "data analytics"],
    "api": ["api", "apis", "rest api", "rest apis"],
    "git": ["git"],
    "aws": ["aws", "amazon web services"],
    "gcp": ["gcp", "google cloud"],
    "communication": ["communication", "communication skills"]
}


def preprocess(text):
    text = text.lower()
    text = text.replace("-", " ")
    text = text.replace("/", " ")
    return text


def extract_skills(text):
    text = preprocess(text)
    found = set()

    for skill, variants in COMMON_SKILLS.items():
        for v in variants:
            if v in text:
                found.add(skill)
                break

    return found


def skill_match(resume_text, jd_text):
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    matched = resume_skills.intersection(jd_skills)
    missing = jd_skills - resume_skills

    if len(jd_skills) == 0:
        return 0, matched, missing

    score = len(matched) / len(jd_skills) * 100
    return round(score, 2), matched, missing