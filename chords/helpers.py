from typing import List

from constants import chord_intervals, implications
from exceptions import InvalidChordException


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


def replace_if_exists(string: str, old, new) -> str:
    if old == None or new == None:
        return string
    return string.replace(old, new)


def implied_extensions(symbol: str) -> List[str]:
    """ If a chord contains a 13, it must contain a 7/Maj7, 9 and 11, 
        unless the chord is an added note chord """
    for key, val in implications.items():
        if key in chord_intervals.keys() and key == symbol:
            return val

    return [symbol]
