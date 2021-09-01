import unittest

import chords
import midi
import constants
from exceptions import InvalidChordException


class TestChordMethods(unittest.TestCase):

    def test_degrees(self):
        self.assertCountEqual(chords.degrees('AbMaj7#11'), [
                              '1', '3', '5', 'Δ', '9', '#11'])
        self.assertCountEqual(chords.degrees('Dm6'), ['1', 'b3', '5', '6'])
        self.assertCountEqual(chords.degrees('D6'), ['1', '3', '5', '6'])
        self.assertCountEqual(chords.degrees('Dm7'), ['1', 'b3', '5', '7'])
        self.assertCountEqual(chords.degrees('D7'), ['1', '3', '5', '7'])
        self.assertCountEqual(chords.degrees('DΔ7'), ['1', '3', '5', 'Δ'])
        self.assertCountEqual(chords.degrees(
            'Dm9'), ['1', 'b3', '5', '7', '9'])
        self.assertCountEqual(chords.degrees('D9'), ['1', '3', '5', '7', '9'])
        self.assertCountEqual(chords.degrees('Dmaj9'), [
                              '1', '3', '5', 'Δ', '9'])
        self.assertCountEqual(chords.degrees('Dmmaj9'), [
                              '1', 'b3', '5', 'Δ', '9'])
        self.assertCountEqual(
            chords.degrees('DmΔ11'), ['1', 'b3', '5', 'Δ', '9', '11'])
        self.assertCountEqual(chords.degrees('F#m7#9'), [
                              '1', 'b3', '5', '7', '#9'])
        self.assertCountEqual(chords.degrees('EbmΔ13'), [
                              '1', 'b3', '5', 'Δ', '9', '11', '13'])

        with self.assertRaises(InvalidChordException):
            chords.degrees('Abmajlol9#12')
            chords.degrees('lAb7')
            chords.degrees('E#m(add4)')

    def test_midi_chord(self):
        self.assertCountEqual(midi.chord('F-6'), [65, 68, 72, 74])
        self.assertCountEqual(midi.chord('F-Δ#11'), [65, 68, 72, 76, 79, 83])
        self.assertCountEqual(midi.chord('B9'), [71, 75, 78, 81, 85])
        self.assertCountEqual(midi.chord('C'), [60, 64, 67])
        self.assertCountEqual(midi.chord('Cmaj9'), [60, 64, 67, 71, 74])


if __name__ == '__main__':
    unittest.main()
