import streamlit as st


def render(jobs):
    if not jobs:
        st.info("Add your experience in data/experience.json")
        return

    for job in jobs:
        with st.container(border=True):
            left, right = st.columns([3, 1])
            left.markdown(f"### {job['role']}")
            meta = [f"**{job['company']}**"]
            for key in ("location", "type"):
                if job.get(key):
                    meta.append(job[key])
            left.markdown(" · ".join(meta))
            right.caption(f"🗓 {job['period']}")

            if job.get("summary"):
                st.write(job["summary"])

            if job.get("points"):
                st.markdown("**Key achievements**")
                for point in job["points"]:
                    st.markdown(f"- {point}")

            if job.get("tools"):
                st.markdown("**Tools:** " + " ".join(f"`{t}`" for t in job["tools"]))
