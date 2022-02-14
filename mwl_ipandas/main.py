import ipdb
import typer

import pandas as pd

from pathlib import Path
from typing import Optional


app = typer.Typer()

@app.callback()
def callback():
    """
    This app opens pandas dataframe in an interactive mode
    """


def input_valid(path):
    if path is None:
        typer.echo("No input path given")
        return False
    if path.is_dir():
        typer.echo("Path is a directory")
        return False
    elif not path.exists():
        typer.echo("The path doesn't exist")
        return False
    elif path.is_file():
        return True
    else:
        typer.echo("Path is not valid for unknown reason.")
        return False



def load_dataframe(path):

    df = None
    if path.suffix in ([".pickle", ".pkl"]):
        df = pd.read_pickle(path)

    elif path.suffix == ".csv":
        df = pd.read_csv(path)

    return df


@app.command()
def load(path: Optional[Path] = typer.Argument(None)):
    """
    Load a dataframe
    """
    if not input_valid(path):
        raise typer.Abort()

    df = load_dataframe(path)
    
    typer.echo(df.columns)
    typer.echo(df.head())
    
    ipdb.set_trace()

