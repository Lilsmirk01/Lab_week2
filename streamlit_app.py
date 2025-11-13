import streamlit as st

st.title("🎈 TikTakToe")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.header("🎮 Tic Tac Toe (Multiplayer)")
st.write("Play with a friend — X vs O!")

# --- Initialize the game state ---
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
if "current_player" not in st.session_state:
    st.session_state.current_player = "X"
if "winner" not in st.session_state:
    st.session_state.winner = None

# --- Function to check the winner ---
def check_winner(board):
    win_patterns = [
        (0,1,2), (3,4,5), (6,7,8),  # Rows
        (0,3,6), (1,4,7), (2,5,8),  # Columns
        (0,4,8), (2,4,6)            # Diagonals
    ]
    for a,b,c in win_patterns:
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]
    if "" not in board:
        return "Draw"
    return None

# --- Function to make a move ---
def make_move(i):
    if st.session_state.board[i] == "" and st.session_state.winner is None:
        st.session_state.board[i] = st.session_state.current_player
        winner = check_winner(st.session_state.board)
        if winner:
            st.session_state.winner = winner
        else:
            st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"

# --- Create the Tic Tac Toe grid ---
cols = st.columns(3)
for i in range(9):
    if cols[i % 3].button(st.session_state.board[i] or " ", key=i):
        make_move(i)

# --- Display game status ---
if st.session_state.winner:
    if st.session_state.winner == "Draw":
        st.info("🤝 It's a draw!")
    else:
        st.success(f"🎉 Player {st.session_state.winner} wins!")
else:
    st.write(f"👉 It's **{st.session_state.current_player}**'s turn")

# --- Restart button ---
if st.button("🔄 Restart Game"):
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None