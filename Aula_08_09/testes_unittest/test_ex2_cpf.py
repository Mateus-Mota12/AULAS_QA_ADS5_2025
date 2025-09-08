import unittest
from ex2_cpf import validar_cpf

class TestCPF(unittest.TestCase):
    def test_validos(self):
        self.assertTrue(validar_cpf("529.982.247-25"))
        self.assertTrue(validar_cpf("16899535009"))

    def test_invalidos(self):
        self.assertFalse(validar_cpf("111.111.111-11"))
        self.assertFalse(validar_cpf("123.456.789-10"))
        self.assertFalse(validar_cpf("52998224724"))  # DV incorreto

    def test_entradas_inesperadas(self):
        self.assertFalse(validar_cpf(123))        # tipo errado
        self.assertFalse(validar_cpf("abc"))
        self.assertFalse(validar_cpf(""))

if __name__ == "__main__":
    unittest.main()