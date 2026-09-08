# Gridline Sudoku

This project is a small Flask-based Sudoku game that generates playable puzzles, validates the board, reveals hints, tracks time, and stores local leaderboard scores in the browser.

## Project structure

```text
github-copilot-python/
├── README.md
├── CODEOWNERS
├── starter/
│   ├── app.py
│   ├── requirements.txt
│   ├── sudoku_logic.py
│   ├── static/
│   │   ├── main.js
│   │   └── styles.css
│   └── templates/
│       └── index.html
└── .gitignore
```

## What is in the app

- `starter/app.py`: Flask routes and game state management
- `starter/sudoku_logic.py`: Sudoku generation and validation logic
- `starter/templates/index.html`: page shell for the React-powered UI
- `starter/static/main.js`: game logic, timer, difficulty controls, hints, and leaderboard
- `starter/static/styles.css`: layout and styling for the Sudoku board and interface

## Features

- Easy, medium, and hard puzzle generation
- Live validation of player inputs
- Hint system that fills a correct cell
- Timer for each round
- Puzzle completion flow with score saving in browser storage
- Responsive single-page UI built with React

## Prerequisites

- Python 3.9+
- A modern web browser

## Run locally

1. Open a terminal and go to the project folder.

```bash
cd github-copilot-python/starter
```

2. Create and activate a virtual environment.

On macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install the dependencies.

```bash
pip install -r requirements.txt
```

4. Start the Flask app.

```bash
python app.py
```

5. Open the app in a browser:

```text
http://127.0.0.1:5000/
```

## Notes

- The game is served from the `starter` directory, not the repository root.
- Top 10 scores are stored in `localStorage` on the client side.
- The project is structured as a lightweight learning/demo app and does not currently include a separate license file.
