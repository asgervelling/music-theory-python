import unittest

import scales


class TestScales(unittest.TestCase):

    def test_interval_between(self):
        self.assertEqual(scales.interval_between('C', 'E'), '3')
        self.assertEqual(scales.interval_between('Db', 'C'), '7')
        self.assertEqual(scales.interval_between('G', 'F'), 'b7')
        self.assertEqual(scales.interval_between('D', 'G'), '4')


if __name__ == '__main__':
    unittest.main()
