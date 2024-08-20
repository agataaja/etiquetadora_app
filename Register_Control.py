from model.Person import Person, Itens
import datetime
import os
from model.DAO.PersonDAO import PersonDAO
from model.DAO.ItemSHEETS import ItemSheets, PersonSheet

class Register_Control:

    def __init__(self, name, cpf, nucleo):

        self.get_date()

        person_sheet = PersonSheet()
        self.person = Person(name, cpf, nucleo)
        last_id = person_sheet.get_last_id()
        self.id = last_id + 1

        self.person = Person(name, cpf, nucleo)
        self.name = self.person.get_name()
        self.cpf = self.person.get_cpf()
        self.nucleo = self.person.get_nucleo()

        self.print_console()

    def get_date(self):

        self.current_date = datetime.datetime.now()

        self.text_date = '{}_{}_{}'.format(self.current_date.day, self.current_date.month, self.current_date.year)
        self.text_time_data = 'Date created: {}'.format(self.current_date.strftime("%d/%m/%Y  %H:%M"))


    def print_console(self):

        print(
            '\n ID: ', self.id,
            '\n Name: ', self.person.get_name(),
            '\n CPF: ', self.person.get_cpf(),
            '\n Núcleo: ', self.person.get_nucleo()
        )
        self.save()

    def save(self):

        try:
            self.dir_path = os.path.dirname(os.path.realpath(__file__))
            self.folder = "logs"

            if not os.path.isdir(self.folder):
                os.mkdir(self.folder)# aqui criamos a pasta caso nao exista
                print('Pasta criada com sucesso!')

            self.file_name = self.dir_path + '/' + self.folder+'/{}_{}.log'.format(self.person.get_name(), self.text_date)
            self.file = open(self.file_name, 'w')

            self.file.write(f'{self.id}')
            self.file.write('\n')
            self.file.write(self.name)
            self.file.write('\n')
            self.file.write(self.cpf)
            self.file.write('\n')
            self.file.write(self.nucleo)
            self.file.write('\n')
            self.file.write(self.text_time_data)

            # self.person = {
            #    "nome": self.name,
            #    "CPF": self.cpf,
            #    "nucleo": self.nucleo
            #}

            self.person_list = [self.text_time_data, self.id, self.name, self.cpf, self.nucleo]

            PersonSheet().insert(self.person_list)
            
            # PersonDAO().insert(self.person)

        except:
            print('\n Error saving data')

        finally:
            self.file.close()
            print('\n Data saved successfully')


class Register_Control_Itens:

    def __init__(self, item, referencia, cor, tamanho, preco, descricao):
        self.get_date()

        self.item_objct = Itens(item, referencia, cor, tamanho, preco, descricao)
        self.item = 'item: {}'.format(self.item_objct.get_item())
        self.referencia = 'Referência: {}'.format(self.item_objct.get_referencia())
        self.cor = 'Cor: {}'.format(self.item_objct.get_cor())
        self.tamanho = 'Tamanho: {}'.format(self.item_objct.get_tamanho())
        self.preco = 'Preço: {}'.format(self.item_objct.get_preco())
        self.descricao = 'Descriçao: {}'.format(self.item_objct.get_descricao())

        self.print_console()

    def get_date(self):

        self.current_date = datetime.datetime.now()
        self.text_date = '{}_{}_{}'.format(self.current_date.day, self.current_date.month, self.current_date.year)
        self.text_time_data = 'Date created: {}'.format(self.current_date.strftime("%d/%m/%Y  %H:%M"))

    def print_console(self):
        print(
            '\n Item: ', self.item_objct.get_item(),
            '\n Referência: ', self.item_objct.get_referencia(),
            '\n Cor: ', self.item_objct.get_cor(),
            '\n Tamanho: ', self.item_objct.get_tamanho(),
            '\n Preço: ', self.item_objct.get_preco(),
            '\n Descrição: ', self.item_objct.get_descricao(),
        )
        self.save()

    def save(self):
        try:
            self.dir_path = os.path.dirname(os.path.realpath(__file__))
            self.folder = "logs"

            if not os.path.isdir(self.folder):
                os.mkdir(self.folder)  # aqui criamos a pasta caso nao exista
                print('Pasta criada com sucesso!')

            self.file_name = self.dir_path + '/' + self.folder + '/{}_{}.log'.format(self.item_objct.get_item(),
                                                                                     self.text_date)
            self.file = open(self.file_name, 'w')

            self.file.write(self.item)
            self.file.write('\n')
            self.file.write(self.referencia)
            self.file.write('\n')
            self.file.write(self.cor)
            self.file.write('\n')
            self.file.write(self.tamanho)
            self.file.write('\n')
            self.file.write(self.preco)
            self.file.write('\n')
            self.file.write(self.descricao)
            self.file.write('\n')
            self.file.write(self.text_time_data)

            self.item_objct = {
                ' Item: ': self.item,
                ' Referência: ': self.referencia,
                ' Cor: ': self.cor,
                ' Tamanho: ': self.tamanho,
                ' Preço: ': self.preco,
                ' Descrição: ': self.descricao,

            }

            self.item_list = [self.text_time_data, self.item, self.referencia, self.cor, self.tamanho, self.preco, self.descricao]

            ItemSheets().insert(self.item_list)

        except:
            print('\n Error saving data')

        finally:
            self.file.close()
            print('\n Data saved successfully')