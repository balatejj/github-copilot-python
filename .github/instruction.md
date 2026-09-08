# Copilot Instruction File

## Project objective
Build and maintain a lightweight Sudoku web application using Python Flask and a browser-based interface. The project should stay small, readable, and aligned with the current repository structure.

## Repository expectations
- Keep the main application code inside the [starter](../starter) folder.
- Keep project-level evidence and workflow files in the repo root, such as [README.md](../README.md), [Prompts](../Prompts), and [Screenshots](../Screenshots).
- Avoid adding unnecessary files or duplicate app logic outside the established structure.
- Preserve a clear separation between backend logic, frontend behavior, and styling.

## Coding standards
- Prefer simple, readable, maintainable code over over-engineered solutions.
- Keep Flask routes focused on game state, validation, and puzzle actions.
- Keep the Sudoku generation and validation rules in a dedicated logic module such as [starter/sudoku_logic.py](../starter/sudoku_logic.py).
- Validate puzzle generation to ensure a unique solution and consistent difficulty behavior.
- Lock prefilled clue cells and prevent invalid overwrites of original values.
- Handle missing or malformed board data gracefully.
- Use accessible UI patterns, readable text, and visible controls in both light and dark themes.
- Keep the layout responsive and stable on desktop and mobile screens.
- Add brief comments only where logic is not obvious.

## Game requirements
- Support Easy, Medium, and Hard difficulty levels.
- Generate valid Sudoku puzzles with a single unique solution.
- Let users fill empty cells, check progress, and request hints.
- Highlight incorrect entries or invalid board states clearly.
- Track game time and persist the top scores in the browser using localStorage.
- Maintain clean 3x3 subgrid organization without visual shifts or broken spacing.
- Include a dark mode theme and ensure all labels, buttons, and cell values remain readable.

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
