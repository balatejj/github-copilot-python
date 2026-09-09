# Gridline Sudoku

Gridline Sudoku is a lightweight Python Flask and browser-based Sudoku game built as a GitHub Copilot project. The app generates playable puzzles, validates moves, supports difficulty settings, offers hints, and tracks puzzle state in the browser.

## Repository structure

```text
github-copilot-python/
├── .github/
│   └── instruction.md
├── Prompts/
│   └── prompts.json
├── README.md
├── Screenshots/
├── starter/
│   ├── app.py
│   ├── requirements.txt
│   ├── pytest.ini
│   ├── sudoku_logic.py
│   ├── static/
│   │   ├── main.js
│   │   └── styles.css
│   ├── templates/
│   │   └── index.html
│   └── tests/
│       ├── test_app_routes.py
│       └── test_sudoku_logic.py
└── .gitignore
```

## Implemented features

- Flask routes for puzzle creation, checking, and hint generation
- Difficulty levels: easy, medium, and hard
- Puzzle generation using a Sudoku solver and uniqueness check logic
- Board shape validation and request validation in the Flask API
- A browser UI with a clue cell model, empty-cell input, and local game feedback
- Optional dark styling and responsive UI behavior in the static CSS and JavaScript files

## Main files

- [starter/app.py](starter/app.py): Flask application and HTTP endpoints
- [starter/sudoku_logic.py](starter/sudoku_logic.py): puzzle generator, solver helpers, and uniqueness checks
- [starter/templates/index.html](starter/templates/index.html): HTML UI shell
- [starter/static/main.js](starter/static/main.js): client-side interaction and UI behavior
- [starter/static/styles.css](starter/static/styles.css): styling and dark-theme layout rules
- [starter/tests/test_app_routes.py](starter/tests/test_app_routes.py): endpoint and request validation tests
- [starter/tests/test_sudoku_logic.py](starter/tests/test_sudoku_logic.py): Sudoku generation and logic tests
- [.github/instruction.md](.github/instruction.md): project instructions for this repository

## Requirements

- Python 3.9+
- Flask 2+
- Pytest 8+
- Modern web browser

## Run locally

1. Open a terminal in the repository root and move into the app folder.

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

4. Run the tests.

```bash
python -m pytest -q
```

5. Start the Flask app.

```bash
python app.py
```

6. Open the app in a browser.

```text
http://127.0.0.1:5000/
```

## Notes

- The request handler and game routes stay in the [starter/app.py](starter/app.py) file.
- Puzzle generation and Sudoku validation logic remain separate in [starter/sudoku_logic.py](starter/sudoku_logic.py).
- The project is intentionally small and organized around a single Flask starter app rather than a larger package structure.
