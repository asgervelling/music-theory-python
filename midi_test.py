import unittest

import midi
from exceptions import InvalidChordException


class TestMidiMethods(unittest.TestCase):

    def test_midi_chord(self):
        self.assertCountEqual(midi.chord('F-6'), [65, 68, 72, 74])
        self.assertCountEqual(midi.chord('F-Δ#11'), [65, 68, 72, 76, 79, 83])
        self.assertCountEqual(midi.chord('B9'), [71, 75, 78, 81, 85])
        self.assertCountEqual(midi.chord('C'), [60, 64, 67])
        self.assertCountEqual(midi.chord('Cmaj9'), [60, 64, 67, 71, 74])
        with self.assertRaises(InvalidChordException):
            print(midi.chord('C11'))


if __name__ == '__main__':
    unittest.main()
