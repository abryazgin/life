import pytest
from life.tick import calc_neighbor
from life.board import Board


@pytest.mark.parametrize('board,h,w,expected', [
    # new born
    (
            Board((
                [1, 1, 0],
                [0, 0, 1],
                [0, 0, 0],
            )),
            1, 1, 3
    ),
    (
            Board((
                [1, 1, 0],
                [0, 0, 1],
                [0, 0, 0],
            )),
            0, 0, 2
    ),
    (
            Board((
                [1, 1, 1],
                [1, 1, 1],
                [1, 1, 1],
            )),
            0, 0, 8
    ),
])
def test_calc(board, h, w, expected):
    assert calc_neighbor(h, w, board) == expected
