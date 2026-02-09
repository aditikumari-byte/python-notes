import streamlit as st

st.title("🧮 Web Calculator")

a = st.number_input("Enter first number", value=0.0)
b = st.number_input("Enter second number", value=0.0)

operation = st.selectbox(
    "Choose operation",
    ("Add", "Subtract", "Multiply", "Divide")
)

if st.button("Calculate"):
    if operation == "Add":
        st.success(f"Result: {a + b}")
    elif operation == "Subtract":
        st.success(f"Result: {a - b}")
    elif operation == "Multiply":
        st.success(f"Result: {a * b}")
    elif operation == "Divide":
        if b != 0:
            st.success(f"Result: {a / b}")
        else:
            st.error("Cannot divide by zero")