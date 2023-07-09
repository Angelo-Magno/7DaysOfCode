class Produto:

    def __init__(self, cod: str, nome: str, preco: float, qtd_estoque: int):
        self.cod = cod
        self.nome = nome
        self.preco = preco
        self.qtd_estoque = qtd_estoque
        self.anterior = None
        self.proximo = None

    def mostrar_produto(self):
        print('=' * 44)
        print(f'Cod: {self.cod}')
        print(f'Nome do produto: {self.nome} ')
        print(f'Preço: R$:{self.preco:.2f} ')
        print(f'Qtd estoque: {self.qtd_estoque}')


class ListaDeProdutos:

    def __init__(self):
        self.head = None
        self.tail = None

    def __lista_vazia(self):
        return self.head is None

    def adicionar(self, cod: str, nome: str, preco: float, qtd_estoque: int):
        novo = Produto(cod, nome, preco, qtd_estoque)
        if self.__lista_vazia():
            self.head = novo
        else:
            self.tail.proximo = novo
            novo.anterior = self.tail
        self.tail = novo

    def pesquisar(self, cod=None, nome=None):
        atual = self.head
        if cod is not None:
            while atual is not None:
                if atual.cod == cod:
                    return atual
                atual = atual.proximo
            print('Produto não encontrado!' + '\n')
            return

        if nome is not None:
            while atual is not None:
                if atual.nome == nome:
                    return atual
                atual = atual.proximo
            print('Produto não encontrado!' + '\n')
            return

    def remover(self, cod=None, nome=None):
        if self.__lista_vazia():
            print('A lista de produtos está vazia!' + '\n')
            return
        produto = self.pesquisar(cod, nome)
        excluido = produto
        if produto:
            if produto == self.head == self.tail:
                self.head = None
                self.tail = None
            elif produto == self.head:
                self.head = self.head.proximo
                self.head.anterior = None
            elif produto == self.tail:
                self.tail = self.tail.anterior
                self.tail.proximo = None
            else:
                produto.anterior.proximo = produto.proximo
                produto.proximo.anterior = produto.anterior
            print(f'Produto: "{excluido.nome}" removido com sucesso!' + '\n')
            return excluido

    def atualizar(self, preco: float, qtd_estoque: int, cod=None, nome=None):
        if self.__lista_vazia():
            print('A lista de produtos está vazia!')
            return
        produto = self.pesquisar(cod, nome)
        if produto:
            produto.preco = preco
            produto.qtd_estoque = qtd_estoque
            print('Produto atualizado com Sucesso!' + '\n')

    def listar_produtos_inicio(self):
        if self.__lista_vazia():
            print('A lista de produtos está vazia!')
            return

        print('=' * 45)
        print('Listando produtos a partir do inicio da lista')
        atual = self.head
        while atual is not None:
            atual.mostrar_produto()
            atual = atual.proximo
        print()

    def listar_produtos_final(self):
        if self.__lista_vazia():
            print('A lista de produtos está vazia!')
            return

        print('=' * 44)
        print('Listando produtos a partir do final da lista')
        atual = self.tail
        while atual is not None:
            atual.mostrar_produto()
            atual = atual.anterior
        print()


lista_de_produtos = ListaDeProdutos()
lista_de_produtos.adicionar('25', 'Sabão', 1.50, 130)
lista_de_produtos.adicionar('316', 'Açucar', 3.00, 83)
lista_de_produtos.adicionar('45', 'Macarrão', 7.00, 64)
lista_de_produtos.adicionar('663', 'Farinha de mandioca', 6.20, 30)
lista_de_produtos.listar_produtos_inicio()
lista_de_produtos.listar_produtos_final()
lista_de_produtos.remover(nome='Macarrão')
lista_de_produtos.remover('25')
lista_de_produtos.listar_produtos_inicio()
lista_de_produtos.remover('663')
lista_de_produtos.listar_produtos_final()
lista_de_produtos.atualizar(nome='Arroz', preco=3.50, qtd_estoque=100)
lista_de_produtos.atualizar(nome='Açucar', preco=4.50, qtd_estoque=35)
lista_de_produtos.listar_produtos_inicio()
