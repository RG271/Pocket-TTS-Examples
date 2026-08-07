# Text-to-Speech based on Pocket TTS
# ==================================
#
# This Python module speaks English text using Kyutai's Pocket TTS,
# https://pypi.org/project/pocket-tts/ , and uses sounddevice or FFmpeg's ffplay
# command to play the audio.  ffplay is only used when a special effect, such as
# increasing pitch, is needed.
#
# Pocket TTS is an excellent text-to-speech engine with pretrained voices and can
# clone voices.
# 
# Before installing dependencies, it may be necessary to enable Windows' long-paths option:
#   1. Press Win + R to open the Run dialog
#   2. Type regedit and press Enter to open the Registry Editor
#   3. Navigate to HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem
#   4. On the right side, double-click on LongPathsEnabled
#   5. Change the Value data from 0 to 1
#   6. Click OK and restart your computer
#
# To install dependencies:
#   1. pip install pocket-tts sounddevice soundfile
#   2. Install FFmpeg:
#      A. Open your web browser to https://www.gyan.dev/ffmpeg/builds
#      B. Scroll down to find, then click, either:
#          "ffmpeg-release-essentials.7z" or "ffmpeg-release-essentials.zip"
#      C. Unpack that file into a new directory, such as C:\ffmpeg
#      D. Append  C:\ffmpeg\bin  to the system path
#           i. Open Windows' Settings
#          ii. Search for "Edit the system environment variables"
#         iii. Click the "Environment Variables..." button
#         iii. Select the "Path" system (or user) environment variable, and click "Edit..."
#          iv. Append "C:\ffmpeg\bin" to Path's directory list
#
# How to use this Python module:
#   Create an instance of the Engine class, and call its speak() method.
#
# References:
#   https://pypi.org/project/pocket-tts
#   https://ffmpeg.org/download.html
#
# file:     PocketTTS.py
# op sys:   Windows 11
# language: Python 3.13.14
# author:   RK
# date:     7/4/2026 - 8/7/2026

import os, subprocess, time
from pocket_tts import TTSModel
# import scipy.io.wavfile
import sounddevice as sd
import soundfile as sf

TMP_FN = 'temporary.wav'   # (str) temporary WAV file, used by play()

# Pretrained Voices
# Note, these English female voices sound best: eponine, eve, jane, mary
PRETRAINED_VOICES = (   # list of voices' name and language
    ( 'alba',            'en' ),
    ( 'anna',            'en' ),
    ( 'azelma',          'en' ),
    ( 'bill_boerst',     'en' ),
    ( 'caro_davy',       'en' ),
    ( 'charles',         'en' ),
    ( 'cosette',         'en' ),
    ( 'eponine',         'en' ),
    ( 'estelle',         'fr' ),
    ( 'eve',             'en' ),
    ( 'fantine',         'en' ),
    ( 'george',          'en' ),
    ( 'giovanni',        'it' ),
    ( 'jane',            'en' ),
    ( 'javert',          'en' ),
    ( 'jean',            'en' ),
    ( 'juergen',         'de' ),
    ( 'lola',            'es' ),
    ( 'marius',          'en' ),
    ( 'mary',            'en' ),
    ( 'michael',         'en' ),
    ( 'paul',            'en' ),
    ( 'peter_yearsley',  'en' ),
    ( 'rafael',          'pt' ),
    ( 'stuart_bell',     'en' ),
    ( 'vera',            'en' )
)


