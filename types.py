from pprint import pprint

import chords
import midi
import notes
import scales

from exceptions import InvalidChordException


class Chord():

    def __init__(self, chord_notation: str):
        self.chord_notation = chord_notation

    def degrees(self):
        return chords.degrees(self.chord_notation)

    def notes(self):
        return list(map(notes.std_name_for_note, self.midi_notes()))

    def notes_from_midi(self, midi_values):
        return list(map(notes.std_name_for_note, midi_values))

    def midi_notes(self, octave=4):
        return midi.chord(self.chord_notation, octave)

    def __add__(self, other):
        print(other)

        degrs = chords.sort_degrees(
            list(set(self.degrees() + other.degrees())))
        note_names = chords.sort_notes(list(set(self.notes() + other.notes())))

        midi_values = sorted(list(set(self.midi_notes() + other.midi_notes())))

        print(note_names)
        print(midi_values)

        print(scales.interval_between('E', 'C'))
        print(scales.interval_between('C', 'E'))

        # To-do: find chord notations based on notes in chord or midi values
        return self

    def __repr__(self):
        return f"""
    {self.chord_notation}:
    Degrees:     {self.degrees()}
    Notes:       {self.notes()}
    MIDI values: {self.midi_notes()}
        """


####

Chord('Em') + Chord('C')
_scales = {
    'c_major': ['C', 'D', 'E', 'F', 'G', 'A', 'B']
}

note_names = [
    ['B#',  'C',  'Dbb'],
    ['B##', 'C#', 'Db'],
    ['C##', 'D',  'Ebb'],
    ['D#',  'Eb', 'Fbb'],
    ['D##', 'E',  'Fb'],
    ['E#',  'F',  'Gbb'],
    ['E##', 'F#', 'Gb'],
    ['F##', 'G',  'Abb'],
    ['G#',  'Ab'],
    ['G##', 'A',  'Bbb'],
    ['A#',  'Bb', 'Cbb'],
    ['A##', 'B',  'Cb'],
]


def find_note_index(scale, search_note):
    ''' Given a scale, find the index of a particular note '''
    for index, note in enumerate(scale):
        # Deal with situations where we have a list of enharmonic
        # equivalents, as well as just a single note as and str.
        if type(note) == list:
            if search_note in note:
                return index
        elif type(note) == str:
            if search_note == note:
                return index
    raise InvalidChordException(f'Invalid note "{search_note}"')


def rotate(scale, n):
    ''' Left-rotate a scale by n positions. '''
    return scale[n:] + scale[:n]


def chromatic(key):
    ''' Generate a chromatic scale in a given key. '''
    # Figure out how much to rotate the notes list by and return
    # the rotated version.
    num_rotations = find_note_index(note_names, key)
    return rotate(note_names, num_rotations)


"""
print(Chord('C13'))
print(Chord('D7#9'))
print(Chord('G7b9'))
print(Chord('CmMaj'))
print(Chord('A#maj11'))
print(Chord('C#7sus'))
print(Chord('E9sus2'))
"""
