Notes on Creating an Audio File of Marvin the Martian Speaking   8/3/2026
==============================================================

voice_raw.wav was created by
1. Using Audacity to record in loopback mode (mono, 48000 samples/second) some audio from
     YouTube video "Looney Tuesdays | Space Adventures | Looney Tunes | WB Kids"
     https://www.youtube.com/watch?v=CbcstzFqGx0
2. Deleting segments where Marvin was not speaking
3. Raising the amplitude as much as possible without saturating any samples

voice.wav was created by uploading voice_raw.wav to https://remove.music/ to remove
background music.  Audacity was used in loopback mode (mono, 48000 Hz) to record the
audio output of that website.  It was then used to shorten the file to <30 seconds
and resample at 24000 Hz.

voice.safetensors was created from voice.wav by export_cloned_voice.py .
N.B., Ultralytics appears to only allow WAV files <30 seconds; longer files
create corrupt output.