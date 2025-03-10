import unittest
from src.recomendacao import Recomendacao

class TestRecomendacao(unittest.TestCase):
    def test_recomendacao_acao(self):
        historico = ["Ação"]
        recomendador = Recomendacao(historico)
        self.assertEqual(recomendador.recomendar(), "Você pode gostar de 'John Wick'.")

    def test_recomendacao_drama(self):
        historico = ["Drama"]
        recomendador = Recomendacao(historico)
        self.assertEqual(recomendador.recomendar(), "Você pode gostar de 'The Crown'.")

if __name__ == "__main__":
    unittest.main()