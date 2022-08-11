import pathlib
import mido
from .shared import ingest_file
from typing import Tuple


def byte_to_note(b: int, time: int, velocity=64) -> mido.Message:
    if b > 127:
        return mido.Message(
            "note_on",
            channel=1,
            note=b % 127,
            time=time,
            velocity=velocity,
        )
    else:
        return mido.Message(
            "note_on",
            channel=0,
            note=b,
            time=20,
            velocity=velocity,
        )


def handle_midi(filename: pathlib.Path, output: pathlib.Path):
    mid = mido.MidiFile()
    track = mido.MidiTrack()
    mid.tracks.append(track)
    hex_array = ingest_file(filename)
    for i, b in enumerate(hex_array):
        note = byte_to_note(b, time=i)
        track.append(note)
    mid.save(output)
