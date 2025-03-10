import hashlib

class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.historico = []
        self.senha = self._criptografar_senha(senha)

    # RNF: Segurança — Criptografia de Senhas
    def _criptografar_senha(self, senha):
        return hashlib.sha256(senha.encode()).hexdigest()

    def verificar_senha(self, senha):
        return self.senha == hashlib.sha256(senha.encode()).hexdigest()

    def assistir(self, titulo):
        self.historico.append(titulo)

    def obter_historico(self):
        return self.historico
