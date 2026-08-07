# Create Voice State File
#
# This script reads file INPUT_FN, which is a <30 second, mono, 24000 or 48000 Hz, audio clip
# of speech in the voice you want to clone.  The script outputs voice-state file, OUTPUT_FN,
# which can be used to speak in that voice:
#   voice_state = import_model_state(OUTPUT_FN)
#   audio = model.generate_audio(voice_state, 'I forgot to plug in my laser!')
#
# Ref: https://huggingface.co/kyutai/pocket-tts
#
# Author: RK
# Date:   7/22/2026 - 8/3/2026

# from pocket_tts import TTSModel, export_model_state, import_model_state
from pocket_tts import TTSModel, export_model_state

INPUT_FN  = 'voice.wav'
OUTPUT_FN = 'voice.safetensors'


model = TTSModel.load_model()

# Export a voice state for fast loading later
print(f'\nReading {INPUT_FN} ...')
voice_state = model.get_state_for_audio_prompt('./' + INPUT_FN)
print(f'Writing {OUTPUT_FN} ...')
export_model_state(voice_state, OUTPUT_FN)
print('Done\n')