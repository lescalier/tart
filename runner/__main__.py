import sys
from . import image, audio
import typer
import pathlib
import logging

cli = typer.Typer()
logging.getLogger().setLevel(logging.INFO)


@cli.command("image")
def handle_image(filename: str, output: str):
    path = pathlib.Path(filename)
    if not path.exists():
        sys.stderr.write(f"Path does not exist: {path}")
        sys.exit(1)
    image.handle_image(path, pathlib.Path(output))


@cli.command("audio")
def handle_audio(filename: str, output: str):
    path = pathlib.Path(filename)
    if not path.exists():
        sys.stderr.write(f"Path does not exist: {path}")
        sys.exit(1)
    audio.handle_midi(path, pathlib.Path(output))


if __name__ == "__main__":
    cli()
