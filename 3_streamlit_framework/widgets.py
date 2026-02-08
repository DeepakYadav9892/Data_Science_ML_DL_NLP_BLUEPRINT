import streamlit as st 
st.title("Streamlit text input")

st.title("Streamlit Text Input")

name=st.text_input("Enter your name:")

age=st.slider("Select your age:",0,100,25)
st.write(f"Your age is {age}.")

options=["Python","java","C++","JavaScript"]
choice=st.selectbox("choose your favorite language:",options)
st.write(f"you selected {choice}.")

if name:
    st.write(f"hello,{name}")