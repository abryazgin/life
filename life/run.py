import time
from life.tick import tick
from life.exc import GenocideLifeException, CircleLifeException
from life.cache import Cache


def _life(board, t):
    cache = Cache()
    while board:
        print(board)
        board_hash = hash(board)
        if board_hash in cache:
            raise CircleLifeException
        cache.add(board_hash)
        time.sleep(t)
        board = tick(board)
    print(board)
    raise GenocideLifeException


def run(board, t):
    try:
        _life(board, t)
    except CircleLifeException:
        print("Circle detected")
    except GenocideLifeException:
        print("Game over")
    except KeyboardInterrupt:
        print("Break game")
