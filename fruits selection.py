import streamlit as st

st.title("Choose a Fruit")

fruit = st.selectbox("Select one:", ["Apple", "Banana", "Mango"])

st.write(f"You selected: {fruit}")
