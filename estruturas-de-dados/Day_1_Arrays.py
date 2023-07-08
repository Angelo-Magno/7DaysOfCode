class ListaDeCompras:

    def __init__(self):
        self._itens = []
        self._quantidades = []

    def adicionar_item(self, nome: str, qtd: int):
        if type(nome) != str:
            raise "O nome deve ser do tipo string"
        if type(qtd) != int:
            raise "A quantidade do produto deve ser um inteiro"

        self._itens.append(nome.lower())
        self._quantidades.append(qtd)

    def remover_item(self, nome: str):
        if type(nome) != str:
            raise "O nome produto deve ser do tipo string"

        try:
            indice = self._itens.index(nome.lower())
        except ValueError:
            print(f'"{nome}" não está na lista de compras' + '\n')
            return

        del self._itens[indice]
        del self._quantidades[indice]
    
    def listar_itens(self):
        print('-' * 32)
        print(f'{"Produto":<20}  {"Quantidade":>5}')
        print('-'*32)
        for i in range(len(self._itens)):
            print(f'{self._itens[i]:<20} - {self._quantidades[i]:>9}')
        print()


lista_de_compras = ListaDeCompras()
lista_de_compras.adicionar_item('Arroz', 4)
lista_de_compras.adicionar_item('Sabão', 2)
lista_de_compras.adicionar_item('Pão', 10)
lista_de_compras.adicionar_item('Ovos', 12)
lista_de_compras.adicionar_item('Manteiga', 1)
lista_de_compras.listar_itens()
lista_de_compras.remover_item('Manteiga')
lista_de_compras.remover_item('sabã')
lista_de_compras.listar_itens()
