from midi import chord
from typing import List
from collections import OrderedDict
from functools import reduce
import re

import constants
import helpers
from exceptions import InvalidChordException


def symbols_with_same_value(value: int) -> List[str]:
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

    for key in constants.chord_intervals.keys():
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
    for val in constants.synonyms.values():
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

    try:
        return list(map(
            std_name_for_symbol,
            helpers.remove_equal_value_symbols(new_symbols)))
    except KeyError as e:
        raise InvalidChordException(
            f'{constants.ERROR}: Invalid chord symbol "{e.args[0]}"')


def intervals_from_chord_symbols(chord_symbols: List[str]) -> List[int]:
    return [constants.chord_intervals[s] for s in chord_symbols]


def altered_extentions(chord_notation: str) -> List[str]:
    """ Find all symbols with accidentals such as 'b9' or '(#11)' """
    captured_groups = re.findall(r'((#|b|♭)\d+)', chord_notation)
    return [i[0] for i in captured_groups]


def implied_extentions(symbol: str) -> List[str]:
    """ If a chord contains a 13, it must contain a 7/Maj7, 9 and 11, 
        unless the chord is an added note chord """
    implications = {
        'Δ': ['Δ'],
        'Δ7': ['Δ'],
        'maj': ['Δ'],
        'maj7': ['Δ'],
        'Maj7': ['Δ'],
        'M': ['Δ'],
        '9': ['7', '9'],
        'b9': ['7', 'b9'],
        '11': ['7', '9', '11'],
        '#11': ['7', '9', '#11'],
        '13': ['7', '9', '11', '13']
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
        return std_name_for_symbol('m')

    # Check whether 'm' for 'minor' is in the notation,
    # or if it's just the 'm' from 'maj'
    chopped = helpers.remove_any_from_string(
        symbols_with_same_value(
            constants.chord_intervals['Δ']
        ), chord_notation
    )
    if 'm' in chopped or '-' in chopped:
        return std_name_for_symbol('m')
    return std_name_for_symbol('3')


def is_major7_chord(chord_notation: str) -> bool:
    return helpers.any_in_string(constants.synonyms['MAJOR7'], chord_notation)


def is_sus_chord(chord_notation: str) -> bool:
    return 'sus' in chord_notation.casefold()


def is_add_chord(chord_notation: str) -> bool:
    return 'add' in chord_notation.casefold()


def number_after_add(chord_notation: str):
    if not is_add_chord(chord_notation):
        return None
    add_symbol = re.search(r'add\d+', chord_notation).group()  # 'add9'
    degree_added = add_symbol[3:]

    if degree_added not in constants.valid_add_numbers:
        raise InvalidChordException(
            f'{constants.ERROR}: Invalid chord symbol "add{degree_added}"')
    return degree_added


def number_after_sus(chord_notation: str):
    if not is_sus_chord(chord_notation):
        return None
    sus_num_search = re.search(r'sus\d+', chord_notation)

    # Notating a chord as 'sus' without specifiying '2' or '4'
    # defaults to '4'
    if sus_num_search == None:
        return '4'
    sus_num = sus_num_search.group()
    return sus_num[3:]


def implied_seventh(chord_notation: str):
    if is_major7_chord(chord_notation):
        return std_name_for_symbol('Maj7')


# For now, this only supports a single add-symbol
def symbols_excluded_by_add(chord_notation: str):
    degree_added = number_after_add(chord_notation)

    for i, symbol in enumerate(constants.valid_add_numbers):
        if symbol == degree_added:
            return constants.valid_add_numbers[:i] + ['7']


def largest_symbol(chord_symbols: List[str]) -> str:
    highest_val = 0
    largest = '1'
    for symbol in chord_symbols:
        if constants.chord_intervals[symbol] > highest_val:
            highest_val = constants.chord_intervals[symbol]
            largest = symbol
    return largest


def first_assumptions(chord_symbols: List[str], chord_notation: str) -> List[str]:
    """ Reads a chord notation and explicit (naïve) assumptions about it.
        Returns a list of symbols that needs to be edited for special cases. """

    impl_third = implied_third(chord_notation)
    impl_fifth = implied_fifth(chord_symbols)
    # impl_seventh = implied_seventh(chord_symbols)

    impl_extentions = list(set(
        implied_extentions(largest_symbol(chord_symbols)) +
        altered_extentions(chord_notation)
    ))

    impl_symbols = [
        '1',
        impl_third,
        impl_fifth,
        *impl_extentions,
        *chord_symbols
    ]
    return impl_symbols


def without_thirds(chord_symbols: List[str]) -> List[str]:
    possible_thirds = constants.synonyms['MINOR'] + ['3']
    return [s for s in chord_symbols if s not in possible_thirds]


def correct_first_assumptions(chord_symbols: List[str], chord_notation: str) -> List[str]:
    """ 'DMaj7' cannot contain '7', 'Cadd11' cannot contain '7' and '9',
        'sus' implies '4' but cannot contain '3' or 'm', etc. """

    corrected_symbols = chord_symbols

    if is_major7_chord(chord_notation):
        corrected_symbols = [ext for ext in corrected_symbols if ext != '7']

    if is_add_chord(chord_notation):
        excluded = symbols_excluded_by_add(chord_notation)
        corrected_symbols = [
            ext for ext in corrected_symbols if ext not in excluded]

    if is_sus_chord(chord_notation):
        corrected_symbols = without_thirds(corrected_symbols)
        corrected_symbols.append(number_after_sus(chord_notation))

    return corrected_symbols


def implied_symbols(chord_notation: str) -> List[str]:
    """ Returns a list without duplicates containing the  """
    rough_draft = symbols_in_notation(chord_notation)
    bold_assumptions = first_assumptions(
        rough_draft,
        chord_notation)

    impl_symbols = correct_first_assumptions(bold_assumptions, chord_notation)
    return list(set(impl_symbols))


def sort_degrees(degr: List[str]) -> List[str]:
    """ Sort degrees by interval size (ascending) """
    intervals = intervals_from_chord_symbols(degr)
    zipped = sorted(zip(intervals, degr))
    sorted_degrees = [deg for _, deg in zipped]
    return sorted_degrees


def degrees(chord_notation: str) -> List[str]:
    # validate_chord_notation(chord_notation)
    try:
        degr = sort_degrees(
            clean_symbols(
                implied_symbols(chord_notation)
            )
        )

        return degr
    except (InvalidChordException, KeyError) as e:
        raise InvalidChordException(e)
