# tart

Encode files in different art forms. Supports images and audio.

## Image

```sh
python -m runner image ./data/archive.tar.gz image.png
```

For now, output_file must be a format that PIL can write to (like PNG, BMP, JPG, etc)

![Example output](examples/output.png?raw=true "For example")


## Audio

```sh
python -m runner audio ./data/archive.tar.gz output.midi
```

Use something like timidity (`brew install timidity`) in conjunction with ffmpeg to convert midi to mp3:

```sh
timidity input_file.mid -Ow -o - | ffmpeg -i - -acodec libmp3lame -ab 64k output_file.mp3
```

![Example output](examples/output.mp3?raw=true "Audio example")
