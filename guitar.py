import numpy as np
import matplotlib.pyplot as plt

fretboard = {
    'E2': [(6, 0)],
    'F2': [(6, 1)],
    'F#/Gb2': [(6, 2)],
    'G2': [(6, 3)],
    'G#/Ab2': [(6, 4)],
    'A2': [(6, 5), (5, 0)],
    'A#/Bb2': [(6, 6), (5, 1)],
    'B2': [(6, 7), (5, 2)],
    'C3': [(6, 8), (5, 3)],
    'C#/Db3': [(6, 9), (5, 4)],
    'D3': [(6, 10), (5, 5), (4, 0)],
    'D#/Eb3': [(6, 11), (5, 6), (4, 1)],
    'E3': [(6, 12), (5, 7), (4, 2)],
    'F3': [(6, 13), (5, 8), (4, 3)],
    'F#/Gb3': [(6, 14), (5, 9), (4, 4)],
    'G3': [(6, 15), (5, 10), (4, 5), (3, 0)],
    'G#/Ab3': [(6, 16), (5, 11), (4, 6), (3, 1)],
    'A3': [(6, 17), (5, 12), (4, 7), (3, 2)],
    'A#/Bb3': [(6, 18), (5, 13), (4, 8), (3, 3)],
    'B3': [(6, 19), (5, 14), (4, 9), (3, 4), (2, 0)],
    'C4': [(6, 20), (5, 15), (4, 10), (3, 5), (2, 1)],
    'C#/Db4': [(6, 21), (5, 16), (4, 11), (3, 6), (2, 2)],
    'D4': [(6, 22), (5, 17), (4, 12), (3, 7), (2, 3)],
    'D#/Eb4': [(6, 23), (5, 18), (4, 13), (3, 8), (2, 4)],
    'E4': [(6, 24), (5, 19), (4, 14), (3, 9), (2, 5), (1, 0)],
    'F4': [(5, 20), (4, 15), (3, 10), (2, 6), (1, 1)],
    'F#/Gb4': [(5, 21), (4, 16), (3, 11), (2, 7), (1, 2)],
    'G4': [(5, 22), (4, 17), (3, 12), (2, 8), (1, 3)],
    'G#/Ab4': [(5, 23), (4, 18), (3, 13), (2, 9), (1, 4)],
    'A4': [(5, 24), (4, 19), (3, 14), (2, 10), (1, 5)],
    'A#/Bb4': [(4, 20), (3, 15), (2, 11), (1, 6)],
    'B4': [(4, 21), (3, 16), (2, 12), (1, 7)],
    'C5': [(4, 22), (3, 17), (2, 13), (1, 8)],
    'C#/Db5': [(4, 23), (3, 18), (2, 14), (1, 9)],
    'D5': [(4, 24), (3, 19), (2, 15), (1, 10)],
    'D#/Eb5': [(3, 20), (2, 16), (1, 11)],
    'E5': [(3, 21), (2, 17), (1, 12)],
    'F5': [(3, 22), (2, 18), (1, 13)],
    'F#/Gb5': [(3, 23), (2, 19), (1, 14)],
    'G5': [(3, 24), (2, 20), (1, 15)],
    'G#/Ab5': [(2, 21), (1, 16)],
    'A5': [(2, 22), (1, 17)],
    'A#/Bb5': [(2, 23), (1, 18)],
    'B5': [(2, 24), (1, 19)],
    'C6': [(1, 20)],
    'C#/Db6': [(1, 21)],
    'D6': [(1, 22)],
    'D#/Eb6': [(1, 23)],
    'E6': [(1, 24)],
}

def define_path(paths, trend_left=True, starting_finger=2):
    current = paths[0][-1]
    domain = range(current[1] - 2, current[1] + 3)
    path = []
    for layer in paths:
        lowest_score = 100
        found = False
        for fret in layer:
            if fret[1] in domain:
                path.append(fret)
                found = True
                break
            
            # Otherwise we give it a score
            score = np.abs(current[1] - fret[1])
            if score < lowest_score:
                lowest_score = score
                best_choice = fret
        
        if found == False: path.append(best_choice)
    
    return path

def plot_path(path):
    # Prepare TAB lines
    plt.figure(figsize=[20, 7])
    plt.margins(y=2)
    plt.axis('off')
    plt.plot((0, len(path)), (6, 6), color='gray')
    plt.plot((0, len(path)), (5, 5), color='gray')
    plt.plot((0, len(path)), (4, 4), color='gray')
    plt.plot((0, len(path)), (3, 3), color='gray')
    plt.plot((0, len(path)), (2, 2), color='gray')
    plt.plot((0, len(path)), (1, 1), color='gray')

    # Plot notes
    for i, elem in enumerate(path):
        plt.text(
            x=i + 0.5, 
            y=((7-elem[0])), 
            s=str(elem[1]), 
            fontsize='xx-large',
            fontweight='bold',
            fontfamily='monospace',
            ha='center', 
            va='center'
        )

    plt.savefig('temp', bbox_inches='tight')
            