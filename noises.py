import sys
import getopt
import random
import time
import argparse
import msvcrt
from pathlib import Path
import winsound

parser = argparse.ArgumentParser(prog="noises.exe", description="Creates silence occaisionally interrupted with arbitrary WAV files")
parser.add_argument('files', nargs='+', type=str, help="Files to play")
parser.add_argument('-s', '--min-wait', type=int, default=60, help="Minimum possible wait time between plays")
parser.add_argument('-l', '--max-wait', type=int, default=600, help="Maximum possible wait time between plays")

def main():
    args = parser.parse_args()

    random_min = args.min_wait
    random_max = args.max_wait

    filenames = args.files
    
    print("Press X to Exit!")

    try:
        while True:
            wait_time = random.randrange(random_min, random_max)
            filename = filenames[random.randrange(0, len(filenames))]
            print(f"Playing {filename}!")
            winsound.PlaySound(filename, winsound.SND_FILENAME)

            if msvcrt.kbhit():
                if msvcrt.getch() == b'x':
                    sys.exit()

            time.sleep(wait_time)
    except SystemExit:
        sys.exit()
    except:
        print("Error Opening File!\nMake sure you typed it in correctly and that it is a WAV!!!")
        sys.exit(1)

main()