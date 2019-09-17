import pytest
from life.tick import tick
from life.board import Board


@pytest.mark.parametrize('board,expected', [
    # new born
    (
            Board((
                [1, 1, 0],
                [0, 0, 1],
                [0, 0, 0],
            )),
            Board((
                [1, 1, 1],
                [1, 1, 1],
                [1, 1, 1],
            )),
    ),
    (
            Board((
                [0, 0, 0, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            )),
            Board((
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            )),
    ),
])
def test_tick(board, expected):
    assert tick(board) == expected
