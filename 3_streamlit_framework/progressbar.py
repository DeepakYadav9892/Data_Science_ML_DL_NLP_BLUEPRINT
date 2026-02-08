import streamlit as st
import time

st.title("Loading Example")

with st.spinner("Processing..."):
    time.sleep(3)

st.success("Done!")

progress = st.progress(0)

for i in range(100):
    time.sleep(0.05)
    progress.progress(i + 1)
