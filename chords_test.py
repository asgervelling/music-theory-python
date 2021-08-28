import unittest

from chords import degrees


class TestChordMethods(unittest.TestCase):

    def test_degrees(self):
        self.assertEqual(degrees('AbMaj7#11'), [
                         '1', '3', '5', '9', 'Maj', '#11'])
        self.assertEqual(degrees('Dm6'), ['1', 'b3', '5', '6'])
        self.assertEqual(degrees('D6'), ['1', '3', '5', '6'])
        self.assertEqual(degrees('Dm7'), ['1', 'b3', '5', '7'])
        self.assertEqual(degrees('D7'), ['1', '3', '5', '7'])
        self.assertEqual(degrees('DΔ7'), ['1', '3', '5', 'Δ'])
        self.assertEqual(degrees('Dm9'), ['1', 'b3', '5', '7', '9'])
        self.assertEqual(degrees('D9'), ['1', '3', '5', '7', '9'])
        self.assertEqual(degrees('Dmaj9'), ['1', '3', '5', 'maj', '9'])


if __name__ == '__main__':
    unittest.main()
