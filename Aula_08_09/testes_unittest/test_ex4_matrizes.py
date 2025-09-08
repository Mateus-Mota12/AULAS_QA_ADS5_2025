import unittest
from ex4_matrizes import multiply_matrices, identity

class TestMatrizes(unittest.TestCase):
    def test_multiplicacao_basica(self):
        A = [[1, 2], [3, 4]]
        B = [[0, 1], [1, 0]]
        self.assertEqual(multiply_matrices(A, B), [[2, 1], [4, 3]])

    def test_identidade(self):
        A = [[2, -1], [0, 3]]
        I = identity(2)
        
        self.assertEqual(multiply_matrices(A, I), A)
        self.assertEqual(multiply_matrices(I, A), A)

    def test_associatividade(self):
        A = [[1, 2], [3, 4]]
        B = [[0, 1], [1, 0]]
        C = [[2, 0], [0, 2]]
        left = multiply_matrices(multiply_matrices(A, B), C)
        right = multiply_matrices(A, multiply_matrices(B, C))
        self.assertEqual(left, right)

    def test_erros(self):
        with self.assertRaises(ValueError):
            multiply_matrices([], [[1]])
        with self.assertRaises(ValueError):
            multiply_matrices([[1,2],[3]], [[1,2],[3,4]])  # A não retangular
        with self.assertRaises(ValueError):
            multiply_matrices([[1,2],[3,4]], [[1,2,3]])    # B não retangular
        with self.assertRaises(ValueError):
            multiply_matrices([[1,2,3]], [[1,2],[3,4]])    # dimensões incompatíveis

if __name__ == "__main__":
    unittest.main()