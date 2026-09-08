# Copilot Instruction File

## Project goal
Build and improve a responsive Sudoku web app in Python Flask with a modern, accessible interface.

## Coding expectations
- Keep the backend small and clear: Flask routes should handle game state and validation cleanly.
- Prefer simple, readable functions over over-engineering.
- Keep game logic in a dedicated module, such as sudoku_logic.py.
- Preserve a single-solution Sudoku generator and validate puzzle difficulty.
- Use locked prefilled cells for puzzle state.
- Provide error handling for invalid board payloads and missing game state.
- Favor accessible HTML and CSS, including readable text and visible controls in both light and dark modes.
- Use responsive layout rules so the grid remains stable on mobile and desktop.
- Add comments where logic is non-trivial, especially for generation, validation, and scoring.
- When suggesting code, prefer solutions that are robust, testable, and easier to maintain.

## Game requirements
- Support easy, medium, and hard difficulty.
- Generate puzzles with exactly one unique solution.
- Lock prefilled clues.
- Highlight invalid entries clearly.
- Add a hint button that fills one valid empty cell.
- Add a check button that reports incorrect cells.
- Track elapsed time and save the top 10 scores in localStorage.
- Keep the board visually consistent, with 3x3 subgrids color-coded without layout shifts.
- Include a dark mode toggle and ensure all labels and controls remain readable.

## Copilot usage guidelines
- Produce concise, production-ready code and avoid unnecessary files.
- Before accepting changes, review whether the solution matches the project requirements.
- If a suggestion introduces a bug, insecure behavior, or poor accessibility, reject it and explain why.
- Prefer explicit, maintainable code over clever-but-opaque shortcuts.
- Keep comments useful and brief.
- Preserve existing app structure when making edits.
