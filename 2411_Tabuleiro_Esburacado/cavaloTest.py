import unittest
from cavalo import passeioCavalo


class TestCavalo(unittest.TestCase):
    def testPasseioCavalo(self):
        movimentos = [[1, 8, 5, 3, 4], [6, 8, 1]]
        results = [4, 3]

        for i in range(2):
            result = passeioCavalo(movimentos[i])
            self.assertEqual(result, results[i])


if __name__ == '__main__':
    unittest.main()
