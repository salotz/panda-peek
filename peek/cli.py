import sys

import pandas as pd

import click

@click.command()
@click.option('--only-columns', '-C', is_flag=True, help="show only the columns for the table")
@click.argument('csv', nargs=1, type=click.Path(exists=True))
def peek(only_columns, csv):

    df = pd.read_csv(csv, index_col=0)

    # flags for only showing part of the data
    if only_columns:
        for column in df.columns.values:
            sys.stdout.write(column.__str__() + "\n")
        return None

    sys.stdout.write(df.__str__() + "\n")

    return None

if __name__ == "__main__":
    peek()
