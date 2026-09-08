from flask import Flask, render_template, jsonify, request
import sudoku_logic

app = Flask(__name__)

# Keep a simple in-memory store for current puzzle and solution
CURRENT = {
    'puzzle': None,
    'solution': None
}

@app.route('/')
def index():
    return render_template('index.html')

DIFFICULTIES = {
    'easy': 42,
    'medium': 34,
    'hard': 28,
}

@app.route('/new')
def new_game():
    difficulty = request.args.get('difficulty', 'medium').lower()
    clues = DIFFICULTIES.get(difficulty, DIFFICULTIES['medium'])
    puzzle, solution = sudoku_logic.generate_puzzle(clues)
    CURRENT['puzzle'] = puzzle
    CURRENT['solution'] = solution
    return jsonify({'puzzle': puzzle, 'difficulty': difficulty, 'clues': clues})

@app.route('/check', methods=['POST'])
def check_solution():
    data = request.json
    board = data.get('board')
    solution = CURRENT.get('solution')
    if solution is None or not isinstance(board, list) or len(board) != sudoku_logic.SIZE:
        return jsonify({'error': 'No game in progress'}), 400
    incorrect = []
    for i in range(sudoku_logic.SIZE):
        for j in range(sudoku_logic.SIZE):
            if not isinstance(board[i], list) or len(board[i]) != sudoku_logic.SIZE:
                return jsonify({'error': 'Invalid board format'}), 400
            if board[i][j] != solution[i][j]:
                incorrect.append([i, j])
    return jsonify({'incorrect': incorrect})

@app.route('/hint', methods=['POST'])
def get_hint():
    data = request.json or {}
    board = data.get('board')
    solution = CURRENT.get('solution')
    if solution is None or not isinstance(board, list) or len(board) != sudoku_logic.SIZE:
        return jsonify({'error': 'No game in progress'}), 400
    for row in range(sudoku_logic.SIZE):
        if not isinstance(board[row], list) or len(board[row]) != sudoku_logic.SIZE:
            return jsonify({'error': 'Invalid board format'}), 400
    for row in range(sudoku_logic.SIZE):
        for col in range(sudoku_logic.SIZE):
            if board[row][col] != solution[row][col]:
                return jsonify({'row': row, 'col': col, 'value': solution[row][col]})
    return jsonify({'error': 'The puzzle is already complete'}), 400

if __name__ == '__main__':
    app.run(debug=True)