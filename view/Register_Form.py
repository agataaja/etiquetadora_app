from view.Itens_Form import Itens_Form
import customtkinter as ctk
from Register_Control import Register_Control_Itens, Register_Control
from controller.services.log import Log
from tkinter import ttk

class Register_Form:

    def __init__(self):

        self.page_index = 0
        self.page_index_list = []# Initialize the page index
        self.frames = []  # List to store frames for each page
        self.input_data = {}  # Dictionary to store input data for each page

        self.__createView()

    def __create_frame(self, main_window):

        self.new_frame = ctk.CTkFrame(main_window)
        self.new_frame.place(relwidth=1, relheight=1)

        return self.new_frame

    def __show_frame(self, frame):

        frame.tkraise()

    def __createView(self):

        self.window = ctk.CTk()
        self.window.geometry('510x600+200+200')
        self.window.title('Registro de Produtos Bazar Rei')
        self.main_frame = self.__create_frame(self.window)
        self.__createForm()
        self.__show_frame(self.main_frame)
        Log().printLog("Programa aberto")
        self.window.mainloop()

    def __createForm(self):

        self.__create_SimpleLabel('Formulário Bazar Rei ', 80, self.main_frame)

        self.__create_SimpleLabel('Nome Compelto: ', 130, self.main_frame)
        self.inputName = self.__createInput(160, self.main_frame)

        self.__create_SimpleLabel('CPF: ', 190, self.main_frame)
        self.inputEmail = self.__create_CPF_Input(220, self.main_frame)

        self.__create_SimpleLabel('Núcleo: ', 250, self.main_frame)
        nucleos_list = ["Reio Hoasqueiro", "Canário Verde"]
        self.input_combobox, self.input_drop_var = self.__createDropDown(280, nucleos_list,  self.main_frame)

        self.__createBtn(320, 340, self.next_page, self.main_frame, "Iniciar")

    def __createItensForm(self, frame):

        def __search_ref_vars(value):

            self.item = value

            print('item é:', self.item)

            self.item_ref_values = []

            if self.item == "Vestuário":
                self.item_ref_values = ['Calça', 'Blusa', 'Camisa']
            elif self.item == "Acessórios":
                self.item_ref_values = ['Brinco', 'Colar', 'Pulseira']
            elif self.item == "Outros":
                self.item_ref_values = ['Outros']
            elif self.item == "Decoração":
                self.item_ref_values = ['Vaso', 'Quadro', 'Tapete']
            elif self.item == "Utilidades":
                self.item_ref_values = ['Copo', 'Prato', 'Talher', 'Outros (Identidicar na descrição)']
            elif self.item == "Eletrônicos/Eletrodomésticos":
                self.item_ref_values = ['Mixer/Juicer', 'Batedeira', 'Micro-ondas', 'Liquidificador',
                                        'Outros (Identidicar na descrição)']

            print(self.item_ref_values)

            self.input_combobox1.configure(values=self.item_ref_values)
            self.input_combobox1.set('')

        self.respost = self.__create_SimpleLabel(f'Registrando itens de: {self.inputName.get()}', 40, frame)

        self.__create_SimpleLabel('Item: ', 70, frame)
        itens_list = ["Acessórios", "Vestuário", "Decoração", "Utilidades", "Eletrônicos/Eletrodomésticos", "Outros"]
        self.input_combobox, self.drop_var_ref = self.__createDropDown(100, itens_list, frame, __search_ref_vars)
        # self.input_combobox.bind("<Button-1>", self.__search_ref_vars)

        self.__create_SimpleLabel('Referência: ', 130, frame)
        self.input_combobox1, self.drop_ref_item = self.__createDropDown(160, [''],  frame)

        self.__create_SimpleLabel('Cor: ', 190, frame)
        cor_dropdown = [
            "Amarelo",
            "Azul",
            "Branco",
            "Cinza",
            "Laranja",
            "Marrom",
            "Preto",
            "Rosa",
            "Roxo",
            "Verde",
            "Vermelho",
            "Sem Cor"]
        self.input_combobox2, self.string_cor = self.__createDropDown(220, cor_dropdown,  frame)

        self.__create_SimpleLabel('Tamanho: ', 250, frame)
        tamanho_dropdown = [
            "PP",
            "M",
            "G",
            "GG",
            "Sem Tamanho"]
        self.input_combobox3, self.string_tamanho = self.__createDropDown(280, tamanho_dropdown, frame)

        self.__create_SimpleLabel('Preço: ', 310, frame)
        self.PrecoName = self.__create_Reais_Input(340, 30, frame)

        self.__create_SimpleLabel('Descrição: ', 370, frame)
        self.inputDesc = self.__createLargerInput(400, 80, frame)
        # self.inputDesc.bind("<KeyRelease>", self.__limit_description)

        self.__createBtn(320, 490, self.next_page, frame, "Próximo")

        self.__createBtn(60, 490, self.back_page, frame, "Voltar")

        self.page_label = self.__create_SimpleLabel(f'Página {self.page_index}', 560, frame)

    def __create_SimpleLabel(self, txt, y, frame):

        self.label = ctk.CTkLabel(frame, text=txt)
        self.label.place(x=60, y=y)

        return self.label

    def __createInput(self, y,frame):
        self.input = ctk.CTkEntry(frame, width=380)
        self.input.place(x=60, y=y)
        return self.input

    def __create_CPF_Input(self, y, frame):
        self.input = CPFEntry(frame, width=380, placeholder_text="Digite o CPF")
        self.input.place(x=60, y=y)
        return self.input

    def __createDropDown(self, y, values, frame, command=None):

        self.drop_var = ctk.StringVar()
        self.dropDown = ctk.CTkComboBox(frame, variable=self.drop_var, values=values, width=380,
                                        command=command)
        self.dropDown.place(x=60, y=y)
        self.dropDown.set('')

        return self.dropDown, self.drop_var

    def __createBtn(self, x, y, command, frame, text):

        self.button = ctk.CTkButton(frame, text=text, width=120, command=command)
        self.button.place(x=x, y=y)

    def __create_Reais_Input(self, y, height, frame):

        self.input = ReaisEntry(frame, width=380, height=height)
        self.input.place(x=60, y=y)
        return self.input

    def __createLargerInput(self, y, height, frame):

        self.email_box = ctk.CTkTextbox(frame, height=height, width=380)
        self.email_box.place(x=60, y=y)
        return self.email_box

    def __proximo_(self):

        Log().printLog("Clicado o botão de Iniciar")
        # self.control = Register_Control(self.inputName.get(), self.inputEmail.get(), self.input_drop_var.get())

        # self.__show_frame(self.donations_frame)

    def get_input_data_itens(self):

        Log().printLog("Clicado o botão de Enviar")

        self.control = Register_Control_Itens(self.drop_var_ref.get(), self.drop_ref_item.get(), self.string_cor.get(),
                                              self.string_tamanho.get(), self.PrecoName.get(), self.inputDesc.get("1.0", "end-1c"))

    def next_page(self):

        if self.page_index + 2 in self. page_index_list:
            print(f"pagina {self.page_index} ja criada")
            print(self.frames)
            print(self.page_index_list)
            print(self.page_index)

            self.__show_frame(self.frames[self.page_index + 1][0] )

        else:

            print(f"pagina {self.page_index} nao criada")
            #self.save_input_data()  # Save current page data
            self.page_index += 1
            self.page_index_list.append(self.page_index)
            self.next_frame = self.__create_frame(self.window)
            self.__createItensForm(self.next_frame)
            self.page_label.configure(text=f'Página {self.page_index}')
            self.frames.append((self.next_frame, self.page_index))
            #self.__show_frame(self.frames[self.page_index])

            print(self.frames)
            print(self.page_index_list)
            print(self.page_index)

    def back_page(self):

        if self.page_index > 0:

            self.page_index -= 1
            #self.page_label.configure(text=f'Página {self.page_index + 1}')
            self.__show_frame(self.frames[self.page_index][0])

    def save_input_data(self):
        """Saves the current inputs into the input_data dictionary."""
        data = {
            "item": self.drop_var_ref.get(),
            "referencia": self.drop_ref_item.get(),
            "cor": self.string_cor.get(),
            "tamanho": self.string_tamanho.get(),
            "preco": self.PrecoName.get(),
            "descricao": self.inputDesc.get("1.0", "end-1c"),
        }
        self.input_data[self.page_index] = data

