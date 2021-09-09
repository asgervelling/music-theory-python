from typing import List

from .notes import is_sharp, is_flat
from .constants import midi_notes, ERROR
from .exceptions import InvalidChordException


def with_accidental_name(note: str) -> str:
    """ 'Ab' -> 'AF'; F# -> FS """
    if is_sharp(note):
        return note[0] + 'S'
    if is_flat(note):
        return note[0] + 'F'
    return note


def note_name(note: str, octave: int):
    return f'{with_accidental_name(note).upper()}{octave}'


def note_name_from_val(note_val: int, octave: int) -> str:
    for key, val in midi_notes.items():
        if val == note_val:
            return key
    return None


def note_names_from_val(note_val: int, octave: int) -> List[str]:
    """ Names of pitch constants with value and octave """
    names = [key for key, val
             in midi_notes.items()
             if val == note_val]

    return names


def note_name_in_octave(note: str, octave: int):
    return note + str(octave)


def midi_note(note, octave: int) -> int:
    try:
        if type(note) == int:
            return midi_notes[note_name_in_octave(note, octave)]
        return midi_notes[note_name(note, octave)]
    except KeyError:
        raise InvalidChordException(
            f'{ERROR}: KeyError in midi.note(note={note}, octave={octave})')


def notation_from_midi(midi_values: List[int], root_note: str):
    print(midi_note(val, 4) for val in midi_values)
