# Gridline Sudoku

Gridline Sudoku is a lightweight Python Flask and browser-based Sudoku game built as a GitHub Copilot project. The app generates playable puzzles, validates moves, supports difficulty levels, offers hints, tracks time, and stores local leaderboard scores in the browser.

## Repository structure

```text
github-copilot-python/
├── .github/
│   └── instruction.md
├── Prompts/
│   └── prompts.json
├── README.md
├── Screenshots/
│   ├── Dark theme.png
│   ├── VENV&requirements.png
│   └── ...
├── .gitignore
├── starter/
│   ├── app.py
│   ├── requirements.txt
│   ├── sudoku_logic.py
│   ├── static/
│   │   ├── main.js
│   │   └── styles.css
│   ├── templates/
│   │   └── index.html
│   └── venv/
```

## Features

- Flask backend with Sudoku generation and validation logic
- Easy, Medium, and Hard difficulty settings
- Locked clue cells and invalid move detection
- Hint and check actions for puzzle progress
- Timer and round-based gameplay
- Local leaderboard saving the top scores in the browser
- Responsive layout with a dark mode theme
- Copilot workflow artifacts stored in the repo for project documentation and rubric evidence

## Main project files

- [starter/app.py](starter/app.py): Flask routes for puzzle generation, validation, hints, and board state
- [starter/sudoku_logic.py](starter/sudoku_logic.py): Sudoku generation, uniqueness checks, validation, and puzzle logic
- [starter/templates/index.html](starter/templates/index.html): UI shell for the game
- [starter/static/main.js](starter/static/main.js): client-side game logic, timer, leaderboard, and interaction handling
- [starter/static/styles.css](starter/static/styles.css): board styling, layout, and dark mode theme
- [.github/instruction.md](.github/instruction.md): project-specific Copilot guidance
- [Prompts/prompts.json](Prompts/prompts.json): prompt examples used as project workflow evidence
- [Screenshots](Screenshots): screenshot evidence for the project and rubric documentation

## Requirements

- Python 3.9+
- Flask
- Modern web browser

## Run locally

1. Open a terminal and go to the app folder.

```bash
cd github-copilot-python/starter
```

2. Create and activate a virtual environment.

On macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

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

5. Open the app in a browser.

```text
http://127.0.0.1:5000/
```

## Notes

- The application runs from the [starter](starter) directory rather than the repository root.
- Score data is stored in the browser using localStorage.
- The project is intentionally kept compact and focused on the Sudoku gameplay and the GitHub Copilot workflow evidence required for the project rubric.
