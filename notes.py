import re

import constants
import midi
import helpers


def is_sharp(note: str) -> bool:
    if len(note) < 2:
        return False
    return note[1] in constants.accidentals['SHARP']


def is_flat(note: str) -> bool:
    if len(note) < 2:
        return False
    return note[1] in constants.accidentals['FLAT']


def root_note_std_name(chord_notation: str) -> str:
    """ 'A#7b9' -> 'A#' """
    return re.search(r'^[A-G](#|b|♭)?', chord_notation).group()


def std_name_for_symbol(symbol: str) -> str:
    """ Choose to work with one (1) name, for cleaner functions """
    for val in constants.synonyms.values():
        if symbol in val:
            return val[0]
    return symbol


def std_name_for_note(midi_value: int) -> str:
    """ The standard non-midi name for a note. 60 -> C (and not B#) """
    midi_notes = midi.note_names_from_val(midi_value, 4)
    avoid_these = ['ES', 'FF', 'BS', 'CF']
    preferred_midi_names = [n for n in midi_notes if n[:2] not in avoid_these]

    """
    if len(preferred_midi_names) > 1:
        print(
            'WARNING: More than one accepted standard name for note with value ', midi_value)
        print(preferred_midi_names)
    """
    # to do: Choose between sharps and flats

    name = preferred_midi_names[0]

    number = re.search(r'\d', name)
    sharp = re.search(r'(?<!^)S', name)
    flat = re.search(r'(?<!^)F', name)

    number_symbol = number.group() if number is not None else None
    sharp_symbol = sharp.group() if sharp is not None else None
    flat_symbol = flat.group() if flat is not None else None

    filtr = helpers.replace_if_exists
    return filtr(filtr(filtr(name,
                             number_symbol, ''),
                       sharp_symbol, '#'
                       ),
                 flat_symbol, 'b'
                 )
