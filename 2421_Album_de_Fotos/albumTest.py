import unittest
from album import encontrarBrinquedo


class TestCasas(unittest.TestCase):
    def testEncontrarBrinquedo(self):
        dica = [8, 5]
        vizinhanca = [ [1, 2, 3, 5], [1, 2, 3, 5] ]
        results = [ "3 5", "2 3" ]

        for i in range(2):
            result = encontrarBrinquedo(dica[i], vizinhanca[i])
            self.assertEqual(result, results[i])


if __name__ == '__main__':
    unittest.main()
