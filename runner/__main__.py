from . import handler
import pathlib
import os

if __name__ == '__main__':
    base = pathlib.Path(os.path.abspath(__file__)).parents[1]
    handler.handle(base / "data" / "tornado-core-2.1.tar.gz")
