import numpy as np
from scipy.fft import fft


class NoteProcessor:
    def __init__(self, sample_rate=None, audio_data=None):
        if sample_rate is None or audio_data is None:
            raise TypeError("SampleProcessor constructor arguments cannot be NoneType")
        
        self.sample_rate = sample_rate
        self.audio_data = audio_data
        self.frequency = None
        self.notes = NoteProcessor.calculate_note_frequencies()
    
    @classmethod
    def calculate_note_frequencies(cls):
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

    def extract_frequency(self):
        fft_data = fft(self.audio_data)
        frequencies = np.fft.fftfreq(len(self.audio_data))
        
        peak_coefficient = np.argmax(np.abs(fft_data))
        peak_freq = frequencies[peak_coefficient]

        self.frequency = round(peak_freq * self.sample_rate, 2)

    def identify_note(self) -> str:
        notes_copy = self.notes
        while True:  
            midpoint = len(notes_copy) // 2
            if self.frequency > notes_copy[midpoint][1]:
                notes_copy = notes_copy[midpoint:]
            else:
                notes_copy = notes_copy[:midpoint+1]

            if len(notes_copy) == 2:
                return notes_copy[1]
            