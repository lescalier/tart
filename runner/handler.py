import logging
import pathlib
import math
import io
import numpy as np
from PIL import Image

logging.getLogger().setLevel(logging.INFO)


def ingest_file(filename: pathlib.Path, mode='rb') -> bytearray:
    tf = io.BytesIO()
    with open(filename, mode) as f:
        tf.write(f.read())
    tf.seek(0)
    return bytearray(tf.read())


def handle(filename: pathlib.Path, output: pathlib.Path):
    hex_array = ingest_file(filename)
    side = math.ceil(math.sqrt(math.ceil(len(hex_array) / 3.0)))
    padding_needed = ((3 * side) ** 2) - len(hex_array)
    arr = np.array(
        hex_array + bytearray([0 for i in range(padding_needed)]), dtype=np.uint8
    )
    arr.resize(3 * side, 3 * side)
    img = Image.frombytes('RGB', data=arr, size=(side, side))
    scale = 50

    img = img.resize((side * scale, side * scale), resample=0)
    img.save(output, quality=100)
