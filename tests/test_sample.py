import pytest
from src.sample import Board


@pytest.mark.parametrize("test_input, expected", [
    (
        [(0, 0), (1, 1), (2, 1), (2, 0)],
        0
    ),
    (
        [(0, 0), (0, 1), (0, 2)],
        1
    ),
    (
        [(0, 0), (1, 0), (2, 0)],
        1
    ),
    (
        [(0, 0), (1, 0), (2, 0)],
        1
    ),
    (
        [(0, 0), (1, 0), (2, 0), (1, 1), (2, 2)],
        2
    ),
])
def test_cross_bingo(test_input, expected):
    board = Board()

    for (x, y) in test_input:
        board.hit(x, y)
    assert board.count_bingo() == expected
