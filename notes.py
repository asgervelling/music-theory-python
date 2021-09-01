import re

import constants


def is_sharp(note: str) -> bool:
    if len(note) < 2:
        return False
    return note[1] in constants.accidentals['SHARP']


def is_flat(note: str) -> bool:
    if len(note) < 2:
        return False
    return note[1] in constants.accidentals['FLAT']


def root_note_simple_name(chord_notation: str) -> str:
    """ 'A#7b9' -> 'A#' """
    return re.search(r'^[A-G](#|b|♭)?', chord_notation).group()
