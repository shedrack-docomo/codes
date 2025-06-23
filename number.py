# app.py
import streamlit as st

st.title("Even or Odd Number Checker")

# Prompt the user for a number
number = st.number_input("Enter an integer:", value=0, step=1, format="%d")

# Button to trigger check
if st.button("Check"):
    if number % 2 == 0:
        st.success(f"{number} is even 🎉")
    else:
        st.info(f"{number} is odd 😊")
