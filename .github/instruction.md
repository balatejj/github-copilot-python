# Copilot Instruction File

## Project objective
Build and maintain a lightweight Sudoku web application using Python Flask and a browser-based interface. The implemented workspace follows a small Flask starter layout with the application code in the [starter](../starter) folder and test files under the same folder.

## Repository expectations
- Keep the main application code inside the [starter](../starter) folder.
- Keep the app-level dependency file in the same folder, including [starter/requirements.txt](../starter/requirements.txt).
- Keep project-level evidence and workflow files in the repository root, such as [README.md](../README.md), [Prompts](../Prompts), and [Screenshots](../Screenshots).
- Avoid adding unnecessary files or duplicating app logic outside the established structure.
- Preserve a clear separation between backend logic, frontend behavior, and styling.

## Code organization
- Keep Flask routes in [starter/app.py](../starter/app.py) for puzzle creation, validation, hints, and board-state checks.
- Keep Sudoku generation and validation rules in the dedicated logic module [starter/sudoku_logic.py](../starter/sudoku_logic.py).
- Keep HTML, CSS, and JavaScript assets in [starter/templates/index.html](../starter/templates/index.html), [starter/static/styles.css](../starter/static/styles.css), and [starter/static/main.js](../starter/static/main.js).
- Keep automated tests in [starter/tests/test_app_routes.py](../starter/tests/test_app_routes.py) and [starter/tests/test_sudoku_logic.py](../starter/tests/test_sudoku_logic.py).
- Keep dependency and pytest configuration in the same project root as the Flask app: [starter/requirements.txt](../starter/requirements.txt) and [starter/pytest.ini](../starter/pytest.ini).

## Coding standards
- Prefer simple, readable, maintainable code over over-engineered solutions.
- Keep Flask routes focused on game state, validation, and puzzle actions.
- Validate puzzle generation to ensure a unique solution and consistent difficulty behavior.
- Lock prefilled clue cells and prevent invalid overwrites of original values.
- Handle missing or malformed board data gracefully.
- Use accessible UI patterns, readable text, and visible controls in both light and dark themes.
- Keep the layout responsive and stable on desktop and mobile screens.
- Add brief comments only where logic is not obvious.

## Game requirements
- Support Easy, Medium, and Hard difficulty levels.
- Generate valid Sudoku puzzles with a unique solution and a consistent clue count per requested level.
- Let users fill empty cells, check progress, and request hints.
- Highlight incorrect entries or invalid board states clearly.
- Track game time and persist top scores in the browser using localStorage.
- Maintain clean 3x3 subgrid organization without visual shifts or broken spacing.
- Include a dark mode theme and ensure all labels, buttons, and cell values remain readable.

## Testing expectations
- Run tests from the [starter](../starter) directory using the repository test configuration in [starter/pytest.ini](../starter/pytest.ini).
- Use the command `python -m pytest -q` to verify the Flask routes and Sudoku logic remain consistent.
- Update tests when changing API response shapes, puzzle generation defaults, or route behavior.

## UI and design expectations
- Keep the interface polished but minimal.
- Ensure controls have strong contrast and consistent spacing.
- Fix readability issues in dark mode before finalizing styling updates.
- Maintain a clean board layout with obvious selection, clue, and error states.

## Copilot usage guidelines
- Produce concise, production-ready code and avoid unnecessary complexity.
- Check whether suggested changes match the project structure and existing design patterns.
- Reject changes that introduce accessibility issues, broken game logic, or unnecessary file clutter.
- Prefer explicit, robust implementations over clever shortcuts.
- Keep comments helpful and brief.
- Preserve the existing app architecture unless a documented change requires restructuring.
