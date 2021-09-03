import chords
import notes
import midi


def debug(chord_notation):
    print(f'{chord_notation}:', chords.degrees(chord_notation))


print(notes.std_name_for_note(61))

print(list(map(notes.std_name_for_note, range(60, 72))))

# print(chords.degrees('E9sus4'))
# print(chords.degrees('EMaj9'))
