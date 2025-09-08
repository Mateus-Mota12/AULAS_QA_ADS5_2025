import unittest
from ex3_romanos import int_to_roman, roman_to_int

class TestRomanos(unittest.TestCase):
    def test_ida_volta(self):
        casos = [1, 4, 9, 40, 44, 58, 1994, 3999]
        for n in casos:
            r = int_to_roman(n)
            self.assertEqual(roman_to_int(r), n)

    def test_limites(self):
        with self.assertRaises(ValueError):
            int_to_roman(0)
        with self.assertRaises(ValueError):
            int_to_roman(4000)

    def test_invalidos(self):
        for s in ["IC", "IL", "XM", "VX", "IIII", "VV", "MCMC", "IIV", ""]:
            with self.assertRaises(ValueError):
                roman_to_int(s)

if __name__ == "__main__":
    unittest.main()
