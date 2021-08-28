from typing import List
from collections import OrderedDict

from symbols import chord_intervals


class Chord():

    def __init__(self, root_note: int, degrees: List[int]) -> None:
        self.root_note = root_note
        self.degrees = degrees


def is_minor_maj7_chord(chord_notation: str):
    m_index = -1
    maj_index = -1
    if 'm' in chord_notation:
        m_index = chord_notation.index('m')
    if 'maj' in chord_notation:
        maj_index = chord_notation.index('maj')
    return not m_index == -1 and \
        not maj_index == -1 and \
        m_index != maj_index


def symbols_in_chord(chord_notation: str):
    symbols = []
    for key, val in chord_intervals.items():
        if key in chord_notation:
            symbols.append(key)

    return symbols


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
    '5': ['b5', '♭5', 'o5', 'dim5', 'dim',
          '#5', '+5', 'aug5'],
    '7': ['Δ', 'Δ7', 'maj', 'Maj', 'M'],
    'M': ['Δ', 'Δ7', 'maj', 'Maj'],
    '9': ['b9', '#9'],
    '11': ['#11'],
    '6': ['b6']
}


def clean_symbols(symbols: List[str]):
    new_symbols = symbols
    for key, val in a_overridden_by_b.items():
        new_symbols = remove_a_if_contains_b(
            new_symbols,
            key,
            *val
        )
    return new_symbols


def intervals_from_chord_symbols(chord_symbols: List[str]):
    return [chord_intervals[s] for s in chord_symbols]


def remove_contradictory_symbols(chord_symbols: List[str]):
    """ to-do: Remove '7' if 'Δ' or 'Maj' is present, and so on """
    pass


def implied_extentions(symbol: str):
    implications = {
        'Δ': ['Δ'],
        'Δ7': ['Δ'],
        'maj7': ['Δ'],
        'Maj7': ['Δ'],
        'M': ['Δ'],
        '9': ['7', '9'],
        'b9': ['7', 'b9'],
        '11': ['9'],
        '#11': ['9']
    }
    for key, val in implications.items():
        if key in chord_intervals.keys() and key == symbol:
            return clean_symbols(val)
    return symbol


def implied_fifth(chord_symbols: List[str]):
    altered_fifths = ['b5', '♭5',
                      'o5', 'dim5', 'dim',
                      '5', '#5', '+5',
                      '+', 'aug5', 'aug']
    for symbol in chord_symbols:
        if symbol in altered_fifths:
            return symbol
    return '5'


def implied_third(chord_symbols: List[str]):
    # to-do: Instead of 'maj' or 'Maj7' here and there,
    # create a set of constants to use in all functions.
    print("All: ", chord_symbols)
    if 'maj' in chord_symbols:
        print(chord_symbols)
        print("her", list(set(chord_symbols) - set(['maj'])))
        if 'm' in list(set(chord_symbols) - set(['maj'])):
            return 'b3'
        return '3'
    if '-' in chord_symbols:
        return 'b3'
    if 'm' in chord_symbols:
        return 'b3'
    return '3'


def implied_symbols(chord_symbols: List[str]):
    highest_val = 0
    biggest_symbol = '1'
    for symbol in chord_symbols:
        if chord_intervals[symbol] > highest_val:
            highest_val = chord_intervals[symbol]
            biggest_symbol = symbol

    impl_third = implied_third(chord_symbols)
    impl_fifth = implied_fifth(chord_symbols)
    impl_extentions = implied_extentions(biggest_symbol)
    impl_symbols = [
        '1', impl_third, impl_fifth,
        *impl_extentions, *chord_symbols]

    return clean_symbols(list(OrderedDict.fromkeys(impl_symbols)))


"""
print('Am7b5', clean_symbols(symbols_in_chord('Am7b5')))
print('Daug5', clean_symbols(symbols_in_chord('Daug5')))
print('AMaj7#11', clean_symbols(symbols_in_chord('AMaj7#11')))
print('EbΔ7', clean_symbols(symbols_in_chord('EbΔ7')))
print('Eb-7b9', clean_symbols(symbols_in_chord('Eb-7b9')))
print()
"""


def degrees(chord_notation: str):
    return remove_equal_value_symbols(
        implied_symbols(
            clean_symbols(
                symbols_in_chord(chord_notation)
            )
        )
    )


print(degrees('Dmaj9'))

"""
# Flats and sharps after the root note don't yet work.
print('Abm7b5', degrees('Am7b5'))
print('D9', degrees('D9'))
print('BΔ9', degrees('BΔ9'))
print('AbMaj7#11', degrees('AbMaj7#11'))
"""
