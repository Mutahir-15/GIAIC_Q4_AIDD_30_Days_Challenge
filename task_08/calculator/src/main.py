import streamlit as st
from calculator import calculate

st.title("Simple Calculator")

expression = st.text_input("Enter a mathematical expression:")

if expression:
    try:
        result = calculate(expression)
        st.success(f"Result: {result}")
    except ValueError as e:
        st.error(str(e))