class CPFEntry(ctk.CTkEntry):

    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.bind("<KeyRelease>", self.format_cpf)

    def format_cpf(self, event):
        value = self.get().replace('.', '').replace('-', '')
        if not value.isdigit():
            return

        if len(value) <= 3:
            formatted_value = value
        elif len(value) <= 6:
            formatted_value = f"{value[:3]}.{value[3:]}"
        elif len(value) <= 9:
            formatted_value = f"{value[:3]}.{value[3:6]}.{value[6:]}"
        else:
            formatted_value = f"{value[:3]}.{value[3:6]}.{value[6:9]}-{value[9:11]}"

        self.delete(0, ctk.END)
        self.insert(0, formatted_value)


class ReaisEntry(ctk.CTkEntry):

    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.bind("<KeyRelease>", self.format_reais)

    def format_reais(self, event):
        value = self.get().replace('R$', '').replace('.', '').replace(',', '').strip()

        # Ensure only digits are processed
        if not value.isdigit():
            self.delete(0, ctk.END)
            return

        # Convert value to an integer (cents)
        int_value = int(value)

        # Format the value with two decimal places, using the comma as the decimal separator
        formatted_value = f"R$ {int_value / 100:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

        # Insert formatted value back into the entry
        self.delete(0, ctk.END)
        self.insert(0, formatted_value)

        # Ensure the cursor is at the right-most position
        self.icursor(ctk.END)




