import sys, os, librosa
from audio2notes import *

def main():
    # Handle incorrect argument count error.
    if len(sys.argv) != 2:
        print(f"Usage: python3 {__file__.split(sep=os.sep)[-1]} <audio.wav>")
        return -1
    
    # Handle incorrect file format error.
    if sys.argv[1].split(sep='.')[-1].lower() != "wav":
        print("Audio file supplied must be wav format")
        return -1

    # Open audio file and store contents.
    audio_data, sample_rate = librosa.load(sys.argv[1])

    # Split audio file according to silences.
    # Get interval of sample indices for each discretized sound.
    intervals = librosa.effects.split(audio_data, top_db=20)

    # Get audio clips using sample index intervals.
    clips = map(lambda a: audio_data[a[0]:a[1]], intervals)

    # Perform Fast Fourier Transform on each clip.
    # Isolate the frequency of each clip.
    frequencies = extract_frequencies(clips, sample_rate)

    # Initialize 12-TET frequency name tuples.
    note_map = initialize_TET_notes()

    # Use binary search to map each frequency
    # according to a schema, in this case
    # 12-tone Equal Temperament.
    notes = map_frequencies(frequencies, note_map)

    print([note[0] for note in notes])

if __name__ == "__main__":
    main()