from collections import deque


class Pedido:

    def __init__(self, n_pedido, nome_cliente, itens_pedido, valor_total):
        self.n_pedido = n_pedido
        self.nome_cliente = nome_cliente
        self.itens_pedido = itens_pedido
        self.valor_total = valor_total

    def __validar(self, n_pedido, nome_cliente, itens_pedido, valor_total):
        if type(n_pedido) is not int:
            raise 'O numero do pedido deve ser um inteiro'
        elif type(nome_cliente) is not str:
            raise 'O nome do cliente deve ser do tipo string'
        elif type(itens_pedido) is not list:
            raise 'Os itens do pedido devem ser passados na forma de lista'
        elif type(valor_total) is not float and type(valor_total) is not int:
            raise 'O valot total do pedido deve ser passado no formato de inteiro ou float'

    def mostrar_pedido(self):
        print('=' * 45)
        print(f'N Pedido: {self.n_pedido} - Cliente: {self.nome_cliente}')
        print(f'Itens do Pedido: {self.itens_pedido}')
        print(f'Valor Total: {self.valor_total}')
        print('=' * 45 + '\n')


class FilaDePedidos:

    def __init__(self):
        self.fila = deque()

    def __fila_vazia(self):
        return len(self.fila) == 0

    def enfileirar(self,  n_pedido: int, nome_cliente: str, itens_pedido: list, valor_total):
        novo_pedido = Pedido(n_pedido, nome_cliente, itens_pedido, valor_total)
        self.fila.appendleft(novo_pedido)
        print('Pedido Adicionado!' + '\n')

    def desemfileirar(self):
        if self.__fila_vazia():
            print('Não há pedidos na Fila!')
            return
        pedido_concluido = self.fila.pop()
        print(f'Pedido {pedido_concluido.n_pedido} de {pedido_concluido.nome_cliente} concluido!' + '\n')
        return pedido_concluido

    def mostrar(self):
        if self.__fila_vazia():
            print('Não há pedidos na Fila')
            return
        for i in range(len(self.fila) - 1, -1, -1):
            self.fila[i].mostrar_pedido()


fila_pedidos = FilaDePedidos()
fila_pedidos.enfileirar(1, 'Angelo', ['Prato do dia', 'Suco de acerola'], 26)
fila_pedidos.enfileirar(2, 'Luiz', ['Picanha', 'Arroz', 'Feijão Preto', 'Salada', 'Coca 250ml'], 52)
fila_pedidos.enfileirar(3, 'Rebecca', ['Strogonoff de frango', 'Arroz', 'Salada', 'Suco de laranja'], 32)
fila_pedidos.mostrar()
fila_pedidos.desemfileirar()
fila_pedidos.mostrar()
fila_pedidos.enfileirar(4, 'Alan', ['Sopa de Carne', 'Torrada'], 22)
fila_pedidos.mostrar()