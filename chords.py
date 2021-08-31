from typing import List
from collections import OrderedDict
from functools import reduce

import constants
import notes
import helpers


def symbols_with_value(value: int) -> List[str]:
    return [k for k, v in constants.chord_intervals.items() if v == value]


def is_minor_maj7_chord(chord_notation: str) -> bool:
    m_index = -1
    maj_index = -1
    if helpers.any_in_string(['m', '-'], chord_notation):
        m_index = next(
            chord_notation.index(s)
            for s in constants.synonyms['MINOR'] if s in chord_notation
        )
    if helpers.any_in_string(constants.synonyms['MAJOR7'], chord_notation):
        maj_index = next(
            chord_notation.index(s)
            for s in constants.synonyms['MAJOR7'] if s in chord_notation)

    return not m_index == -1 and \
        not maj_index == -1 and \
        m_index != maj_index


def is_major_chord(chord_notation: str) -> bool:
    if is_minor_maj7_chord(chord_notation):
        return False
    return not helpers.any_in_string(
        ['m', '-'],
        helpers.remove_any_from_string(constants.synonyms['MAJOR7'], chord_notation))


def symbols_in_notation(chord_notation: str) -> List[str]:
    symbols = []
    for key, val in constants.chord_intervals.items():
        if key in chord_notation:
            symbols.append(key)

    if is_major_chord(chord_notation):
        return clean_symbols(list(set(symbols) - set(['m', '-'])))

    if not is_minor_maj7_chord(chord_notation):
        return clean_symbols(symbols)

    return clean_symbols(symbols)


# These keys can't exist in a chord, if their values are present
a_overridden_by_b = {
    '3': ['b3', '13'],
    '5': ['b5', '♭5', 'o5', 'dim5', 'dim',
          '#5', '+5', 'aug5'],
    '6': ['b6'],
    '7': constants.synonyms['MAJOR7'],
    'M': constants.synonyms['MAJOR7'],
    '9': ['b9', '#9'],
    '11': ['#11'],
    '13': ['b13', '♭13', '#13'],
}


def std_name_for_symbol(symbol: str) -> str:
    """ Choose to work with one (1) name, for cleaner functions """
    for key, val in constants.synonyms.items():

        if symbol in val:
            return val[0]
    return symbol


def std_name_for_note(note: int) -> str:
    pass


def clean_symbols(symbols: List[str]):
    new_symbols = symbols
    for key, val in a_overridden_by_b.items():

        new_symbols = helpers.remove_a_if_contains_b(
            new_symbols,
            key,
            *val
        )

    return helpers.remove_equal_value_symbols(new_symbols)


def intervals_from_chord_symbols(chord_symbols: List[str]) -> List[int]:
    return [constants.chord_intervals[s] for s in chord_symbols]


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
        if key in constants.chord_intervals.keys() and key == symbol:
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
    chopped = helpers.remove_any_from_string(
        symbols_with_value(
            constants.chord_intervals['Δ']
        ), chord_notation
    )
    if 'm' in chopped or '-' in chopped:
        return 'b3'
    return '3'


def implied_symbols(chord_symbols: List[str], chord_notation: str) -> List[str]:
    highest_val = 0
    biggest_symbol = '1'
    for symbol in chord_symbols:
        if constants.chord_intervals[symbol] > highest_val:
            highest_val = constants.chord_intervals[symbol]
            biggest_symbol = symbol

    impl_third = implied_third(chord_notation)
    impl_fifth = implied_fifth(chord_symbols)
    impl_extentions = implied_extentions(biggest_symbol)
    impl_symbols = [
        '1', impl_third, impl_fifth,
        *impl_extentions, *chord_symbols]

    return clean_symbols(list(OrderedDict.fromkeys(impl_symbols)))


def sort_degrees(degr: List[str]) -> List[str]:
    intervals = intervals_from_chord_symbols(degr)
    zipped = sorted(zip(intervals, degr))
    sorted_degrees = [deg for _, deg in zipped]
    return sorted_degrees


def degrees(chord_notation: str) -> List[str]:
    return sort_degrees(
        list(map(
            std_name_for_symbol,
            clean_symbols(
                implied_symbols(
                    symbols_in_notation(chord_notation),
                    chord_notation
                )
            )
        ))
    )


def old_degrees(chord_notation: str) -> List[str]:
    return clean_symbols(
        implied_symbols(
            symbols_in_notation(chord_notation),
            chord_notation
        )
    )


print(degrees('A-maj9♭5'))
print(sort_degrees(degrees('A-maj9♭5')))
