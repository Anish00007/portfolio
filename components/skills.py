import streamlit as st


def render(skills):
    if not skills:
        st.info("Add your skills in data/skills.json")
        return
    cols = st.columns(2)
    for i, (group, items) in enumerate(skills.items()):
        with cols[i % 2].container(border=True):
            st.markdown(f"**{group}**")
            st.write(" ".join(f"`{s}`" for s in items))
