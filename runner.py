import click
from life.run import run
from life.board import Board


@click.command()
@click.option('--w', type=int, default=3)
@click.option('--h', type=int, default=3)
@click.option('--t', type=float, default=1)
def start(w, h, t):
    run(Board.generate(w, h), t)
    # run(Board((
    #     [0, 0, 0, 0, 0],
    #     [0, 1, 0, 0, 0],
    #     [0, 0, 1, 1, 0],
    #     [0, 1, 1, 0, 0],
    #     [0, 0, 0, 0, 0],
    # )), 0.01)


if __name__ == '__main__':
    start()
