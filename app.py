import streamlit as st

status = st.empty()
status.write("App is running... It may take some time.....please wait")

from utils.parser import extract_text_from_pdf
from utils.language import is_english
from utils.matcher import get_similarity
from utils.skills import skill_match
from utils.scorer import final_score

st.title("SmartResume AI")
status.empty()


resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
jd_text = st.text_area("Paste Job Description")

if st.button("Analyze"):
    if not resume_file or not jd_text:
        st.error("Please upload resume and enter job description")
    else:
        resume_text = extract_text_from_pdf(resume_file)

        if not resume_text:
            st.error("Error reading PDF")
        elif not is_english(resume_text):
            st.error("Resume must be in English")
        elif len(resume_text) < 50:
            st.warning("Resume too short for analysis")
        elif len(jd_text) < 30:
            st.warning("Job description too vague")
        else:
         
            with st.spinner("Analyzing resume..."):
                sim_score = get_similarity(resume_text, jd_text)
                skill_score, matched, missing = skill_match(resume_text, jd_text)


                if skill_score > 40:
                    sim_score += 10

                final = final_score(sim_score, skill_score)

        
            st.success(f"Match Score: {final:.1f}%")

            st.subheader("✅ Strengths")
            for s in matched:
                st.write("-", s)

            st.subheader("⚠️ Missing Skills")
            for s in missing:
                st.write("-", s)

            st.subheader("💡 Suggestions")

            if missing:
                st.write("Consider adding the following skills to improve your match:")
                for s in missing:
                    st.write("-", s)
            else:
                st.write("Great! Your resume matches most required skills.")