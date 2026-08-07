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
    voice = 'mary'   # (str) one of the voice names from PocketTTS.PRETRAINED_VOICES

    print('\nPocket TTS Demo\n---------------')


    print(f'\nSpeaking with pretrained voice "{voice}" ...\n')

    # Create a text-to-speech engine
    tts = PocketTTS.Engine(voice = voice, verbose = True)

    # Speak
    tts.speak( 'In 1976 the United States celebrated its bicentennial.' )
    time.sleep(1)
    tts.speak( '''Albert Einstein said, "If you can't explain it simply, you don't understand it well enough."''' )


    print(f'\nSpeaking with pretrained voice "{voice}" and raised pitch ...\n')

    # Create a text-to-speech engine
    tts = PocketTTS.Engine(voice = voice, increasePitch = True, verbose = True)

    # Speak
    tts.speak( 'In 1976 the United States celebrated its bicentennial.' )
    time.sleep(1)
    tts.speak( '''Albert Einstein said, "If you can't explain it simply, you don't understand it well enough."''' )


    print('\nDone.\n')


if __name__ == '__main__':
    main()
