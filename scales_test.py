import unittest

import scales


class TestScales(unittest.TestCase):

    def test_interval_between_notes(self):
        self.assertEqual(scales.interval_between_notes('C', 'E'), '3')
        self.assertEqual(scales.interval_between_notes('Db', 'C'), '7')
        self.assertEqual(scales.interval_between_notes('G', 'F'), 'b7')
        self.assertEqual(scales.interval_between_notes('D', 'G'), '4')


if __name__ == '__main__':
    unittest.main()
