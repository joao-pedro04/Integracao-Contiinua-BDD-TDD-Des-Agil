import unittest
from TDD import calcular_media

class TestCalcularMedia(unittest.TestCase):
    def test_media_inteiros(self):
        self.assertEqual(calcular_media(10, 20), 15)

    def test_media_decimais(self):
        self.assertAlmostEqual(calcular_media(10.5, 20.5), 15.5)

    def test_media_negativos(self):
        self.assertEqual(calcular_media(-10, -20), -15)

if __name__ == '__main__':
    unittest.main()