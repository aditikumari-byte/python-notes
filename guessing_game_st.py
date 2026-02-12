import streamlit as st
import random

st.title("🎯 Number Guessing Game")

# Initialize session state
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.guesses = 0

st.write("I'm thinking of a number between 1 and 100!")

user_guess = st.number_input("Take a guess:", min_value=1, max_value=100, step=1)

if st.button("Submit Guess"):
    st.session_state.guesses += 1

    if user_guess == st.session_state.secret_number:
        st.success(f"🎉 Correct! The number was {st.session_state.secret_number}")
        st.write(f"You took {st.session_state.guesses} guesses.")

    elif user_guess < st.session_state.secret_number:
        st.warning("Too low!")

    else:
        st.warning("Too high!")

if st.button("Play Again"):
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.guesses = 0
    st.success("New game started!")