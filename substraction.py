import streamlit as st

st.title("➖ Subtract Two Numbers (Always bigger - smaller)")

a = st.number_input("Enter first number:")
b = st.number_input("Enter second number:")

if st.button("Subtract"):
    result = abs(a - b)
    st.success(f"Result: {result}")
