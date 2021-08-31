from typing import List

import notes
import constants
import chords


def with_accidental_name(note: str) -> str:
    if notes.is_sharp(note):
        return note[0] + 'S'
    if notes.is_flat(note):
        return note[0] + 'F'
    return note


def note_name(note: str, octave: int):
    return f'{with_accidental_name(note).upper()}{octave}'


def note_name_from_val(note_val: int, octave: int):
    for key, val in constants.chord_intervals.items():
        if val == note_val:
            print(val)
            return note_name(key, octave)
    return None


def note_name_in_octave(note: str, octave: int):
    return note + str(octave)


def note(note, octave: int) -> int:
    if type(note) == int:
        return constants.midi_notes[note_name_in_octave(note, octave)]
    return constants.midi_notes[note_name(note, octave)]


def chord(chord_notation: str, root_note_octave: int = 4) -> List[int]:
    degr = chords.degrees(chord_notation)
    intervals = [constants.chord_intervals[deg] for deg in degr]
    root = notes.root_note_simple_name(chord_notation)
    root_midi = note(root, root_note_octave)
    return list(map(lambda x: x + root_midi, intervals))
