# Pocket TTS Demo of Speaking with Marvin the Martian's Voice
# ===========================================================
#
# Pocket TTS, https://pypi.org/project/pocket-tts, is a text-to-speech engine
# with pretrained voices and has the ability to clone voices.
#
# For how to install dependencies and for other notes, see the comments in PocketTTS.py
#
# op sys:   Windows 11
# language: Python 3.13.14
# author:   RK
# date:     7/4/2026 - 8/7/2026

import PocketTTS
import time


# Main
def main():
    print('\nPocket TTS Demo\n---------------\n')
    print("Speaking with Marvin the Martian's voice ...\n")

    # Create a text-to-speech engine
    tts = PocketTTS.Engine(voice = 'marvin', verbose = True)

    # Speak

#   tts.speak( 'In 1976 the United States celebrated its bicentennial.' )
#   time.sleep(1)

#   tts.speak( '''Albert Einstein said, "If you can't explain it simply, you don't understand it well enough."''' )
#   time.sleep(1)

#   tts.speak( 'I found my Illudium Q36 Explosive Space Modulator! Now, say hello to Earth - for the last time!!!' )
#   time.sleep(1)

    tts.speak(
        'After sipping a cup of camomile tea last night, I woke up with a new perspective.\n'
        'I will modify my Illudium Q36 Explosive Space Modulator to communicate with Earth!\n'
        "Put on your laser safety glasses and SPF 100. Let's begin!!" )
    # Note, "camomile" should be spelled "chamomile", but that correct spelling isn't pronounced correctly.

    print('\nDone.\n')


if __name__ == '__main__':
    main()
