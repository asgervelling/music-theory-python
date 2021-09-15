from chords.exceptions import InvalidChordException
from chords.notation import degrees, midi_chord

class Chord:

    def __init__(self, chord_notation: str):
        self.degrees = degrees(chord_notation)
        self.midi = midi_chord(chord_notation)
        