import unittest
from banco import excedeAtendimento


class TestBanco(unittest.TestCase):
    def testAtendimento(self):
        caixas = [1, 3, 3]
        clientes = [[[0, 10], [0, 10], [1, 10], [2, 10], [30, 10]],
                    [[0, 10], [0, 10], [0, 20], [2, 10]],
                    [[0, 10], [0, 10], [0, 10], [3, 10], [5, 10], [7, 10], [11, 10], [13, 10], [14, 10], [15, 10],
                     [16, 10], [17, 10], [18, 3], [19, 10], [20, 10], [23, 3]]]
        results = [1, 0, 2]

        for i in range(3):
            result = excedeAtendimento(caixas[i], clientes[i])
            self.assertEqual(results[i], result)


if __name__ == '__main__':
    unittest.main()
