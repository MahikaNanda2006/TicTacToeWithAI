from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)
#Step 1: We want to make a grid
board = [" "]*9

#2. We write a code to print it
def print_board():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i<6:
            print ("---------")

#3. Defining win states
win_states = [(0,1,2), (0,4,8), (0,3,6) ,(1,4,7), (2,4,6),(2,5,8), (3,4,5), (6,7,8)]

def check_winner(player):
    for states in win_states:
        if board[states[0]]==board[states[1]]==board[states[2]]==player:
            return True
    return False

def user_input():
    x = int(input("Enter the box you would like to move to"))
    if board[x] == " ":
        board[x] = "X"
    else:
        print("Spot taken, try again!")
        user_input()

def evaluate():
    if check_winner("O"):
        return 1
    elif check_winner("X"):
        return -1
    else:
        return 0

def minMax (is_maximising):
    # Here, we use minMax
    # This method is recursive
    # To write recursive methods, first figure out the base case
    #1. Base Case

    if check_winner("O"):
        return 1
    elif check_winner("X"):
        return -1
    elif " " not in board:
        return 0
    
    #2. Now, we have to write the recursive case
    # For the AI's turn, we want to take the maximum case
    # For the user's, we want the minimum
    #2.1 We start with the AI's turn

    if is_maximising:
        # We defind best_score and give it the lowest possible value
        best_score = -float('inf')
        for i in range (9):
            if board[i] == " ":
                board[i] = "O"
                # Call again for User's simulation
                result = minMax(False)
                # We have to also manually backtrack here
                board[i] = " "
                # Finally, update the maximum value
                best_score = max(best_score, result)
        return best_score
    # Now, same for the user
    else:
        #Here, it is the user's move
        worst_score = float ('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                # Call again for AI simulation
                result = minMax(True)
                # Backtrack
                board[i] = " "
                # Update score
                worst_score = min(worst_score, result)
        return worst_score

def AI_move():
    best_score = -float('inf')
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            result = minMax(False)
            board[i] = " "
            if result>best_score:
                best_score = result
                move = i
    board[move] = "O"

            
@app.route("/move", methods=["POST"])
def move():
    data = request.json
    user_pos = data["position"]
    
    if board[user_pos] != " ":
        return jsonify({"error": "Spot taken"}), 400
    
    board[user_pos] = "X"
    
    # Check if user won
    if check_winner("X"):
        result = {"board": board.copy(), "winner": "X"}
        return jsonify(result)
    
    if " " not in board:
        winner = "Draw"
    # AI makes a move
    AI_move()
    if check_winner("O"):
        winner = "O"

    
    result = {"board": board.copy(), "winner": winner}
    
    # Only reset after sending the board to client
    if winner:
        reset_board()
    
    return jsonify(result)

@app.route("/")
def home():
    return render_template("index.html")

def reset_board():
    global board
    board = [" "]*9



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
