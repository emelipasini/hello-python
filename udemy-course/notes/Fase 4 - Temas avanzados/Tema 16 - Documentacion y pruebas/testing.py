import unittest

class Pruebas(unittest.TestCase):

    def test(self):
        pass

    def test_fail(self):
        raise AssertionError()

    def test_error(self):
        1/0

    """
    def test_cases(self):
        assertEqual(a, b)
        assertNotEqual(a, b)
        assertTrue(x)
        assertFalse(x)
        assertIs(a, b)
        assertIsNot(a, b)
        assertIsNone(x)
        assertIsNotNone(x)
        assertIn(a, b)
        assertNotIn(a, b)
        assertIsInstance(a, b)
        assertNotIsInstance(a, b)
    """

if __name__ == "__main__":
    unittest.main()

