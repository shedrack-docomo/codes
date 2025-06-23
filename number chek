import streamlit as st

st.title("Even or Odd Checker")

num = st.number_input("Enter an integer", step=1, format="%d")

if st.button("Check"):
    if int(num) % 2 == 0:
        st.success("Even Number")
    else:
        st.warning("Odd Number")
