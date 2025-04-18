from pydub import AudioSegment
import os

INPUT_DIR = "whale_audio"
OUTPUT_DIR = "whale_audio_clean"
os.makedirs(OUTPUT_DIR, exist_ok=True) # Only make if doesn't exist

MIN_DURATION = 3 * 1000
MAX_DURATION = 30 * 1000

# Process .wav files with whale audio
for filename in os.listdir(INPUT_DIR):
    if filename.endswith(".wav"):
        try:
            path = os.path.join(INPUT_DIR, filename)
            audio = AudioSegment.from_file(path)

            if MIN_DURATION <= len(audio) <= MAX_DURATION:
                # Convert to mono and 16kHz
                audio = audio.set_channels(1).set_frame_rate(16000)
                out_path = os.path.join(OUTPUT_DIR, filename)
                audio.export(out_path, format="wav")
                print(f"Processed: {filename}")
            else:
                print(f"Skip out of range file: {filename}")
        except Exception as e:
            print(f"Error with {filename}: {e}")