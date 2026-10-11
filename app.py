import streamlit as st

from components import education, experience, highlights, projects, sidebar, skills
from utils.loader import load

profile = load("profile", {})

st.set_page_config(
    page_title=f"{profile.get('name', 'Portfolio')} | Portfolio",
    page_icon="📄",
    layout="wide",
)

sidebar.render(profile)

st.title(profile.get("name", "Your Name"))
st.subheader(profile.get("title", ""))
st.write(profile.get("summary", ""))

tab_exp, tab_proj, tab_skills, tab_edu, tab_more = st.tabs(
    ["💼 Experience", "🚀 Projects", "🛠 Skills", "🎓 Education", "🏅 Achievements & Volunteering"]
)

with tab_exp:
    experience.render(load("experience", []))
with tab_proj:
    projects.render(load("projects", []))
with tab_skills:
    skills.render(load("skills", {}))
with tab_edu:
    education.render(load("education", []), load("certifications", []))
with tab_more:
    highlights.render(load("achievements", []), load("volunteer", []))
