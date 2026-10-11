import streamlit as st

from utils.loader import ASSETS_DIR


def render(profile):
    with st.sidebar:
        photo = ASSETS_DIR / profile.get("photo", "photo.jpg")
        if photo.exists():
            st.image(str(photo), use_container_width=True)
        st.header(profile.get("name", ""))
        st.caption(profile.get("title", ""))
        if profile.get("location"):
            st.write(f"📍 {profile['location']}")
        if profile.get("email"):
            st.write(f"✉️ {profile['email']}")
        for label, url in profile.get("links", {}).items():
            st.link_button(label, url, use_container_width=True)

        resume = ASSETS_DIR / profile.get("resume_file", "resume.pdf")
        if resume.exists():
            st.download_button(
                "⬇️ Download Resume (PDF)",
                resume.read_bytes(),
                file_name=resume.name,
                mime="application/pdf",
                use_container_width=True,
            )
