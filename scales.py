from pprint import pprint

from exceptions import InvalidChordException

steps = [
    ['1', 'bb2'],
    ['b2',  '#1'],
    ['2', 'bb3',   '9'],
    ['b3',  '#2'],
    ['3',  'b4'],
    ['4',  '#3',  '11'],
    ['b5',  '#4', '#11'],
    ['5', 'bb6'],
    ['b6',  '#5'],
    ['6', 'bb7',  '13'],
    ['b7',  '#6'],
    ['7',  'b8'],
    ['8',  '#7'],
]

formulas = {
    'major': ['1', '2', '3', '4', '5', '6', '7'],
}

note_names = [
    ['B#',  'C',  'Dbb'],
    ['B##', 'C#', 'Db'],
    ['C##', 'D',  'Ebb'],
    ['D#',  'Eb', 'Fbb'],
    ['D##', 'E',  'Fb'],
    ['E#',  'F',  'Gbb'],
    ['E##', 'F#', 'Gb'],
    ['F##', 'G',  'Abb'],
    ['G#',  'Ab'],
    ['G##', 'A',  'Bbb'],
    ['A#',  'Bb', 'Cbb'],
    ['A##', 'B',  'Cb'],
]


def find_note_index(scale, search_note):
    """ Given a scale, find the index of a particular note """
    for index, note in enumerate(scale):
        # Deal with situations where we have a list of enharmonic
        # equivalents, as well as just a single note as and str.
        if type(note) == list:
            if search_note in note:
                return index
        elif type(note) == str:
            if search_note == note:
                return index
    raise InvalidChordException(f'Invalid note "{search_note}"')


def interval_between(note_a, note_b):
    index_a = find_note_index(note_names, note_a)
    index_b = find_note_index(note_names, note_b)
    index_sum = (-1 * (index_a - index_b) + 12) % 12
    print(f'{note_a} to {note_b}: {steps[index_sum][0]}')
    return steps[index_sum][0]


def rotate(scale, n):
    """ Left-rotate a scale by n positions. """
    return scale[n:] + scale[:n]


def chromatic(key):
    """ Generate a chromatic scale in a given key. """
    # Figure out how much to rotate the notes list by and return
    # the rotated version.
    num_rotations = find_note_index(note_names, key)
    return rotate(note_names, num_rotations)


def scale(key, formula=formulas['major']):
    pass
