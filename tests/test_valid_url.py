import unittest

import functions


class MyTestCase(unittest.TestCase):
    def test_valid_url(self):
        self.assertTrue(functions.valid_url(
            "https://www.youtube.com/watch?v=Z_9nfYT3QyQ&t=146s"))
        self.assertTrue(functions.valid_url(
            "https://www.youtube.com/watch?v=9XFcFXdVIfk&t=1346s"))
        self.assertTrue(functions.valid_url(
            "https://www.youtube.com/watch?v=aYgeh-k18Tc"))
        self.assertFalse(functions.valid_url(
            "https://www.youtube.com/watch?v"))
        self.assertFalse(functions.valid_url(
            "https://www.youtube.com/watch?v=aYgeh"))


if __name__ == '__main__':
    unittest.main()
