import streamlit as st
import pandas as pd
import numpy as np

st.title("Charts Example")

data = pd.DataFrame(
    np.random.rand(10, 2),
    columns=["Sales", "Profit"]
)

st.bar_chart(data)
st.area_chart(data)
