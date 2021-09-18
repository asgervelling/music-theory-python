import re
from typing import List

from .constants import chord_intervals, synonyms, ERROR, a_overridden_by_b, implications
from .exceptions import InvalidChordException
from .symbols import (number_after_add, symbols_with_same_value, largest_symbol,
                      symbols_excluded_by_add, std_name_for_symbol)
from .helpers import (any_in_string, remove_any_from_string, remove_a_if_contains_b,
                      remove_equal_value_symbols, replace_if_exists, implied_extensions)
from .midi import midi_note, note_names_from_val


def clean_symbols(symbols: List[str]):
    new_symbols = symbols
    for key, val in a_overridden_by_b.items():
        new_symbols = remove_a_if_contains_b(
            new_symbols,
            key,
            *val
        )
    try:
        return list(map(
            std_name_for_symbol,
            remove_equal_value_symbols(new_symbols)))
    except KeyError as e:
        raise InvalidChordException(
            f'{ERROR}: Invalid chord symbol "{e.args[0]}"')


def without_root_note(chord_notation: str) -> str:
    try:
        return re.search(r'^[A-G](#|b|♭)?', chord_notation).group()
    except AttributeError:
        raise InvalidChordException(
            f'No root note found for "{chord_notation}"')


def intervals_from_chord_symbols(chord_symbols: List[str]) -> List[int]:
    return [chord_intervals[s] for s in chord_symbols]


def symbols_in_notation(chord_notation: str) -> List[str]:
    symbols = []

    for key in chord_intervals.keys():
        if key in chord_notation and key != '3':
            symbols.append(key)

    if is_major_chord(chord_notation):
        return clean_symbols(list(set(symbols) - set(['m', '-'])))

    if not is_minor_maj7_chord(chord_notation):
        return clean_symbols(symbols)

    return clean_symbols(symbols)


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
    chopped = remove_any_from_string(
        symbols_with_same_value(
            chord_intervals['Δ']
        ), chord_notation
    )
    if 'm' in chopped or '-' in chopped:
        return std_name_for_symbol('m')
    return std_name_for_symbol('3')


def altered_extensions(chord_notation: str) -> List[str]:
    """ Find all symbols with accidentals such as 'b9' or '(#11)' """
    captured_groups = re.findall(
        r'((#|b|♭)\d+)', without_root_note(chord_notation))
    return [i[0] for i in captured_groups]


def is_major7_chord(chord_notation: str) -> bool:
    return any_in_string(synonyms['MAJOR7'], chord_notation)


def is_sus_chord(chord_notation: str) -> bool:
    return 'sus' in chord_notation.casefold()


def is_add_chord(chord_notation: str) -> bool:
    return 'add' in chord_notation.casefold()


def has_multiple_added_tones(chord_notation: str):
    if not is_add_chord(chord_notation):
        print(f'{chord_notation} is not an add chord')
        return False
    return 'add' in chord_notation.replace('add', '', 1)


def added_tones(chord_notation: str):
    added = []
    remaining = chord_notation
    while 'add' in remaining:
        num = number_after_add(remaining)
        added.append(num)
        remaining = remaining.replace('add' + str(num), '', 1)
    return added


def is_add_number(symbol: str, chord_notation: str) -> bool:
    if symbol not in chord_notation or \
            chord_notation.index(symbol) < 4:   # Earlisest possible index is 4: 'Cadd9'
        return False
    num_index = chord_notation.index(symbol)
    return chord_notation[num_index - 3:num_index] == 'add'


def largest_non_add_symbol(chord_symbols, chord_notation):
    highest_val = 0
    largest = '1'
    for symbol in chord_symbols:
        if chord_intervals[symbol] > highest_val and \
                not is_add_number(symbol, chord_notation):
            highest_val = chord_intervals[symbol]
            largest = symbol
    return largest


def number_after_sus(chord_notation: str):
    if not is_sus_chord(chord_notation):
        return ''
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


def first_assumptions(chord_symbols: List[str], chord_notation: str) -> List[str]:
    """ Reads a chord notation and explicit (naïve) assumptions about it.
        Returns a list of symbols that needs to be edited for special cases. """

    impl_third = implied_third(chord_notation)
    impl_fifth = implied_fifth(chord_symbols)
    # impl_seventh = implied_seventh(chord_symbols)

    impl_extensions = list(set(
        implied_extensions(largest_non_add_symbol(
            chord_symbols, chord_notation))
    ))

    impl_symbols = [
        '1',
        impl_third,
        impl_fifth,
        *impl_extensions,
        *chord_symbols
    ]

    return impl_symbols


def without_thirds(chord_symbols: List[str]) -> List[str]:
    possible_thirds = synonyms['MINOR'] + ['3']
    return [s for s in chord_symbols if s not in possible_thirds]


def correct_first_assumptions(chord_symbols: List[str], chord_notation: str) -> List[str]:
    """ 'DMaj7' cannot contain '7', 'Cadd11' cannot contain '7' and '9',
        'sus' implies '4' but cannot contain '3' or 'm', etc. """

    corrected_symbols = chord_symbols

    if is_major7_chord(chord_notation):
        corrected_symbols = [ext for ext in corrected_symbols if ext != '7']

    if is_add_chord(chord_notation):
        for tone in added_tones(chord_notation):
            corrected_symbols.append(tone)

    if is_sus_chord(chord_notation):
        corrected_symbols = without_thirds(corrected_symbols)
        corrected_symbols.append(number_after_sus(chord_notation))

    return corrected_symbols


def implied_symbols(chord_notation: str) -> List[str]:
    """ Returns a list without duplicates containing the symbols in a chord """
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


def midi_chord(chord_notation: str, root_note_octave: int = 4) -> List[int]:
    try:
        degr = degrees(chord_notation)
        intervals = [chord_intervals[deg] for deg in degr]
        root = std_name_for_root(chord_notation)
        root_midi = midi_note(root, root_note_octave)
        return list(map(lambda x: x + root_midi, intervals))

    # Top level function handles the exception
    except InvalidChordException as e:
        raise e


""" Naming """


def std_name_for_root(chord_notation: str) -> str:
    """ 'A#7b9' -> 'A#' """
    name = re.search(r'^[A-G](#|b|♭)?', chord_notation)
    if name != None:
        return name.group()

    print("NO NAME")
    raise InvalidChordException(
        f'{ERROR}: Cannot find root note for chord "{chord_notation}"')


def std_name_for_interval(symbol: str) -> str:
    pass


def std_name_for_symbol(symbol: str) -> str:
    """ Choose to work with one (1) name, for cleaner functions """
    for val in synonyms.values():
        if symbol in val:
            return val[0]
    return symbol


def std_name_for_note(midi_value: int) -> str:
    """ The standard non-midi name for a note. 60 -> C (and not B#) """
    midi_note_names = note_names_from_val(midi_value, 4)
    avoid_these = ['ES', 'FF', 'BS', 'CF']
    preferred_midi_names = [
        n for n in midi_note_names if n[:2] not in avoid_these]

    name = preferred_midi_names[0]

    number = re.search(r'\d', name)
    sharp = re.search(r'(?<!^)S', name)
    flat = re.search(r'(?<!^)F', name)

    number_symbol = number.group() if number is not None else None
    sharp_symbol = sharp.group() if sharp is not None else None
    flat_symbol = flat.group() if flat is not None else None

    filtr = replace_if_exists
    return filtr(filtr(filtr(name,
                             number_symbol, ''),
                       sharp_symbol, '#'
                       ),
                 flat_symbol, 'b'
                 )
