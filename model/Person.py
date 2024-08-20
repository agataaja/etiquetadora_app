class Person:

    def __init__(self, name, cpf, nucleo):
        self.__name = name
        self.__cpf = cpf
        self.__nucleo = nucleo

    def get_name(self):
        return self.__name

    def get_cpf(self):
        return self.__cpf

    def get_nucleo(self):
        return self.__nucleo


class Itens:

    def __init__(self, item, referencia, cor, tamanho, preco, descricao):
        self.__item = item
        self.__referencia = referencia
        self.__cor = cor
        self.__tamanho = tamanho
        self.__preco = preco
        self.__descricao = descricao

    def get_item(self):
        return self.__item

    def get_referencia(self):
        return self.__referencia

    def get_cor(self):
        return self.__cor

    def get_tamanho(self):
        return self.__tamanho

    def get_preco(self):
        return self.__preco

    def get_descricao(self):
        return self.__descricao
