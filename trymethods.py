import chords
import midi


def debug(chord_notation):
    print(f'{chord_notation}:', chords.degrees(chord_notation))


debug('Esus')
debug('Esus4add9')
debug('Fadd4')
debug('DMaj13')

# print(chords.degrees('E9sus4'))
# print(chords.degrees('EMaj9'))
