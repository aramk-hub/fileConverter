import unittest

import functions


class MyTestCase(unittest.TestCase):
    def test_calc_timestamps(self):
        self.assertEqual(
            functions.calc_timestamps(["00:18:11", "00:42:23"]), [1091, 2543])
        self.assertEqual(functions.calc_timestamps(["00:00:00"]), [0])


if __name__ == '__main__':
    unittest.main()
