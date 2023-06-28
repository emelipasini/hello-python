import unittest

class PruebasMetodosCadenas(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('hola'.upper(), 'HOLA')

    def test_is_upper(self):
        self.assertTrue('HOLA'.isupper())
        self.assertFalse('hola'.isupper())

    def test_split(self):
        cadena = 'Hola mundo'
        self.assertEqual(cadena.split(" "), ['Hola', 'mundo'])

if __name__ == "__main__":
    unittest.main()

