
from player_ranking import Ranking


ranking = Ranking()

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
            nome = input("Digite o nome do jogador: ").title()
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