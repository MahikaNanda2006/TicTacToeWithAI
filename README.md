Tic-Tac-Toe AI Web App

A simple Tic-Tac-Toe game where you can play against an AI that uses the Minimax algorithm. Built with Python (Flask) for the backend and HTML/CSS/JavaScript for the frontend.

Features

Play as X against an unbeatable AI (O).

AI uses the Minimax algorithm to make optimal moves.

Responsive grid layout with a soft, pastel pink theme.

Game highlights the winner or draw before restarting.

Simple and lightweight, runs in any modern browser.

Technologies Used

Backend: Python 3, Flask

Frontend: HTML, CSS, JavaScript (fetch API)

Algorithm: Minimax (recursive AI decision-making)

How to Run

Clone the repository or download the project files.

Install Flask (if not already installed):

pip install flask


Run the Flask app:

python app.py


Open your browser and go to:

http://127.0.0.1:5000/


Click on a cell to make your move. The AI will respond automatically.

Folder Structure
/tic-tac-toe-ai
│
├── app.py             # Flask backend and game logic
├── templates/
│   └── index.html     # Frontend HTML page
└── static/
    └── styles.css     # Optional external CSS file

How It Works

The board state is stored in a global Python list.

When the user makes a move, the backend checks for a win/draw.

The AI then calculates its move using Minimax and updates the board.

The frontend fetches updates from the backend and updates the grid.

If the game ends, the board shows the final state for 3 seconds before resetting.

Customization

Change the theme: Modify the CSS in index.html to adjust colors or styles.

AI symbol: By default, AI plays O. You can switch symbols in app.py.

Grid size: Currently a 3x3 board; adapting to larger boards requires modifying the win states and Minimax logic.

License

This project is free to use and modify for personal or educational purposes.