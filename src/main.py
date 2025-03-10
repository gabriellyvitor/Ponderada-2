from src.recomendacao import Recomendacao
from src.usuario import Usuario
from src.serie import Serie

# RNF: Manutenibilidade — Código modular e bem organizado
def executar():
    # Criando um usuário com senha
    usuario = Usuario("Alice", "senha123")
    if usuario.verificar_senha("senha123"):
        print("Senha verificada com sucesso!")

    usuario.assistir("Ação")

    # Recomendação com base no histórico
    recomendador = Recomendacao(usuario.obter_historico())
    print(recomendador.recomendar())

    # Controle de séries
    serie = Serie("Stranger Things")
    serie.assistir(30)
    print(serie.continuar())

if __name__ == "__main__":
    executar()
