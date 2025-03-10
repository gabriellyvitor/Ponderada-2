import unittest
from src.serie import Serie

class TestSerie(unittest.TestCase):
    def test_continuar(self):
        serie = Serie("Stranger Things")
        serie.assistir(30)
        self.assertEqual(serie.continuar(), "Continuando 'Stranger Things' a partir de 30 minutos.")

if __name__ == "__main__":
    unittest.main()