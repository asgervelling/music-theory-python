import unittest

from .midi import *


class TestMidiMethods(unittest.TestCase):

    test_tuples = [
        # (std name, octave, midi name, midi value)
        ('B#', 3, 'BS3', 60),
        ('C', 4, 'C4', 60),
        ('C#', 4, 'CS4', 61),
        ('D♭', 4, 'DF4', 61),
        ('D', 4, 'D4', 62),
        ('D#', 4, 'DS4', 63),
        ('E♭', 4, 'EF4', 63),
        ('E', 4, 'E4', 64),
        ('E#', 4, 'ES4', 65),
        ('Fb', 4, 'FF4', 64),
        ('F', 4, 'F4', 65),
        ('F#', 4, 'FS4', 66),
        ('Gb', 4, 'GF4', 66),
        ('G', 4, 'G4', 67),
        ('G#', 4, 'GS4', 68),
        ('GS', 4, 'GS4', 68),
        ('Ab', 4, 'AF4', 68),
        ('A', 4, 'A4', 69),
        ('A#', 4, 'AS4', 70),
        ('Bb', 4, 'BF4', 70),
        ('B', 4, 'B4', 71),
        ('Cb', 5, 'CF5', 71),
    ]

    def test_note_name(self):
        for t in self.test_tuples:
            self.assertEqual(note_name(t[0], t[1]), t[2])

    def test_midi_note(self):
        for t in self.test_tuples:
            self.assertEqual(midi_note(t[0], t[1]), t[3])


if __name__ == '__main__':
    unittest.main()
