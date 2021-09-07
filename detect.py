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

def is_add_chord(chord_symbols: List[str]) -> bool:
    """ An added tone chord is a triad with an added diatonic extension that is not 7. """
    


def sus_symbol(chord_symbols: List[str]) -> str:
    if not is_sus_chord(chord_symbols):
        return ''
    for symbol in chord_symbols:
        if symbol in ['2', '4']:
            return 'sus' + symbol
    return 'sus4'


def implied_diatonic_extensions(chord_symbols: List[str]) -> List[str]:
    print(chord_symbols)
    """ Returns the implied diatonic extensions of a chord symbol. 'Cm11' -> ['7', '9', '11'] """
    diatonic_extensions = [
        symbol for symbol in chord_symbols if symbol in constants.diatonic_extensions]

    print(diatonic_extensions)

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
    # add
    # altered_symbols

    return ''.join([
        root_note,
        sus,
        third,
        maj,
        largest_diatonic_ext
    ])
    return implied_diatonic_extensions(chord_symbols)


print(chord_notation('C', ['1', '3', '5', '7', '9', '11']))
print(chord_notation('C', ['1', 'm', '5', '7', '9', '11']))
print(chord_notation('C', ['1', '3', '5', 'maj', '9', '11']))
print(chord_notation('C', ['1', '3', '5', '9']))
