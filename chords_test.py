import unittest

from chords import degrees


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


if __name__ == '__main__':
    unittest.main()
