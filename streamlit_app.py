import streamlit as st
import random

st.title("🎈 app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# ==============================
# 🐍 Simple Snake Game
# ==============================

st.header("🐍 Snake Game")
st.write("Use the arrow buttons to move and eat the apple!")

GRID_SIZE = 10

# --- Initialize game state ---
if "snake" not in st.session_state:
    st.session_state.snake = [(5, 5)]
if "food" not in st.session_state:
    st.session_state.food = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
if "direction" not in st.session_state:
    st.session_state.direction = "RIGHT"
if "game_over" not in st.session_state:
    st.session_state.game_over = False

# --- Movement controls ---
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("⬆️ Up"):
        st.session_state.direction = "UP"
with col2:
    if st.button("⬅️ Left"):
        st.session_state.direction = "LEFT"
    if st.button("➡️ Right"):
        st.session_state.direction = "RIGHT"
with col3:
    if st.button("⬇️ Down"):
        st.session_state.direction = "DOWN"

# --- Game logic ---
if not st.session_state.game_over:
    head_x, head_y = st.session_state.snake[0]

    if st.session_state.direction == "UP":
        head_y -= 1
    elif st.session_state.direction == "DOWN":
        head_y += 1
    elif st.session_state.direction == "LEFT":
        head_x -= 1
    elif st.session_state.direction == "RIGHT":
        head_x += 1

    new_head = (head_x, head_y)

    # Check collisions
    if (
        head_x < 0 or head_x >= GRID_SIZE or
        head_y < 0 or head_y >= GRID_SIZE or
        new_head in st.session_state.snake
    ):
        st.session_state.game_over = True
    else:
        st.session_state.snake.insert(0, new_head)
        if new_head == st.session_state.food:
            st.session_state.food = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
        else:
            st.session_state.snake.pop()

# --- Draw grid ---
def draw_grid():
    grid = ""
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            if (x, y) == st.session_state.food:
                grid += "🍎 "
            elif (x, y) in st.session_state.snake:
                if (x, y) == st.session_state.snake[0]:
                    grid += "🟩 "  # Snake head
                else:
                    grid += "🟢 "  # Snake body
            else:
                grid += "⬜ "
        grid += "\n"
    return grid

st.text(draw_grid())

# --- Display status ---
if st.session_state.game_over:
    st.error("💀 Game Over! You hit the wall or yourself!")

if st.button("🔄 Restart Game"):
    st.session_state.snake = [(5, 5)]
    st.session_state.food = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
    st.session_state.direction = "RIGHT"
    st.session_state.game_over = False
