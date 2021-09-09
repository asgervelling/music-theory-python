import re
from typing import List

from .constants import chord_intervals, synonyms, ERROR, valid_add_numbers
from .exceptions import InvalidChordException
from .detect import is_add_chord


def symbols_with_same_value(value: int) -> List[str]:
    return [k for k, v in chord_intervals.items() if v == value]


def std_name_for_symbol(symbol: str) -> str:
    """ Choose to work with one (1) name, for cleaner functions """
    for val in synonyms.values():
        if symbol in val:
            return val[0]
    return symbol


def number_after_add(chord_notation: str):
    if not is_add_chord(chord_notation):
        return ''
    add_symbol = re.search(r'add\d+', chord_notation).group()  # 'add9'
    degree_added = add_symbol[3:]

    if degree_added not in valid_add_numbers:
        raise InvalidChordException(
            f'{ERROR}: Invalid chord symbol "add{degree_added}"')
    return degree_added


def symbols_excluded_by_add(chord_notation: str):
    degree_added = number_after_add(chord_notation)

    for i, symbol in enumerate(valid_add_numbers):
        if symbol == degree_added:
            return valid_add_numbers[:i] + ['7']


def largest_symbol(chord_symbols: List[str]) -> str:
    highest_val = 0
    largest = '1'
    for symbol in chord_symbols:
        if chord_intervals[symbol] > highest_val:
            highest_val = chord_intervals[symbol]
            largest = symbol
    return largest
