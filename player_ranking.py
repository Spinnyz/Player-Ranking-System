class Jogador:
    def __init__(self,nome,pontuacao):
        self.nome = nome
        self.pontuacao = pontuacao
    
    def adicionar_pontos(self,pontos):
        self.pontuacao += pontos

    def __str__(self):
        return f"{self.nome}: {self.pontuacao} pontos"

class Ranking:
    def __init__(self):
        self.jogadores = []

    def adicionar_jogador(self,nome,pontuacao):
        self.jogadores.append(Jogador(nome,pontuacao))
    
    def remover_jogador(self,nome):
        for jogador in self.jogadores:
            if jogador.nome == nome:
                self.jogadores.remove(jogador)
                print (f"O jogador {nome} foi removido do ranking.")
                return
        print (f"O jogador {nome} não foi encontrado no ranking.")
