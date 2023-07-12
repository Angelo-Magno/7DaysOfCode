class Produto:

    def __init__(self, id, nome, quantidade):
        self.id = id
        self.nome = nome
        self.qtd = quantidade

    def mostrar_produto(self):
        print(f'ID: {self.id} - Nome: {self.nome} - Qtd: {self.qtd}' + '\n')


class Node:
    def __init__(self, produto):
        self.produto = produto
        self.esquerda = None
        self.direita = None


class ArvoreProduto:
    def __init__(self):
        self.raiz = None
        self.ligacoes = []

    def inserir_produto(self, produto):
        novo = Node(produto)
        if self.raiz is None:
            self.raiz = novo
        else:
            atual = self.raiz
            while True:
                pai = atual
                if produto.id == atual.produto.id:
                    atual.produto = produto
                    return
                # Esquerda
                elif produto.id < atual.produto.id:
                    atual = atual.esquerda
                    if atual is None:
                        pai.esquerda = novo
                        return
                # Direita
                else:
                    atual = atual.direita
                    if atual is None:
                        pai.direita = novo
                        return

    def buscar_produto(self, id):
        atual = self.raiz
        while atual.produto.id != id:
            if id < atual.produto.id:
                atual = atual.esquerda
            else:
                atual = atual.direita
            if atual is None:
                print('Produto não encontrado!' + '\n')
                return None

        atual.produto.mostrar_produto()
        return atual


arvore_produtos = ArvoreProduto()
arvore_produtos.inserir_produto(Produto(23, 'Teclado', 20))
arvore_produtos.inserir_produto(Produto(31, 'Mouse', 121))
arvore_produtos.inserir_produto(Produto(15, 'Monitor', 32))
arvore_produtos.inserir_produto(Produto(12, 'Placa-Mãe', 63))
arvore_produtos.inserir_produto(Produto(11, 'HD', 300))

arvore_produtos.buscar_produto(15)
arvore_produtos.inserir_produto(Produto(15, 'Monitor', 45))
arvore_produtos.buscar_produto(15)

arvore_produtos.buscar_produto(13)
arvore_produtos.buscar_produto(12)
