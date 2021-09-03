import unittest

import chords
from exceptions import InvalidChordException


class TestChordMethods(unittest.TestCase):

    def test_degrees(self):
        self.assertCountEqual(chords.degrees('AbMaj7#11'), [
                              '1', '3', '5', 'Δ', '9', '#11'])
        self.assertCountEqual(chords.degrees('Dm6'), ['1', 'm', '5', '6'])
        self.assertCountEqual(chords.degrees('D6'), ['1', '3', '5', '6'])
        self.assertCountEqual(chords.degrees('Dm7'), ['1', 'm', '5', '7'])
        self.assertCountEqual(chords.degrees('D7'), ['1', '3', '5', '7'])
        self.assertCountEqual(chords.degrees('DΔ7'), ['1', '3', '5', 'Δ'])
        self.assertCountEqual(chords.degrees(
            'Dm9'), ['1', 'm', '5', '7', '9'])
        self.assertCountEqual(chords.degrees('D9'), ['1', '3', '5', '7', '9'])
        self.assertCountEqual(chords.degrees('Dmaj9'), [
                              '1', '3', '5', 'Δ', '9'])
        self.assertCountEqual(chords.degrees('Dmmaj9'), [
                              '1', 'm', '5', 'Δ', '9'])
        self.assertCountEqual(
            chords.degrees('DmΔ11'), ['1', 'm', '5', 'Δ', '9', '11'])
        self.assertCountEqual(chords.degrees('F#m7#9'), [
                              '1', 'm', '5', '7', '#9'])
        self.assertCountEqual(chords.degrees('EbmΔ13'), [
                              '1', 'm', '5', 'Δ', '9', '11', '13'])

        # sus functionality
        self.assertCountEqual(chords.degrees('Esus2'), ['1', '2', '5'])
        self.assertCountEqual(chords.degrees('Esus'), ['1', '4', '5'])
        self.assertCountEqual(chords.degrees(
            'Esus4add9'), ['1', '4', '5', '9'])

        with self.assertRaises(InvalidChordException):
            chords.degrees('Abmajlol9#12')
            chords.degrees('lAb7')
            chords.degrees('E#m(add4)')


if __name__ == '__main__':
    unittest.main()
