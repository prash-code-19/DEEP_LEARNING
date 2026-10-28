import streamlit as st
from yt_video_analyzer import build_yt_agent

import pandas as pd

st.set_page_config(
    page_title="Youtube video Analyzer",
    layout = "centered"

)


st.title("AI YT Video Analyzer")

@st.cache_resource
def get_agent():
    return build_yt_agent()

agent = get_agent()

# input box

video_url = st.text_input("Enter youtube video link")
button = st.button("analyze")

if video_url and button:
    with st.spinner("analyzing video..."):
        response = agent.run(
            f"Analyze this  video : {video_url}"

        )
    st.markdown("Analysis Report")
    st.markdown(response.content)