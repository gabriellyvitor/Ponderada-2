import unittest
from src.usuario import Usuario

class TestUsuario(unittest.TestCase):
    def test_historico(self):
        # Corrigido: Adicionada a senha como argumento
        usuario = Usuario("Alice", "senha123")
        usuario.assistir("Ação")
        self.assertEqual(usuario.obter_historico(), ["Ação"])

    # Novo teste para verificar a senha
    def test_verificar_senha(self):
        usuario = Usuario("Alice", "senha123")
        self.assertTrue(usuario.verificar_senha("senha123"))
        self.assertFalse(usuario.verificar_senha("senhaErrada"))

if __name__ == "__main__":
    unittest.main()
