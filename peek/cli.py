import sys

import pandas as pd

import click

@click.command()
@click.argument('csv', nargs=1, type=click.Path(exists=True))
def peek(csv):
    df = pd.read_csv(csv, index_col=0)
    sys.stdout.write(df.__str__())

if __name__ == "__main__":
    peek()
