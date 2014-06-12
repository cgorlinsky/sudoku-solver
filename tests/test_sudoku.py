import pytest
import sudoku

# def test_create_sqr():
#     assert sudoku.squares == {'I1': [], 'D9': [], 'E4': [], 'E7': [], 'A3': [],
#                     'H3': [], 'B3': [], 'C3': [], 'D7': [], 'F4': [],
#                     'H4': [], 'H9': [], 'I3': [], 'A8': [], 'B9': [],
#                     'B4': [], 'F3': [], 'G2': [], 'B1': [], 'F2': [],
#                     'B5': [], 'B2': [], 'F7': [], 'D8': [], 'I8': [],
#                     'I6': [], 'C5': [], 'C2': [], 'G3': [], 'D4': [],
#                     'I4': [], 'B8': [], 'A1': [], 'G1': [], 'I7': [],
#                     'E6': [], 'E9': [], 'G7': [], 'C7': [], 'F6': [],
#                     'D6': [], 'G6': [], 'A7': [], 'H7': [], 'E1': [],
#                     'G4': [], 'A4': [], 'G9': [], 'E2': [], 'F9': [],
#                     'H6': [], 'C4': [], 'H5': [], 'F1': [], 'C6': [],
#                     'H2': [], 'D3': [], 'E5': [], 'E3': [], 'I2': [],
#                     'A6': [], 'H8': [], 'B6': [], 'A2': [], 'D2': [],
#                     'A9': [], 'G5': [], 'C1': [], 'I9': [], 'C8': [],
#                     'E8': [], 'G8': [], 'I5': [], 'A5': [], 'C9': [],
#                     'F8': [], 'H1': [], 'F5': [], 'D5': [], 'B7': [],
#                     'D1': []
#                     }

def test_squares():
    assert len(sudoku.square_keys) == 81
    assert len(sudoku.columns) == 9
    assert len(sudoku.rows) == 9
    assert len(sudoku.blocks)  == 9
    assert len(sudoku.squares) == 81
    assert sudoku.check_group['D5']== {'D3', 'E5', 'I5', 'D9', 'E4', 'D1',
                                       'D6', 'F4', 'B5', 'D2', 'F6', 'F5',
                                       'G5', 'H5', 'D8', 'A5', 'D7', 'E6',
                                       'D4', 'C5'}

def test_puzzle():
    assert len(sudoku.puzzle_values) == 81

def test_row_creation():
    assert sudoku.create_puzzle_row('7...3.....6....97....9...565....'
                                    '...3.4......72..61....3.1..4....'
                                    '.....56...7.2....'
    ) == (
        '7 . . | . 3 . | . . . '
    )
    assert sudoku.create_horizontal_ln() == '- - - + - - - + - - - \n'

def test_block_creation():
    assert sudoku.create_block_row('7...3.....6....97....9...565....'
                                    '...3.4......72..61....3.1..4....'
                                    '.....56...7.2....'
    ) == ('7 . . | . 3 . | . . . \n'
        + '. 6 . | . . . | 9 7 . \n'
        + '. . . | 9 . . | . 5 6 \n'
    )

def test_create_grid():
    assert sudoku.create_grid(
        '7...3.....6....97....9...565.......3.4...'
        '...72..61....3.1..4.........56...7.2....'
    ) == (
        '7 . . | . 3 . | . . . \n'
        '. 6 . | . . . | 9 7 . \n'
        '. . . | 9 . . | . 5 6 \n'
        '- - - + - - - + - - - \n'
        '5 . . | . . . | . . 3 \n'
        '. 4 . | . . . | . . 7 \n'
        '2 . . | 6 1 . | . . . \n'
        '- - - + - - - + - - - \n'
        '3 . 1 | . . 4 | . . . \n'
        '. . . | . . . | 5 6 . \n'
        '. . 7 | . 2 . | . . . \n'
    )

def test_check_row():


# def test_check_col():

# def test_check_block():