# Text-to-Speech Class
# This class uses Pocket TTS (pocket-tts module).
class Engine:

    # Initializer
    # in: voice = (str) can be either:
    #               1. The name of a predefined voice (such as 'alba'; see PRETRAINED_VOICES)
    #               2. An audio file (*.wav) of the voice you would like to clone
    #               3. A voice-state file (*.safetensors), which was created from an audio file
    #               4. 'marvin', which specifies the voice-state file './marvin1/voice.safetensors'
    #                    that was created from audio clips of WB Kids' Looney Tunes' Space Adventures
    #                    https://www.youtube.com/watch?v=CbcstzFqGx0
    #             The audio file may be local or at Hugging Face, for example: './some_audio.wav'
    #             or 'hf://kyutai/tts-voices/expresso/ex01-ex02_default_001_channel2_198s.wav'.
    #             The audio file should be <30 seconds, mono, and 24000 or 48000 Hz; longer files
    #             seem to create corrupt output.
    #     increasePitch = (bool) if True, raises the voice's pitch.  Note, raising the pitch of
    #             an adult's voice will sound like a child's or cartoon character's voice.
    #     verbose = (bool) if True, debugging messages will be printed
    def __init__(self, voice = 'mary', increasePitch = False, verbose = False):
        self.verbose = verbose
        if verbose:
            print('INFO: Loading model')
        self.model = TTSModel.load_model()
        if verbose:
            sr = self.model.sample_rate    # (int) sample rate, typically 24000 Hz
            print(f"INFO: Model's sample rate is {sr} Hz")
        if voice == 'marvin':
            voice = './marvin1/voice.safetensors'
        self.voice = self.model.get_state_for_audio_prompt(voice)
        self.increasePitch = increasePitch


    # Play Audio Data
    # Either sounddevice or FFmpeg's ffplay command is used to play audio data.  ffplay can
    # apply audio special effects, and will be used when self.increasePitch is true.
    # instance in: self.increasePitch, self.verbose
    # in: data = (numpy.ndarray) 1D array of float32 audio samples
    #     sampleRate = (int >0) data's sample rate in Hz
    def _play(self, data, sampleRate):
        cmd = ['ffplay', '-nodisp', '-autoexit']
        if self.increasePitch:
            # Specify audio filters
            # For a faster temp use: atempo=1.1,rubberband=pitch=1.2,volume=3
            cmd += ['-af', 'rubberband=pitch=1.2,volume=3']

            # Write audio to WAV file with format: pcm_s16le, 24000 Hz, 1 channel
            sf.write(TMP_FN, data, sampleRate)
            if self.verbose:
                print(f'INFO: Wrote audio to {TMP_FN}')

            # # Write audio to WAV file with format: pcm_f32le, 24000 Hz, 1 channel
            # scipy.io.wavfile.write(TMP_FN, sampleRate, data)
            # if self.verbose:
            #     print(f'INFO: Wrote audio to {TMP_FN}')

            # Play WAV file pitch shifted upward to sound like a child or a cartoon character
            if self.verbose:
                print('INFO: Playing with increased pitch')
            cmd.append(TMP_FN)
            subprocess.run( cmd,
                            capture_output = False, stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL,
                            creationflags = subprocess.CREATE_NO_WINDOW )
            if self.verbose:
                print('INFO: Playing finished')

            # Clean up
            os.remove(TMP_FN)
            if self.verbose:
                print(f'INFO: Removed {TMP_FN}')

        else:
            # Play audio without increasing its pitch
            if self.verbose:
                print('INFO: Playing')
            sd.play(data, samplerate = sampleRate)
            sd.wait()   # wait for playback to finish
            if self.verbose:
                print('INFO: Playing finished')


    # Speak
    # in: text = (str) the text to speak
    def speak(self, text):
        if self.verbose:
            print(f'INFO: Converting text to speech:\n  {text}')
            t0 = time.time()
            result = self.model.generate_audio(self.voice, text)   # (torch.Tensor) PCM audio data
            dt = time.time() - t0   # (float) duration in seconds
            print(f'INFO: conversion time: {dt:.3f} s')
        else:
            result = self.model.generate_audio(self.voice, text)   # (torch.Tensor) PCM audio data
        data = result.numpy()                 # (numpy.ndarray) 1D array of float32 audio samples
        sampleRate = self.model.sample_rate   # (int >0) data's sample rate in Hz
        self._play(data, sampleRate)



# If this module is run directly, rather than being imported and used by
# another script, speak some example text.
if __name__ == '__main__':
    tts = Engine(voice = 'mary', increasePitch = False, verbose = True)
#   tts = Engine(voice = 'mary', increasePitch = True,  verbose = True)
#   tts = Engine(voice = 'marvin', increasePitch = False, verbose = True)
    tts.speak( 'In 1976 the United States celebrated its bicentennial.' )
    time.sleep(1)
    tts.speak( '''Albert Einstein said, "If you can't explain it simply, you don't understand it well enough."''' )
    print()
