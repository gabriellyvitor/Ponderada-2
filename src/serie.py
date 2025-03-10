class Serie:
    def __init__(self, titulo):
        self.titulo = titulo
        self.progresso = 0

    def assistir(self, minutos):
        if minutos <= 0:
            raise ValueError("Minutos assistidos devem ser maiores que zero.")
        
        # RNF: Usabilidade — Mensagens de erro claras
        self.progresso += minutos

    def continuar(self):
        return f"Continuando '{self.titulo}' a partir de {self.progresso} minutos."
