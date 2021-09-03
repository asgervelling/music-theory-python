from typing import List

import notes
import constants
import chords
from exceptions import InvalidChordException


def with_accidental_name(note: str) -> str:
    """ 'Ab' -> 'AF'; F# -> FS """
    if notes.is_sharp(note):
        return note[0] + 'S'
    if notes.is_flat(note):
        return note[0] + 'F'
    return note


def note_name(note: str, octave: int):
    return f'{with_accidental_name(note).upper()}{octave}'


def note_name_from_val(note_val: int, octave: int) -> str:
    for key, val in constants.midi_notes.items():
        if val == note_val:
            return note_name(key, octave)
    return None


def note_names_from_val(note_val: int, octave: int) -> List[str]:
    """ Names of pitch constants with value and octave """
    names = [key for key, val
             in constants.midi_notes.items()
             if val == note_val]

    return names


def note_name_in_octave(note: str, octave: int):
    return note + str(octave)


def note(note, octave: int) -> int:
    try:
        if type(note) == int:
            return constants.midi_notes[note_name_in_octave(note, octave)]
        return constants.midi_notes[note_name(note, octave)]
    except KeyError:
        raise InvalidChordException(
            f'{constants.ERROR}: KeyError in midi.note(note={note}, octave={octave})')


def chord(chord_notation: str, root_note_octave: int = 4) -> List[int]:
    try:
        degr = chords.degrees(chord_notation)
        intervals = [constants.chord_intervals[deg] for deg in degr]
        root = notes.root_note_std_name(chord_notation)
        root_midi = note(root, root_note_octave)
        return list(map(lambda x: x + root_midi, intervals))

    # Top level function handles the exception
    except InvalidChordException as e:
        return [str(e)]
