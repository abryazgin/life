from life.board import Board


def tick(board: Board) -> Board:
    res = Board(
        [int(state(h, w, board))
         for w, el in enumerate(row)]
        for h, row in enumerate(board)
    )
    return res


def state(h, w, board):
    if board[h][w] == -1:
        return 0
    if board[h][w] and check(h, w, board):
        return 1
    elif board[h][w] and not check(h, w, board):
        return -1
    else:
        return check(h, w, board)


def check(h, w, board) -> int:
    neighbors_count = calc_neighbor(h, w, board)
    if board[h][w]:
        return neighbors_count in [2, 3]
    return neighbors_count in [3]


def calc_neighbor(h, w, board):
    neighbor_indexes = [
        (h - 1, w - 1),
        (h - 1, w),
        (h - 1, w + 1),

        (h, w - 1),
        (h, w + 1),

        (h + 1, w - 1),
        (h + 1, w),
        (h + 1, w + 1),
    ]
    neighbor_indexes = [
        (
            h_i % len(board),
            w_i % len(board[0])
         ) for h_i, w_i in neighbor_indexes]
    return sum(board[h_i][w_i] for h_i, w_i in neighbor_indexes if board[h_i][w_i] > 0)
