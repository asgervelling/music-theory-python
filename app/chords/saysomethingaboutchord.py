from .notation import is_add_chord, is_minor_maj7_chord, is_major7_chord, is_sus_chord


def say_something_about_chord(chord_notation: str):
    statements = []
    if is_major7_chord(chord_notation):
        if is_minor_maj7_chord(chord_notation):
            statements.append('mMaj7')
        else:
            statements.append('Maj7')
    if is_sus_chord(chord_notation):
        statements.append('sus')
    if is_add_chord(chord_notation):
        statements.append('add')

    print(f'{chord_notation} is all of these things:\n' +
          ' '.join(statements))


say_something_about_chord('Ammaj9add13')
