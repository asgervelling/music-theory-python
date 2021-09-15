import re
from typing import List

from .scales import find_note_index, note_names
from .constants import accidentals


def is_sharp(note: str) -> bool:
    if len(note) < 2:
        return False
    return note[1] in accidentals['SHARP']


def is_flat(note: str) -> bool:
    if len(note) < 2:
        return False
    return note[1] in accidentals['FLAT']


def std_name_for_root(chord_notation: str) -> str:
    """ 'A#7b9' -> 'A#' """
    return re.search(r'^[A-G](#|b|♭)?', chord_notation).group()


def sort_notes(notes_to_sort: List[str]):
    indices = []
    for i in range(len(notes_to_sort)):
        indices.append(find_note_index(
            note_names, notes_to_sort[i]))

    return [x for _, x in sorted(zip(indices, notes_to_sort))]
