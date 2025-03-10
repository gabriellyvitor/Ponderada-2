class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.historico = []

    def assistir(self, titulo):
        self.historico.append(titulo)

    def obter_historico(self):
        return self.historico