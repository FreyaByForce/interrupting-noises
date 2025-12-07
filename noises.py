import sys
import random
import time
import msvcrt
from pathlib import Path
import winsound

def main():
    if len(sys.argv) != 2 and len(sys.argv) != 4:
        print("Incorrect Usage!\nnoises.exe [FILENAME.wav] <minimum time> <maximum time>")
        sys.exit()
    
    filename = sys.argv[1]

    random_min = 60
    random_max = 600

    if len(sys.argv) == 4:
        random_min = int(sys.argv[2])
        random_max = int(sys.argv[3])
    
    print("Press X to Exit!")

    try:
        while True:
            wait_time = random.randrange(random_min, random_max)
            print("Playing Sound!!")
            winsound.PlaySound(filename, winsound.SND_FILENAME)

            if msvcrt.kbhit():
                if msvcrt.getch() == b'x':
                    sys.exit()

            time.sleep(wait_time)
    except:
        print("Error Opening File:\nMake sure you typed it in correctly and that it is a WAV!!!")
        sys.exit()

main()