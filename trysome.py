import chords


print(chords.degrees('E9'))         # ['1', '3', '5', '7', '9']
print(chords.degrees('Fmaj#11'))    # ['1', '3', '5', 'Δ', '9', '#11']
print(chords.midi_chord('Fmaj#11'))  # [65, 69, 72, 76, 79, 83]

print(chords.degrees('F♯7sus4'))
