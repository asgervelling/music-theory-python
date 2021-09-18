from typing import List

from .notes import is_sharp, is_flat
from .constants import midi_notes, ERROR
from .exceptions import InvalidChordException
from .helpers import shortest_key_for_val


def _with_accidental_name(note: str) -> str:
    """ 'Ab' -> 'AF'; F# -> FS """
    if is_sharp(note):
        return note[0] + 'S'
    if is_flat(note):
        return note[0] + 'F'
    return note


def note_name(note: str, octave: int):
    """ ('C#', '4') -> 'CS4' """
    return f'{_with_accidental_name(note).upper()}{octave}'


def note_name_from_val(note_val: int) -> str:
    """ Todo: Take sharp and flat keys into consideration. """
    return shortest_key_for_val(note_val, midi_notes)


def note_names_from_val(note_val: int, octave: int) -> List[str]:
    """ (61, 4) -> ['CS4', 'DF4'] """
    names = [key for key, val
             in midi_notes.items()
             if val == note_val]

    return names


def midi_note(std_note_name: str, octave: int) -> int:
    """ ('C#', '4') -> 61 """
    try:
        return midi_notes[note_name(std_note_name, octave)]
    except KeyError:
        raise InvalidChordException(
            f'{ERROR}: KeyError in midi.note(note={std_note_name}, octave={octave})')
