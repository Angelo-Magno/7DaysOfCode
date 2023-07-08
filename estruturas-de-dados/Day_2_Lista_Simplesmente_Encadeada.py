class Paciente:

    def __init__(self,  id: int, nome: str, estado_saude: str):
        estado_saude = estado_saude.lower().strip()
        self.__validar(id, estado_saude)
        self.id = id
        self.nome = nome.strip()
        self.estado_saude = estado_saude
        self.proximo = None

    def __validar(self, id, estado_saude):
        if type(id) != int:
            raise 'O ID deve ser um inteiro'
        if estado_saude not in ['estavel', 'tratamento intensivo', 'em estado critico']:
            raise 'O estado de saúde deve ser "estavel", "tratamento intensivo" ou "em estado critico"'

    def exibir_paciente(self):
        print('-' * 25)
        print(f'ID: {self.id}')
        print(f'Nome: {self.nome}')
        print(f'Estado de Saúde: {self.estado_saude}')
        print('-' * 25)


class ListaDePacientes:

    def __init__(self):
        self.head = None
        self.tail = None

    def __lista_vazia(self):
        return self.head is None

    def adicionar_paciente(self,  id: int, nome: str, estado_saude: str):
        novo_paciente = Paciente(id, nome, estado_saude)
        if self.__lista_vazia():
            self.head = novo_paciente
        else:
            self.tail.proximo = novo_paciente
        self.tail = novo_paciente

    def pesquisar_paciente(self, id: int):
        if self.__lista_vazia():
            print('Não há pacientes na lista!')
            return

        atual = self.head
        while atual is not None:
            if atual.id == id:
                return atual
            atual = atual.proximo

        print('Paciente não encontrado')

    def remover_paciente(self, id: int):
        if self.__lista_vazia():
            print('Não há pacientes na lista!')
            return

        atual = self.head
        flag = 0
        while atual is not None:
            if atual.id == id:
                flag = 1
                break
            anterior = atual
            atual = atual.proximo

        if flag:
            if atual == self.head == self.tail:
                self.head = None
                self.tail = None
            elif atual == self.head:
                self.head = self.head.proximo
            elif atual == self.tail:
                self.tail = anterior
                anterior.proximo = None
            else:
                anterior.proximo = atual.proximo
            print('Paciente removido com Sucesso!')
        else:
            print('Paciente não encontrado!')

    def listar_pacientes(self):
        if self.__lista_vazia():
            print('Não há pacientes na lista!')
            return

        atual = self.head
        while atual is not None:
            atual.exibir_paciente()
            atual = atual.proximo


lista_de_paciente = ListaDePacientes()
lista_de_paciente.adicionar_paciente(14, 'Jubileu', 'tratamento intensivo')
lista_de_paciente.adicionar_paciente(18, 'Siclano', 'estavel')
lista_de_paciente.adicionar_paciente(16, 'Fulano', 'em estado critico')
lista_de_paciente.listar_pacientes()
lista_de_paciente.remover_paciente(18)
lista_de_paciente.listar_pacientes()
lista_de_paciente.remover_paciente(15)
lista_de_paciente.remover_paciente(14)
lista_de_paciente.listar_pacientes()
lista_de_paciente.remover_paciente(16)
lista_de_paciente.listar_pacientes()