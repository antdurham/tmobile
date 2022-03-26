import unittest
import cap


class TestCap(unittest.TestCase):

    def test_hello_world(self):
        text = 'Hello World!'
        result = cap.cap_text(text)
        self.assertEqual(result, 'HELLO WORLD!')



if __name__ == '__main__':
    unittest.main()
