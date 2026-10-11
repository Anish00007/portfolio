import streamlit as st


def render(achievements, volunteer):
    if achievements:
        st.markdown("### 🏅 Achievements & Leadership")
        for a in achievements:
            st.markdown(f"- {a}")
    if volunteer:
        st.markdown("### 🤝 Volunteering")
        for v in volunteer:
            with st.container(border=True):
                st.markdown(f"**{v['org']}**")
                st.caption(f"🗓 {v['period']}")
                for p in v.get("points", []):
                    st.markdown(f"- {p}")
