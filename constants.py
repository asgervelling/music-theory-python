ERROR = 'ERROR'
OK = 'OK'

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
    '♭6': 8,
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
    '♭9': 13,
    '9': 14,
    '#9': 15,
    '11': 17,
    '#11': 18,
    'b13': 20,
    '♭13': 20,
    '13': 21,
    '#13': 22,
}

valid_chord_symbols = ['m', '-', '4',
                       '#4', 'b5', '♭5', 'o5', 'dim5', 'dim', '5',
                       '#5', '+5', '+', 'aug5', 'aug', 'b6', '6',
                       '7', 'Δ', 'Δ7', 'maj', 'maj7', 'Maj', 'Maj7', 'M',
                       'b9', '9', '#9', '#11', '11', '♭13', 'b13', '13', '#13']

common_note_names = {
    'C': 12,
    'C#': 13,
    'Db': 13,
    'D': 14,
    'D#': 15,
    'Eb': 15,
    'E': 16,
    'E#': 17,
    'Fb': 16,
    'F': 17,
    'F#': 18,
    'Gb': 18,
    'G': 19,
    'G#': 20,
    'Ab': 20,
    'A': 21,
    'A#': 22,
    'Bb': 22,
    'B': 23,
    'B#': 24,
}

# Pitch constants
# https://jythonmusic.me/api/midi-constants/pitch/
midi_notes = {
    'C_1': 0,
    'CS_1': 1,
    'DF_1': 1,
    'D_1': 2,
    'DS_1': 3,
    'EF_1': 3,
    'E_1': 4,
    'ES_1': 5,
    'FF_1': 4,
    'F_1': 5,
    'FS_1': 6,
    'GF_1': 6,
    'G_1': 7,
    'GS_1': 8,
    'AF_1': 8,
    'A_1': 9,
    'AS_1': 10,
    'BF_1': 10,
    'B_1': 11,
    'BS_1': 12,
    'CF0': 11,
    'C0': 12,
    'CS0': 13,
    'DF0': 13,
    'D0': 14,
    'DS0': 15,
    'EF0': 15,
    'E0': 16,
    'ES0': 17,
    'FF0': 16,
    'F0': 17,
    'FS0': 18,
    'GF0': 18,
    'G0': 19,
    'GS0': 20,
    'AF0': 20,
    'A0': 21,
    'AS0': 22,
    'BF0': 22,
    'B0': 23,
    'BS0': 24,
    'CF1': 23,
    'C1': 24,
    'CS1': 25,
    'DF1': 25,
    'D1': 26,
    'DS1': 27,
    'EF1': 27,
    'E1': 28,
    'ES1': 29,
    'FF1': 28,
    'F1': 29,
    'FS1': 30,
    'GF1': 30,
    'G1': 31,
    'GS1': 32,
    'AF1': 32,
    'A1': 33,
    'AS1': 34,
    'BF1': 34,
    'B1': 35,
    'BS1': 36,
    'CF2': 35,
    'C2': 36,
    'CS2': 37,
    'DF2': 37,
    'D2': 38,
    'DS2': 39,
    'EF2': 39,
    'E2': 40,
    'ES2': 41,
    'FF2': 40,
    'F2': 41,
    'FS2': 42,
    'GF2': 42,
    'G2': 43,
    'GS2': 44,
    'AF2': 44,
    'A2': 45,
    'AS2': 46,
    'BF2': 46,
    'B2': 47,
    'BS2': 48,
    'CF3': 47,
    'C3': 48,
    'CS3': 49,
    'DF3': 49,
    'D3': 50,
    'DS3': 51,
    'EF3': 51,
    'E3': 52,
    'ES3': 53,
    'FF3': 52,
    'F3': 53,
    'FS3': 54,
    'GF3': 54,
    'G3': 55,
    'GS3': 56,
    'AF3': 56,
    'A3': 57,
    'AS3': 58,
    'BF3': 58,
    'B3': 59,
    'BS3': 60,
    'CF4': 59,
    'C4': 60,
    'CS4': 61,
    'DF4': 61,
    'D4': 62,
    'DS4': 63,
    'EF4': 63,
    'E4': 64,
    'ES4': 65,
    'FF4': 64,
    'F4': 65,
    'FS4': 66,
    'GF4': 66,
    'G4': 67,
    'GS4': 68,
    'AF4': 68,
    'A4': 69,
    'AS4': 70,
    'BF4': 70,
    'B4': 71,
    'BS4': 72,
    'CF5': 71,
    'C5': 72,
    'CS5': 73,
    'DF5': 73,
    'D5': 74,
    'DS5': 75,
    'EF5': 75,
    'E5': 76,
    'ES5': 77,
    'FF5': 76,
    'F5': 77,
    'FS5': 78,
    'GF5': 78,
    'G5': 79,
    'GS5': 80,
    'AF5': 80,
    'A5': 81,
    'AS5': 82,
    'BF5': 82,
    'B5': 83,
    'BS5': 84,
    'CF6': 83,
    'C6': 84,
    'CS6': 85,
    'DF6': 85,
    'D6': 86,
    'DS6': 87,
    'EF6': 87,
    'E6': 88,
    'ES6': 89,
    'FF6': 88,
    'F6': 89,
    'FS6': 90,
    'GF6': 90,
    'G6': 91,
    'GS6': 92,
    'AF6': 92,
    'A6': 93,
    'AS6': 94,
    'BF6': 94,
    'B6': 95,
    'BS6': 96,
    'CF7': 95,
    'C7': 96,
    'CS7': 97,
    'DF7': 97,
    'D7': 98,
    'DS7': 99,
    'EF7': 99,
    'E7': 100,
    'ES7': 101,
    'FF7': 100,
    'F7': 101,
    'FS7': 102,
    'GF7': 102,
    'G7': 103,
    'GS7': 104,
    'AF7': 104,
    'A7': 105,
    'AS7': 106,
    'BF7': 106,
    'B7': 107,
    'BS7': 108,
    'CF8': 107,
    'C8': 108,
    'CS8': 109,
    'DF8': 109,
    'D8': 110,
    'DS8': 111,
    'EF8': 111,
    'E8': 112,
    'ES8': 113,
    'FF8': 112,
    'F8': 113,
    'FS8': 114,
    'GF8': 114,
    'G8': 115,
    'GS8': 116,
    'AF8': 116,
    'A8': 117,
    'AS8': 118,
    'BF8': 118,
    'B8': 119,
    'BS8': 120,
    'CF9': 119,
    'C9': 120,
    'CS9': 121,
    'DF9': 121,
    'D9': 122,
    'DS9': 123,
    'EF9': 123,
    'E9': 124,
    'ES9': 125,
    'FF9': 124,
    'F9': 125,
    'FS9': 126,
    'GF9': 126,
    'G9': 127,
}
