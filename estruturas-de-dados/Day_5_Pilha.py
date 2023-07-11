class Livro:

    def __init__(self, titulo: str, qtd_paginas: int):
        self.titulo = titulo
        self.qtd_paginas = qtd_paginas

    def mostrar_livro(self):
        print(f'Livro: {self.titulo} - {self.qtd_paginas} págs')


class PilhaDeLivros:

    def __init__(self):
        self.livros = []

    def __pilha_vazia(self):
        return len(self.livros) < 1

    def adicionar_livro(self, titulo: str, qtd_paginas: int):
        novo_livro = Livro(titulo, qtd_paginas)
        self.livros.append(novo_livro)

    def remover_livro(self):
        if self.__pilha_vazia():
            print('A pilha de livros está vazia!' + '\n')
            return
        return self.livros.pop()

    def livro_do_topo(self):
        topo = self.livros[-1]
        topo.mostrar_livro()
        return topo

    def mostrar_livros(self):
        if self.__pilha_vazia():
            print('A pilha de livros está vazia!' + '\n')
            return
        print('Pilha de Livros:')
        for livro in self.livros[::-1]:
            livro.mostrar_livro()
        print()


pilha_livros = PilhaDeLivros()

pilha_livros.adicionar_livro("A Guerra dos Tronos", 600)
pilha_livros.adicionar_livro("A Fúria dos Reis", 648)
pilha_livros.adicionar_livro("A Tormenta das Espadas", 848)
pilha_livros.adicionar_livro("O Festim dos Corvos", 608)
pilha_livros.adicionar_livro("A Dança dos Dragões", 336)

pilha_livros.mostrar_livros()

livro_removido = pilha_livros.remover_livro()
print('Livro removido:')
livro_removido.mostrar_livro()
