# Pocket-TTS-Examples

Example Python scripts for text-to-speech using Pocket TTS on a basic Windows 11 PC &mdash;
no NVIDIA GPU required.


## Development Platform

These scripts were developed in Python 3.13 on a desktop PC with the following specs:
* Operating system: Windows 11 Pro 25H2
* Processor: Intel(R) Core(TM) i5-14500 (2.60 GHz)
* RAM: 32.0 GB
* Graphics card: Intel(R) UHD Graphics 770 (128 MB)


## How to Install Dependencies

Before installing dependencies, it may be necessary to enable Windows' long-paths option:
1. Press `Win` + `R` to open the Run dialog
1. Type `regedit` and press `Enter` to open the Registry Editor
1. Navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem`
1. On the right side, double-click on `LongPathsEnabled`
1. Change the Value data from `0` to `1`
1. Click OK and restart your computer

To install the dependencies:
1. pip install pocket-tts sounddevice soundfile
1. Install FFmpeg:
   1. Open your web browser to https://www.gyan.dev/ffmpeg/builds
   1. Scroll down to find, then click, either: `ffmpeg-release-essentials.7z` or `ffmpeg-release-essentials.zip`
   1. Unpack that file into a new directory, such as `C:\ffmpeg`
   1. Append `C:\ffmpeg\bin` to the system path
      1. Open Windows' Settings
      1. Search for "Edit the system environment variables"
      1. Click the "Environment Variables..." button
      1. Select the `Path` system (or user) environment variable, and click "Edit..."
      1. Append `C:\ffmpeg\bin` to Path's directory list


## How to Run the Examples

Simply execute the demo scripts from within a *Windows PowerShell* or *Command Prompt (CMD)* window:
* `python .\demo_cloned_voice.py`
* `python .\demo_pretrained_voice.py`
