import unittest

from .notation import *
from .exceptions import InvalidChordException


class TestNotationMethods(unittest.TestCase):

    def test_degrees(self):
        self.assertCountEqual(degrees('Am'), ['1', 'm', '5'])
        self.assertCountEqual(degrees('Cmadd4'), ['1', 'm', '4', '5'])
        self.assertCountEqual(degrees('Gbmaj7#13sus2'), [
            '1', '2', '5', 'Δ', '9', '11', '#13'])

        # Added tone chords
        self.assertCountEqual(degrees('C#add4'), ['1', '3', '4', '5'])
        self.assertCountEqual(degrees('Badd4add9'), ['1', '3', '4', '5', '9'])
        self.assertCountEqual(degrees('Am9add13'), [
                              '1', 'm', '5', '7', '9', '13'])
        with self.assertRaises(InvalidChordException):
            print(degrees('Cadd1'))
            print(degrees('Cadd3'))
            print(degrees('Cadd4add1'))
            print(degrees('Cadd5'))
            print(degrees('Cadd6'))
            print(degrees('Cadd7'))
            print(degrees('Cadd8'))
            print(degrees('Cadd10'))
            print(degrees('Cadd12'))


if __name__ == '__main__':
    unittest.main()
