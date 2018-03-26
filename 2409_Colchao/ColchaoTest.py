import unittest
from Colchao import passaPelaPorta


class TestColchao(unittest.TestCase):

    def testPassaPelaPorta(self):
        colchoes = [[25, 120, 220], [25, 205, 220], [25, 200, 220], [25, 230, 220]]
        portas = [[200, 100], [200, 100], [200, 100], [200, 100]]
        results = ["S", "N", "S", "N"]

        for i in range(3):
            result = passaPelaPorta(colchoes[i], portas[i])
            self.assertEqual(result, results[i])


if __name__ == '__main__':
    unittest.main()
