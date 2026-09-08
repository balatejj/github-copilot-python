# Gridline Sudoku

Gridline Sudoku is a responsive Flask and React-based Sudoku game created as a GitHub Copilot project. The app generates playable puzzles, validates moves, tracks elapsed time, offers hints and difficulty levels, and saves the top 10 scores locally in the browser.

## Repository structure

```text
github-copilot-python/
├── .github/
│   └── instruction.md
├── Prompts/
│   └── prompts.json
├── Screenshots/
│   ├── app_dark_mode.png
│   ├── app_light_mode.png
│   ├── copilot_grid_style_prompt.png
│   ├── copilot_rejection_prompt.png
│   ├── copilot_setup_testing_prompt.png
│   ├── copilot_top10_score_prompt.png
│   └── copilot_unique_solution_prompt.png
├── README.md
├── .gitignore
├── starter/
│   ├── app.py
│   ├── requirements.txt
│   ├── sudoku_logic.py
│   ├── static/
│   │   ├── main.js
│   │   └── styles.css
│   └── templates/
│       └── index.html
└── venv/
```

## Project highlights

- Flask backend with Sudoku generation and validation logic
- Difficulty modes: Easy, Medium, Hard
- Locked clue cells and invalid-move feedback
- Hint and check puzzle actions
- Timer for each round
- Local leaderboard keeping the top 10 scores
- Dark mode toggle and responsive design
- Project rubric evidence stored in the prompt and screenshot folders

## App files

- starter/app.py: Flask routes for puzzle generation, checking, hints, and game state
- starter/sudoku_logic.py: board creation, uniqueness checks, puzzle generation, and validation logic
- starter/templates/index.html: HTML shell for the game UI
- starter/static/main.js: React-based UI, timer, difficulty logic, hints, leaderboard, and game flow
- starter/static/styles.css: layout, board styling, responsive behavior, and dark mode theme

## Copilot workflow artifacts

This repository includes the required Copilot process evidence:

- .github/instruction.md: project-specific instruction file for Copilot
- Prompts/prompts.json: rubric-aligned prompt examples used during development
- Screenshots/: labeled images showing Copilot prompts, responses, and app states that support the project rubric

## Requirements

- Python 3.9+
- Flask
- Modern browser

## Run locally

1. Open a terminal and navigate to the project folder.

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

3. Install dependencies.

```bash
pip install -r requirements.txt
```

4. Run the app.

```bash
python app.py
```

5. Open the app in a browser.

```text
http://127.0.0.1:5000/
```

## Notes

- The app is served from the starter folder rather than the repository root.
- Score data is stored in browser localStorage.
- The project is intentionally kept lightweight and focused on the Sudoku gameplay and the Copilot workflow evidence required by the rubric.
