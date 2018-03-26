import unittest
from tarzan import viagemTarzan


class TestTarzan(unittest.TestCase):
    def testTarzanViaja(self):
        result = viagemTarzan([[1, 1], [6, 1], [6, 6], [11, 6]], 5)
        self.assertEqual('S', result)

    def testTarzanNaoViaja(self):
        result = viagemTarzan([[1, 1], [6, 6], [11, 6], [13, 8]], 5)
        self.assertEqual('N', result)


if __name__ == '__main__':
    unittest.main()
