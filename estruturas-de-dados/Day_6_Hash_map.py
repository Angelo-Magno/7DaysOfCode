class Jogo:

    def __init__(self):
        self.tabela = {}

    def adicionar_jogador(self, nome, pontos=0):
        self.tabela[nome] = pontos

    def remover_jogador(self, nome):
        try:
            del self.tabela[nome]
        except KeyError:
            print('Jogador não encontrado!' + '\n')

    def listar_tabela(self):
        for k in sorted(self.tabela, key=self.tabela.get, reverse=True):
            print(f'Jogador: {k} - {self.tabela[k]} pts')
        print()

    def atualizar_pontuacao(self, nome, nova_pontuacao):
        try:
            self.tabela[nome]
        except KeyError:
            print('Jogador não encontrado!' + '\n')
            return
        self.tabela[nome] = nova_pontuacao

    def vencedor(self):
        maior = 0
        vencedor = ''
        for k, v in self.tabela.items():
            if v > maior:
                maior = v
                vencedor = k
        print(f'Campeão {vencedor} com {maior} pts')
        return vencedor


jogo = Jogo()
jogo.adicionar_jogador('player1', 50)
jogo.adicionar_jogador('player2', 30)
jogo.adicionar_jogador('player3', 25)
jogo.adicionar_jogador('player4', 87)
jogo.adicionar_jogador('player5', 150)

jogo.listar_tabela()

jogo.remover_jogador('player1')
jogo.atualizar_pontuacao('player4', 225)

jogo.listar_tabela()

jogo.vencedor()
