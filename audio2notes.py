import numpy as np
from scipy.fft import fft

def initialize_TET_notes():
    notes = [
        'A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D',
        'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab'
    ]
    ratio = 1.059463094359295
    table = [('A0', 27.5)]
    register = 0
    for i in range(1, 88):
        table.append((f'{notes[i%12]}{register}', round(table[-1][1] * ratio, 2)))
        if notes[i%12] == 'B':
            register += 1
    return table

def extract_frequencies(clips, sample_rate):
    for clip in clips:
        fft_data = fft(clip)
        frequencies = np.fft.fftfreq(len(clip))
        
        peak_coefficient = np.argmax(np.abs(fft_data))
        peak_freq = frequencies[peak_coefficient]
        yield round(peak_freq * sample_rate, 2)

def map_frequencies(frequencies, note_map) -> str:
    for frequency in frequencies:
        note_map_copy = note_map
        while True:
            midpoint = len(note_map_copy) // 2
            if frequency > note_map_copy[midpoint][1]:
                note_map_copy = note_map_copy[midpoint:]
            else:
                note_map_copy = note_map_copy[:midpoint+1]

            if len(note_map_copy) == 2:
                a_diff = np.abs(frequency - note_map_copy[0][1])
                b_diff = np.abs(frequency - note_map_copy[1][1])
                yield note_map_copy[0] if a_diff < b_diff else note_map_copy[1]
                break
            