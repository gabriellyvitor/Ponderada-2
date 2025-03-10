class Recomendacao:
    def __init__(self, historico):
        self.historico = historico

    def recomendar(self):
        if "Ação" in self.historico:
            return "Você pode gostar de 'John Wick'."
        elif "Drama" in self.historico:
            return "Você pode gostar de 'The Crown'."
        else:
            return "Que tal explorar novos gêneros?"