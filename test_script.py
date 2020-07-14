import unittest
import script


class MyTestCase(unittest.TestCase):
    def test_valid_url(self):
        self.assertEqual(script.valid_url("https://www.youtube.com/watch?v=jq824hrfCuc&t=2225s"), True)
        self.assertEqual(script.valid_url("https://www.youtube.com/watch?v=oJN_NV6rRnI"), True)


if __name__ == '__main__':
    unittest.main()
