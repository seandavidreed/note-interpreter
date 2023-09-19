import sys
import os
import librosa
from noteprocessor import NoteProcessor


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 {__file__.split(sep=os.sep)[-1]} <audio.wav>")
        return -1
    
    if sys.argv[1].split(sep='.')[-1].lower() != "wav":
        print("Audio file supplied must be wav format")
        return -1

    audio_data, sample_rate = librosa.load(sys.argv[1])

    intervals = librosa.effects.split(audio_data, top_db=20)
    clips = map(lambda a: audio_data[a[0]:a[1]], intervals)
    frequencies = [NoteProcessor(sample_rate, clip) for clip in clips]

    for freq in frequencies:
        freq.extract_frequency()
        print(freq.identify_note())
        print(freq.frequency)
        print()

if __name__ == "__main__":
    main()