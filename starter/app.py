from flask import Flask, render_template, jsonify, request
import sudoku_logic

app = Flask(__name__)

# Keep a simple in-memory store for current puzzle and solution
CURRENT = {
    'puzzle': None,
    'solution': None
}


def get_request_object():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return None, jsonify({'error': 'Expected a JSON object'}), 400
    return data, None, None


def validate_board_shape(board):
    if not isinstance(board, list) or len(board) != sudoku_logic.SIZE:
        return False
    for row in board:
        if not isinstance(row, list) or len(row) != sudoku_logic.SIZE:
            return False
    return True


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
    data, error_response, status = get_request_object()
    if error_response:
        return error_response, status

    board = data.get('board')
    if not validate_board_shape(board):
        return jsonify({'error': 'Invalid board format'}), 400

    solution = CURRENT.get('solution')
    if solution is None:
        return jsonify({'error': 'No game in progress'}), 400

    incorrect = []
    for i in range(sudoku_logic.SIZE):
        for j in range(sudoku_logic.SIZE):
            if board[i][j] != solution[i][j]:
                incorrect.append([i, j])
    return jsonify({'incorrect': incorrect})

@app.route('/hint', methods=['POST'])
def get_hint():
    data, error_response, status = get_request_object()
    if error_response:
        return error_response, status

    board = data.get('board')
    if not validate_board_shape(board):
        return jsonify({'error': 'Invalid board format'}), 400

    row = data.get('row')
    col = data.get('col')
    if not isinstance(row, int) or not isinstance(col, int):
        return jsonify({'error': 'Expected row and col coordinates'}), 400
    if row < 0 or row >= sudoku_logic.SIZE or col < 0 or col >= sudoku_logic.SIZE:
        return jsonify({'error': 'Coordinates are out of bounds'}), 400

    solution = CURRENT.get('solution')
    if solution is None:
        return jsonify({'error': 'No game in progress'}), 400

    if board[row][col] != sudoku_logic.EMPTY:
        return jsonify({'error': 'Selected cell is already filled'}), 400

    return jsonify({'row': row, 'col': col, 'value': solution[row][col]})

if __name__ == '__main__':
    app.run(debug=True)