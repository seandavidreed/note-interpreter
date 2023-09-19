import sys
import os
from scipy import io
from freq import SampleProcessor


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 {__file__.split(sep=os.sep)[-1]} <audio.wav>")
        return -1
    
    if sys.argv[1].split(sep='.')[-1].lower() != "wav":
        print("Audio file supplied must be wav format")
        return -1

    sample_rate, data = io.wavfile.read(sys.argv[1])
    
    freq = SampleProcessor(sample_rate, data)

    freq.extract_frequency()
    note = freq.identify_note()
    print(note)

if __name__ == "__main__":
    main()