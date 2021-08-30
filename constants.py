# prefer value[0]
synonyms = {
    'MINOR': ['m', '-'],
    'DIMINISHED': ['b5', '♭5', 'o5', 'dim5', 'dim'],
    'AUGMENTED': ['#5', '+5', '+', 'aug5', 'aug'],
    'MAJOR7': ['Δ', 'Δ7', 'maj', 'maj7', 'Maj', 'Maj7', 'M']
}


accidentals = {
    'SHARP': ['#', 'S'],
    'FLAT': ['b', '♭', 'F'],
}

chord_intervals = {
    '1': 0,
    'b2': 1,
    '2': 2,
    'b3': 3,
    'm': 3,
    '-': 3,
    '3': 4,
    '4': 5,
    '#4': 6,
    'b5': 6,
    '♭5': 6,
    'o5': 6,
    'dim5': 6,
    'dim': 6,
    '5': 7,
    '#5': 8,
    '+5': 8,
    '+': 8,
    'aug5': 8,
    'aug': 8,
    'b6': 8,
    '6': 9,
    '7': 10,
    'Δ': 11,
    'Δ7': 11,
    'maj': 11,
    'maj7': 11,
    'Maj': 11,
    'Maj7': 11,
    'M': 11,
    'b9': 13,
    '9': 14,
    '#9': 15,
    '11': 17,
    '#11': 18,
    '13': 21,
}

"""
(?P<root_note>^[A-G])(?P<minor>[m-]?)(?P<altered>(?:maj|min|m|sus|aug|dim|b5|#5)?)(?P<number>[0-9]{0,2})

(?P<root_note>^[A-G])
"""

extentions = {
    '6': 9,
    '7': 10,
    'Δ': 11,
    'Δ7': 11,
    'maj': 11,
    'Maj': 11,
    'M': 11,
    '9': 14,
    '#9': 15,
    '11': 17,
    '#11': 18,
    '13': 21,
}

alterations = {
    '#4': 6,
    'b5': 6,
    '♭5': 6,
    'o5': 6,
    'dim5': 6,
    'dim': 6,
    '5': 7,
    '#5': 8,
    '+5': 8,
    '+': 8,
    'aug5': 8,
    'aug': 8,
    'b9': 13,

}