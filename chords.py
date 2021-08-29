from typing import List
from collections import OrderedDict
from functools import reduce

from symbols import chord_intervals, synonyms, accidentals
from notes import notes


def root_note(chord_notation: str):
    if len(chord_notation) < 2:
        return chord_notation[0]
    if is_sharp(chord_notation[:2]) or is_flat(chord_notation[:2]):
        return chord_notation[:2]
    return chord_notation[0]


def remove_any_from_string(substrings: List[str], string: str) -> str:
    new_string = string
    for substring in substrings:
        if substring in string:
            new_string = string.replace(substring, '')
    return new_string


def any_in_string(items: List[str], string: str) -> bool:
    for item in items:
        if item in string:
            return True
    return False


def any_in_list(items: List[str], lst: List[str]) -> bool:
    for item_a in items:
        for item_b in lst:
            if item_a == item_b:
                return True
    return False


def symbols_with_value(value: int) -> List[str]:
    return [k for k, v in chord_intervals.items() if v == value]


def is_sharp(note: str) -> bool:
    if len(note) < 2:
        return False
    return note[1] in accidentals['SHARP']


def is_flat(note: str) -> bool:
    if len(note) < 2:
        return False
    return note[1] in accidentals['FLAT']


def is_minor_maj7_chord(chord_notation: str) -> bool:
    m_index = -1
    maj_index = -1
    if any_in_string(['m', '-'], chord_notation):
        m_index = next(
            chord_notation.index(s)
            for s in synonyms['MINOR'] if s in chord_notation
        )
    if any_in_string(synonyms['MAJOR7'], chord_notation):
        maj_index = next(
            chord_notation.index(s)
            for s in synonyms['MAJOR7'] if s in chord_notation)

    return not m_index == -1 and \
        not maj_index == -1 and \
        m_index != maj_index


def is_major_chord(chord_notation: str) -> bool:
    if is_minor_maj7_chord(chord_notation):
        return False
    return not any_in_string(
        ['m', '-'],
        remove_any_from_string(synonyms['MAJOR7'], chord_notation))


def symbols_in_chord(chord_notation: str) -> List[str]:
    symbols = []
    for key, val in chord_intervals.items():
        if key in chord_notation:
            symbols.append(key)

    if is_major_chord(chord_notation):
        return clean_symbols(list(set(symbols) - set(['m', '-'])))

    if not is_minor_maj7_chord(chord_notation):
        return clean_symbols(symbols)

    return clean_symbols(symbols)


def remove_a_if_contains_b(items, a, b, *b_variations):
    new_list = items
    if a in new_list and b in new_list:
        new_list.remove(a)
    if b_variations:
        for variation in b_variations:
            if a in new_list and variation in new_list:
                new_list.remove(a)
    return new_list


def remove_equal_value_symbols(symbols: List[str]):
    found_values = []
    new_symbols = []
    for symbol in symbols:
        if chord_intervals[symbol] not in found_values:
            found_values.append(chord_intervals[symbol])
            new_symbols.append(symbol)
    return new_symbols


# These keys can't exist in a chord, if their values are present
a_overridden_by_b = {
    '3': ['b3', '13'],
    '5': ['b5', '♭5', 'o5', 'dim5', 'dim',
          '#5', '+5', 'aug5'],
    '6': ['b6'],
    '7': synonyms['MAJOR7'],
    'M': synonyms['MAJOR7'],
    '9': ['b9', '#9'],
    '11': ['#11'],
}


def clean_symbols(symbols: List[str]):
    new_symbols = symbols
    for key, val in a_overridden_by_b.items():
        new_symbols = remove_a_if_contains_b(
            new_symbols,
            key,
            *val
        )
    return remove_equal_value_symbols(new_symbols)


def intervals_from_chord_symbols(chord_symbols: List[str]):
    return [chord_intervals[s] for s in chord_symbols]


def remove_contradictory_symbols(chord_symbols: List[str]):
    """ to-do: Remove '7' if 'Δ' or 'Maj' is present, and so on """
    pass


def implied_extentions(symbol: str) -> List[str]:
    implications = {
        'Δ': ['Δ'],
        'Δ7': ['Δ'],
        'maj7': ['Δ'],
        'Maj7': ['Δ'],
        'M': ['Δ'],
        '9': ['7', '9'],
        'b9': ['7', 'b9'],
        '11': ['9', '11'],
        '#11': ['9', '#11'],
        '13': ['9', '11', '13']
    }
    for key, val in implications.items():
        if key in chord_intervals.keys() and key == symbol:
            return clean_symbols(val)

    return [symbol]


def implied_fifth(chord_symbols: List[str]):
    altered_fifths = ['b5', '♭5',
                      'o5', 'dim5', 'dim',
                      '5', '#5', '+5',
                      '+', 'aug5', 'aug']
    for symbol in chord_symbols:
        if symbol in altered_fifths:
            return symbol
    return '5'


def implied_third(chord_notation: str):
    if is_minor_maj7_chord(chord_notation):
        return 'b3'
    chopped = remove_any_from_string(
        symbols_with_value(
            chord_intervals['Δ']
        ), chord_notation
    )
    if 'm' in chopped or '-' in chopped:
        return 'b3'
    return '3'


def implied_symbols(chord_symbols: List[str], chord_notation: str) -> List[str]:
    highest_val = 0
    biggest_symbol = '1'
    for symbol in chord_symbols:
        if chord_intervals[symbol] > highest_val:
            highest_val = chord_intervals[symbol]
            biggest_symbol = symbol

    impl_third = implied_third(chord_notation)
    impl_fifth = implied_fifth(chord_symbols)
    impl_extentions = implied_extentions(biggest_symbol)
    impl_symbols = [
        '1', impl_third, impl_fifth,
        *impl_extentions, *chord_symbols]

    return clean_symbols(list(OrderedDict.fromkeys(impl_symbols)))


def degrees(chord_notation: str):
    return clean_symbols(
        implied_symbols(
            symbols_in_chord(chord_notation),
            chord_notation
        )
    )


"""
MIDI
"""


def with_midi_accidental_name(note: str) -> str:
    if is_sharp(note):
        return note[0] + 'S'
    if is_flat(note):
        return note[0] + 'F'
    return note


def midi_note_name(note: str, octave: int):
    return f'{with_midi_accidental_name(note).upper()}{octave}'


def midi_note_name_from_val(note_val: int, octave: int):
    for key, val in chord_intervals.items():
        if val == note_val:
            print(val)
            return midi_note_name(key, octave)
    return None


def midi_note_name_in_octave(note: str, octave: int):
    return note + str(octave)


def midi_note(note, octave: int) -> int:
    if type(note) == int:
        return notes[midi_note_name_in_octave(note, octave)]
    return notes[midi_note_name(note, octave)]


def midi_chord(chord_notation: str, root_note_octave: int = 4) -> List[int]:
    degr = degrees(chord_notation)
    intervals = [chord_intervals[deg] for deg in degr]
    root = root_note(chord_notation)
    root_midi = midi_note(root, root_note_octave)
    return list(map(lambda x: x + root_midi, intervals))
