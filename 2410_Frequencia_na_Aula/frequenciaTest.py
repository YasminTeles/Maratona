import unittest
from frequencia import presenteNaAula


class TestFrequencia(unittest.TestCase):
    def testPresenteNaAula(self):
        registros = [[2, 3, 1], [0, 5, 12, 41, 7, 5, 41]]
        results = [3, 5]

        for i in range(2):
            result = presenteNaAula(registros[i])
            self.assertEqual(result, results[i])


if __name__ == '__main__':
    unittest.main()
