import unittest
from src.usuario import Usuario

class TestUsuario(unittest.TestCase):
    def test_historico(self):
        usuario = Usuario("Alice")
        usuario.assistir("Ação")
        self.assertEqual(usuario.obter_historico(), ["Ação"])

if __name__ == "__main__":
    unittest.main()