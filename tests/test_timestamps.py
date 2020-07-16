import unittest

import functions


class TestTimestamps(unittest.TestCase):
    def test_calc_timestamps(self):
        self.assertEqual(
            functions.check_timestamps(
                ["00:18:11", "00:42:23"])[1], [1091, 2543])
        self.assertEqual(functions.check_timestamps(["00:00:00"])[1], [0])

    def test_check_timestamps(self):
        self.assertTrue(
            functions.check_timestamps(
                ["00:18:11", "00:42:11", "01:23:52"])[0])
        self.assertTrue(
            functions.check_timestamps(["00:59:59", "10:59:59"])[0])
        self.assertFalse(
            functions.check_timestamps(["10:59:59", "00:59:59"])[0])
        self.assertFalse(
            functions.check_timestamps(["00:68:43"])[0])
        self.assertFalse(
            functions.check_timestamps(["00:28:34", "00:09:12", "00:39:00"])[0])


if __name__ == '__main__':
    unittest.main()
