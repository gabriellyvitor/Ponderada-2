import unittest
from src.recomendacao import Recomendacao
import time

class TestRecomendacao(unittest.TestCase):
    def test_recomendacao_acao(self):
        historico = ["Ação"]
        recomendador = Recomendacao(historico)
        inicio = time.time()
        resultado = recomendador.recomendar()
        fim = time.time()
        self.assertEqual(resultado, "Você pode gostar de 'John Wick'.")
        self.assertLess(fim - inicio, 2, "Recomendação demorou mais de 2 segundos")

if __name__ == "__main__":
    unittest.main()
