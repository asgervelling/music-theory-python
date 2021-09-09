from midi import chord
from typing import List

import scales
import constants
import helpers
import notes


def is_triad(chord_symbols: List[str]) -> bool:
    return len(chord_symbols) == 3


def is_minor_chord(chord_symbols: List[str]) -> bool:
    return helpers.any_in_list(constants.synonyms['MINOR'], chord_symbols)


def is_major7_chord(chord_symbols: List[str]) -> bool:
    if is_triad(chord_symbols):
        return False
    return helpers.any_in_list(constants.synonyms['MAJOR7'], chord_symbols)


def is_extended_beyond_7(chord_symbols: List[str]) -> bool:
    return helpers.any_in_list(constants.extensions_beyond_7, chord_symbols)


def is_sus_chord(chord_symbols: List[str]) -> bool:
    """ A suspended chord has no third. Instead it has a perfect 4th or perfect 2nd. """
    return not helpers.any_in_list(constants.synonyms['MINOR'] + ['3'], chord_symbols) and \
        helpers.any_in_list(['2', '4'], chord_symbols)


def is_interval(semitones, symbol_a, symbol_b):
    a = constants.chord_intervals[symbol_a]
    b = constants.chord_intervals[symbol_b]
    return b - a == semitones


def is_tertian(chord_symbols: List[str]) -> bool:
    """ A tertian chord is a chord that can be decomposed into a series of thirds. """
    for i in range(len(chord_symbols) - 1):
        if not is_interval(3, chord_symbols[i], chord_symbols[i+1]) and \
                not is_interval(4, chord_symbols[i], chord_symbols[i+1]):
            return False
    return True


def non_tertian_symbols(chord_symbols: List[str]):
    non_tertian = []
    for i in range(len(chord_symbols) - 1):
        a = chord_symbols[i]
        b = chord_symbols[i+1]
        if not is_interval(3, a, b) and not is_interval(4, a, b):
            non_tertian.append(b)
    print(non_tertian)
    return non_tertian


non_tertian_symbols(['1', '3', '5', '7', '9'])
non_tertian_symbols(['1', '3', '5', '9'])
non_tertian_symbols(['1', '4', '5'])
non_tertian_symbols(['1', '3', '4', '5'])


def is_symbol_diatonic(chord_symbol: str) -> bool:
    return chord_symbol in constants.diatonic_extensions


def extentions_are_add_valid(chord_symbols: List[str]) -> bool:
    if len(chord_symbols) != 4:
        return False
    if helpers.any_in_list(['2', '4'], chord_symbols) and \
            helpers.any_in_list(constants.synonyms['MINOR'] + ['3'], chord_symbols):
        return True

    # to-do: Add symbol is not necessarily at index 3, it might be at index 1 ('2', or '4')
    return chord_symbols[3] in constants.diatonic_extensions.keys()


def is_add_chord(chord_symbols: List[str]) -> bool:
    """ 'An added tone chord, or added note chord, is a non-tertian chord 
        composed of a tertian triad and an extra "added" note. 
        The added note is not a seventh (three thirds from the chord root),
        but typically a non-tertian note, which cannot be defined by a sequence of thirds from the root,
        such as the added sixth' - WIkipedia.

        However this method will only return true if the extention
        is above the 7th degree. That's because in practice, you would
        never write Aadd6, you would just call it A6. """
    return len(chord_symbols) == 4 and \
        '7' not in chord_symbols and \
        not is_tertian(chord_symbols) and \
        extentions_are_add_valid(chord_symbols)


def sus_symbol(chord_symbols: List[str]) -> str:
    if not is_sus_chord(chord_symbols):
        return ''
    for symbol in chord_symbols:
        if symbol in ['2', '4']:
            return 'sus' + symbol
    return 'sus4'


def add_symbol(chord_symbols: List[str]):
    if not is_add_chord(chord_symbols):
        return ''
    # If it's not an add chord, it must contain exactly 4 tones
    return 'add' + chord_symbols[3]


def implied_diatonic_extensions(chord_symbols: List[str]) -> List[str]:
    """ Returns the implied diatonic extensions of a chord symbol. 'Cm11' -> ['7', '9', '11'] """
    diatonic_extensions = [
        symbol for symbol in chord_symbols if symbol in constants.diatonic_extensions]

    if is_major7_chord(chord_symbols):
        return [notes.std_name_for_symbol('Maj7')] + diatonic_extensions
    return ['7'] + diatonic_extensions


def chord_notation(root_note, chord_symbols):
    """ ('C', ['1', 'm', 'b5', '7']) -> 'Cm7b5' """

    """ 
    Anatomy of a chord:

        Root note
        Quality
        Fifth
        extensions (may be altered)

    Build the chord:

        Root note
        Maybe sus (if so, sus-number)
        Maybe minor
        Maybe Δ
        Maybe largest diatonic extension
        Maybe altered symbols

        (Append sus or add)
    """

    impl_diatonic_exts = implied_diatonic_extensions(chord_symbols)

    third = 'm' if is_minor_chord(chord_symbols) else ''
    sus = sus_symbol(chord_symbols)
    maj = notes.std_name_for_symbol(
        'Maj') if is_major7_chord(chord_symbols) else ''
    largest_diatonic_ext = impl_diatonic_exts[len(impl_diatonic_exts) - 1]
    add = add_symbol(chord_symbols)
    # altered_symbols

    return ''.join([
        root_note,
        sus,
        third,
        maj,
        add if add != '' else largest_diatonic_ext
    ])
    return implied_diatonic_extensions(chord_symbols)
