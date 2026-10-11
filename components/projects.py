import streamlit as st


def render(projects):
    if not projects:
        st.info("Add your projects in data/projects.json")
        return
    cols = st.columns(2)
    for i, p in enumerate(projects):
        with cols[i % 2].container(border=True):
            st.markdown(f"### {p['title']}")
            if p.get("category"):
                st.caption(p["category"])
            st.write(p.get("description", ""))
            st.write(" ".join(f"`{t}`" for t in p.get("tools", [])))
            if p.get("link"):
                st.link_button("View project", p["link"])
