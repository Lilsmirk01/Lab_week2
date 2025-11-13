import streamlit as st
import random

st.title("🎈 My newasdasdawkhsgkdsd app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.header("🎯 Number Guessing Game")

# Generate a random number and store it in session state so it doesn't reset on each rerun
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 20)

guess = st.number_input("Guess a number between 1 and 20", min_value=1, max_value=20, step=1)
if st.button("Submit Guess"):
    if guess == st.session_state.number:
        st.success("🎉 Correct! You guessed the number!")
        st.session_state.number = random.randint(1, 20)  # reset game
    elif guess < st.session_state.number:
        st.warning("Too low! Try again.")
    else:
        st.warning("Too high! Try again.")

if st.button("Reset Game"):
    st.session_state.number = random.randint(1, 20)
    st.info("🔄 Game reset! Guess the new number.")