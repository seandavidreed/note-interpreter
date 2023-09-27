import sys, os, librosa
from audio2notes import *
from guitar import *

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
    audio_data, sample_rate = librosa.load(sys.argv[1], sr=44100)

    # Split audio file according to silences.
    # Get interval of sample indices for each discretized sound.
    intervals = librosa.effects.split(audio_data, top_db=20)

    # Get audio clips using sample index intervals.
    clips = map(lambda a: audio_data[a[0]:a[1]], intervals)

    # Perform Fast Fourier Transform on each clip.
    # Isolate the frequency of each clip.
    frequencies = extract_frequencies(clips, sample_rate)

    # Initialize 12-TET frequency name tuples.
    note_map = initialize_12TET_notes()

    # Use binary search to map each frequency
    # according to a schema, in this case
    # 12-tone Equal Temperament.
    notes = map_frequencies(frequencies, note_map)
    notes = [note for note in notes]
    print(notes)
    
    # Generate a list of lists of potential frets for
    # each note in the melody.
    layers = list(map(lambda x: fretboard[x[0]], notes))

    # Get viable paths sorted according to score.
    results = get_viable_paths(layers)

    for result in results:
        print(result)
        print()

    # Generate TAB for result with highest score.
    plot_path(results[0][0])


if __name__ == "__main__":
    main()