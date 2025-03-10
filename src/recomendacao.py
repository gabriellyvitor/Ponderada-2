import time

class Recomendacao:
    def __init__(self, historico):
        self.historico = historico

    def recomendar(self):
        # RNF: Desempenho — O sistema deve processar recomendações em menos de 2 segundos
        inicio = time.time()
        
        if "Ação" in self.historico:
            recomendacao = "Você pode gostar de 'John Wick'."
        elif "Drama" in self.historico:
            recomendacao = "Você pode gostar de 'The Crown'."
        else:
            recomendacao = "Que tal explorar novos gêneros?"
        
        fim = time.time()
        tempo_execucao = fim - inicio
        
        # Aferição do RNF
        if tempo_execucao > 2:
            raise TimeoutError("O sistema demorou mais de 2 segundos para processar.")
        
        return recomendacao
