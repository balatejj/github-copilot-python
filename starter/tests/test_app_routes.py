import pytest

from app import app, CURRENT, sudoku_logic


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_check_rejects_non_object_json_instead_of_crashing(client):
    response = client.post('/check', data='null', content_type='application/json')

    assert response.status_code == 400
    assert response.get_json()['error'] == 'Expected a JSON object'


def test_hint_rejects_array_json_instead_of_crashing(client):
    response = client.post('/hint', data='[]', content_type='application/json')

    assert response.status_code == 400
    assert response.get_json()['error'] == 'Expected a JSON object'


def test_hint_returns_value_for_selected_coordinates(client):
    puzzle, solution = sudoku_logic.generate_puzzle(clues=35)
    CURRENT['solution'] = solution
    CURRENT['puzzle'] = puzzle

    empty_row, empty_col = next(
        (row, col)
        for row, line in enumerate(puzzle)
        for col, value in enumerate(line)
        if value == sudoku_logic.EMPTY
    )
    response = client.post('/hint', json={'board': puzzle, 'row': empty_row, 'col': empty_col})

    assert response.status_code == 200
    assert response.get_json() == {'row': empty_row, 'col': empty_col, 'value': solution[empty_row][empty_col]}
