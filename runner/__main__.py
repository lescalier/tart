import sys
from . import handler
import typer
import pathlib
import os


def main(filename: str, output: str):
    path = pathlib.Path(filename)
    if not path.exists():
        sys.stderr.write(f'Path does not exist: {path}')
        sys.exit(1)
    handler.handle(path, pathlib.Path(output))


if __name__ == '__main__':
    typer.run(main)
