import streamlit as st


def render(education, certifications):
    for e in education:
        with st.container(border=True):
            st.markdown(f"**{e['degree']}**")
            st.caption(f"{e['school']} · {e['period']}")
            if e.get("details"):
                st.write(e["details"])
    if certifications:
        st.markdown("**Certifications**")
        for c in certifications:
            st.markdown(f"- {c}")
