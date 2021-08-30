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
    if len(chord_notation) < 2:
        return chord_notation[0]
    if is_sharp(chord_notation[:2]) or is_flat(chord_notation[:2]):
        return chord_notation[:2]
    return chord_notation[0]
