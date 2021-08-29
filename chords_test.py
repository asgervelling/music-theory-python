import unittest

from chords import degrees, midi_chord


class TestChordMethods(unittest.TestCase):

    def test_degrees(self):
        self.assertCountEqual(degrees('AbMaj7#11'), [
                              '1', '3', '5', '9', 'Maj7', '#11'])
        self.assertCountEqual(degrees('Dm6'), ['1', 'b3', '5', '6'])
        self.assertCountEqual(degrees('D6'), ['1', '3', '5', '6'])
        self.assertCountEqual(degrees('Dm7'), ['1', 'b3', '5', '7'])
        self.assertCountEqual(degrees('D7'), ['1', '3', '5', '7'])
        self.assertCountEqual(degrees('DΔ7'), ['1', '3', '5', 'Δ'])
        self.assertCountEqual(degrees('Dm9'), ['1', 'b3', '5', '7', '9'])
        self.assertCountEqual(degrees('D9'), ['1', '3', '5', '7', '9'])
        self.assertCountEqual(degrees('Dmaj9'), ['1', '3', '5', 'maj', '9'])
        self.assertCountEqual(degrees('Dmmaj9'), ['1', 'b3', '5', 'maj', '9'])
        self.assertCountEqual(
            degrees('DmΔ11'), ['1', 'b3', '5', 'Δ', '9', '11'])
        self.assertCountEqual(degrees('F#m7#9'), ['1', 'b3', '5', '7', '#9'])
        self.assertCountEqual(degrees('EbmΔ13'), [
                              '1', 'b3', '5', 'Δ', '9', '11', '13'])

    def test_midi_chord(self):
        self.assertCountEqual(midi_chord('F-6'), [65, 68, 72, 74])
        self.assertCountEqual(midi_chord('F-Δ#11'), [65, 68, 72, 76, 79, 83])
        self.assertCountEqual(midi_chord('B9'), [71, 75, 78, 81, 85])
        self.assertCountEqual(midi_chord('C'), [60, 64, 67])
        self.assertCountEqual(midi_chord('Cmaj9'), [60, 64, 67, 71, 74])


if __name__ == '__main__':
    unittest.main()
