from recomendacao import Recomendacao
from usuario import Usuario
from serie import Serie

# Criando um usuário
usuario = Usuario("Alice")
usuario.assistir("Ação")

# Recomendação com base no histórico
recomendador = Recomendacao(usuario.obter_historico())
print(recomendador.recomendar())

# Controle de séries
serie = Serie("Stranger Things")
serie.assistir(30)
print(serie.continuar())