# Interrupting Noises

A windows command line application for creating silence occaisionally interrupted by arbitrary WAV files.

## Usage

`noises.exe [filename.wav]`
This will play **filename.wav** repeatedly between a random wait time between the default 1-10 minutes.

`noises.exe [file1.wav] [file2.wav] ... --min-wait 10 --max-wait 30`
This will randomly choose any of the files to play before waiting between 10 to 30 seconds.

## Known Limitations

 - This application **only works with WAV files** as that is what the `winsound` library supports.
 - This application only works on Windows, as I have yet to find a cross-platform library for playing sound that works properly.