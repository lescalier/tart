import logging
import pathlib
import io


def ingest_file(filename: pathlib.Path, mode="rb") -> bytearray:
    tf = io.BytesIO()
    with open(filename, mode) as f:
        tf.write(f.read())
    tf.seek(0)
    return bytearray(tf.read())
