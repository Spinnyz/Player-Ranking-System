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
    
    def atualizar_pontuacao(self,nome,pontos):
        for jogador in self.jogadores:
            if jogador.nome == nome:
                jogador.adicionar_pontos(pontos)
                print (f"A pontuação de {nome} foi atualizado para {jogador.pontuacao}")
                return
        print (f"O jogador {nome} não foi encontrado")
    
    def listar_ranking(self):
        for jogador in sorted (self.jogadores, key=lambda jogador: jogador.pontuacao, reverse=True):
            print (jogador)
    
    def top_jogadores(self):
        return [jogador.nome for jogador in self.jogadores if jogador.pontuacao >= 40]
    
    def buscar_jogadores(self,nome):
        for jogador in self.jogadores:
            if jogador.nome == nome:
                print (jogador)
                return
        print (f"O jogador {nome} não foi encontrado")

while True:
    print ("""
[1] Adicionar jogador
[2] Remover jogador
[3] Atualizar pontuação
[4] Listar ranking
[5] Top jogadores
[6] Buscar jogador
[0] Sair
""")
    opcao = input("Escolha uma opção: ")


    match opcao:
        case "1":
            nome = input("Digite o nome do jogador: ")
            pontuacao = int(input("Digite a pontuação do jogador: "))  
            Ranking.adicionar_jogador(nome,pontuacao)
        case "2":
            nome = input("Digite o nome do jogador: ")
            Ranking.remover_jogador(nome)
        case "3":
            nome = input("Digite o nome do jogador: ")
            pontos = int(input("Digite a quantidade de pontos: "))
            Ranking.atualizar_pontuacao(nome,pontos)
        case "4":
            Ranking.listar_ranking()
        case "5":
            print (Ranking.top_jogadores())
        case "6":
            nome = input("Digite o nome do jogador: ")
            Ranking.buscar_jogadores(nome)
        case "0":
            break
        case _:
            print ("Opção inválida")