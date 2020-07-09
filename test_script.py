# These are unit tests that will check to make sure that videos 
# are downloaded and deleted properly. Will check for conversion 
# later.

import unittest
import script

class TestVideoDownload(unittest.TestCase):

    def test_link_retrieval(self):
        self.assertEqual(script.download_vid("https://www.youtube.com/watch?v=Z_9nfYT3QyQ&t=1s"), 
        "https://www.youtube.com/watch?v=Z_9nfYT3QyQ&t=1s")
        self.assertFalse(script.download_vid("https://www.youtube.com/watch?v=Z_9nfYT3QyQ&t=1s"),
        "https://www.youtube.com/watch?v=Z_9nfYT3")

    if __name__ == '__main__':
        unittest.main()