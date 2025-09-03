class jogador:
    def __init__(self,nome,pontuacao):
        self.nome = nome
        self.pontuacao = pontuacao
    
    def adicionar_pontos(self,pontos):
        self.pontuacao += pontos

    def __str__(self):
        return f"{self.nome}: {self.pontuacao} pontos"