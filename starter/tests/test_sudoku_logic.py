import sudoku_logic


def test_create_empty_board_has_correct_grid_shape():
    board = sudoku_logic.create_empty_board()

    assert len(board) == sudoku_logic.SIZE
    assert all(len(row) == sudoku_logic.SIZE for row in board)
    assert all(cell == sudoku_logic.EMPTY for row in board for cell in row)


def test_is_safe_detects_conflicts_in_row_and_box():
    board = sudoku_logic.create_empty_board()
    board[0][0] = 1
    board[0][1] = 2

    # Candidate 1 is already present in the same row.
    assert sudoku_logic.is_safe(board, 0, 2, 1) is False

    board = sudoku_logic.create_empty_board()
    board[0][0] = 1
    board[0][1] = 2
    board[0][2] = 3
    board[1][0] = 4
    board[1][1] = 5
    board[1][2] = 6
    board[2][0] = 7
    board[2][1] = 8

    # Candidate 1 appears inside the same 3x3 box and should be rejected.
    assert sudoku_logic.is_safe(board, 2, 2, 1) is False


def test_generate_puzzle_returns_a_9_by_9_puzzle_and_solution():
    puzzle, solution = sudoku_logic.generate_puzzle(clues=35)

    assert len(puzzle) == sudoku_logic.SIZE
    assert len(solution) == sudoku_logic.SIZE
    assert all(len(row) == sudoku_logic.SIZE for row in puzzle)
    assert all(len(row) == sudoku_logic.SIZE for row in solution)

    assert all(cell in range(1, sudoku_logic.SIZE + 1) for row in solution for cell in row)
    assert sum(cell != sudoku_logic.EMPTY for row in puzzle for cell in row) >= 17
