import unittest

from detect import *


class TestDetectMethods(unittest.TestCase):

    def test_is_minor_chord(self):
        self.assertTrue(is_minor_chord(['1', 'm', '5', '6']))
        self.assertTrue(is_minor_chord(['1', 'b3', 'b5']))
        self.assertFalse(is_minor_chord(['1', '4', '5']))
        self.assertFalse(is_minor_chord(['1', '3', '5']))

    def test_is_triad(self):
        self.assertTrue(is_triad(['1', '3', '5']))
        self.assertFalse(is_triad(['1', '2', '3', '4']))

    def test_is_major7_chord(self):
        self.assertTrue(is_major7_chord(['1', '3', '5', 'Δ']))
        self.assertTrue(is_major7_chord(['1', 'm', '5', 'Δ', '9', '11']))
        self.assertFalse(is_major7_chord(['1', '3', '5', '6']))
        self.assertFalse(is_major7_chord(['1', '3', '5', '7']))

    def test_is_extended_beyond_7(self):
        self.assertTrue(is_extended_beyond_7(['1', 'm', '5', 'Δ', '9', '11']))
        self.assertTrue(is_extended_beyond_7(['1', '3', '5', '9']))
        self.assertTrue(is_extended_beyond_7(['b9']))
        self.assertFalse(is_extended_beyond_7(['1', '3', '5', '7']))
        self.assertFalse(is_extended_beyond_7(['7']))

    def test_is_sus_chord(self):
        self.assertTrue(is_sus_chord(['1', '2', '5', '7']))
        self.assertTrue(is_sus_chord(['1', '4', '5']))
        self.assertFalse(is_sus_chord(['1', '5', '6']))
        self.assertFalse(is_sus_chord(['1', '5']))

    def test_sus_number(self):
        self.assertEqual(sus_symbol(['1', '2', '5', '7']), 'sus2')
        self.assertEqual(sus_symbol(['1', '4', '5']), 'sus4')
        self.assertEqual(sus_symbol(['1', '3', '5']), '')


if __name__ == '__main__':
    unittest.main()
