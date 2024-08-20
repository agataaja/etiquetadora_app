import customtkinter as ctk
from Register_Control import Register_Control_Itens
from controller.services.log import Log
from tkinter import ttk


class Itens_Form:

    def __init__(self):
        self.__createView1()

    def __createView1(self):
        self.register_itens_window = ctk.CTk()
        self.register_itens_window.geometry('500x500+200+200')
        self.register_itens_window.title('Registro de Produtos Bazar Rei')
        self.__createForm1()
        Log().printLog("Input itens aberto")
        self.register_itens_window.mainloop()

    def __limit_description(self, event):

        current_text = self.inputDesc.get()
        if len(current_text) > 15:
            self.inputDesc.delete(15, 'end')

    def __search_ref_vars(self, event):

        self.item = self.drop_var_ref.get()

        print('item é:', self.item)

        self.item_ref_values = []

        if self.item == "Vestuário":
            self.item_ref_values = ['Calça', 'Blusa', 'Camisa']
        elif self.item == "Acessórios":
            self.item_ref_values = ['Brinco', 'Colar', 'Pulseira']
        elif self.item == "Decoração":
            self.item_ref_values = ['Vaso', 'Quadro', 'Tapete']
        elif self.item == "Utilidades":
            self.item_ref_values = ['Copo', 'Prato', 'Talher']
        elif self.item == "Eletrônicos/Eletrodomésticos":
            self.item_ref_values = ['Televisão', 'Geladeira', 'Micro-ondas']

        print(self.item_ref_values)

        self.input_combobox1['values'] = self.item_ref_values

        self.input_combobox1.set('')

    def __createForm1(self):

        self.__createLabel1('Item: ', 70)
        itens_list = ["Acessórios", "Vestuário", "Decoração", "Utilidades", "Eletronicos/eletrodoméstico", "Outros"]
        self.input_combobox, self.drop_var_ref = self.__createDropDown1(100, itens_list)
        self.input_combobox.bind("<<ComboboxSelected>>", self.__search_ref_vars)

        self.__createLabel1('Referência: ', 130)
        self.input_combobox1, self.drop_ref_item = self.__createDropDown1(160, [''])

        self.__createLabel1('Cor: ', 190)
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
            "Vermelho"]
        self.input_combobox2, self.string_cor = self.__createDropDown1(220, cor_dropdown)

        self.__createLabel1('Tamanho: ', 250)
        cor_dropdown = [
            "PP",
            "M",
            "G",
            "GG"]
        self.input_combobox3, self.string_tamanho = self.__createDropDown1(280, cor_dropdown)

        self.__createLabel1('Preço: ', 310)
        self.PrecoName = self.__createInput1(340, 30)

        self.__createLabel1('Descrição: ', 370)
        self.inputDesc = self.__createInput1(400, 80)
        self.inputDesc.bind("<KeyRelease>", self.__limit_description)

        self.__createBtnSubmit1()

    def __createLabel1(self, txt, y):
        self.label = ctk.CTkLabel(self.register_itens_window, text=txt)
        self.label.place(x=60, y=y)

    def __createInput1(self, y, height):
        self.input = ctk.CTkEntry(self.register_itens_window, width=380, height=height)
        self.input.place(x=60, y=y)
        return self.input

    def __createDropDown1(self, y, values):
        self.drop_var = ctk.StringVar()
        self.dropDown = ctk.CTkComboBox(self.register_itens_window, variable=self.drop_var, values=values, width=380)
        self.dropDown.place(x=60, y=y)
        self.dropDown.set('')

        return self.dropDown, self.drop_var

    def __createDropDown_bind1(self, y, values):

        self.drop_var = ctk.StringVar()
        self.dropDown = ttk.Combobox(self.register_itens_window, textvariable=self.drop_var, values=values, width=45)
        self.dropDown.place(x=60, y=y)
        self.dropDown.set('')

        return self.dropDown, self.drop_var


    def __createBtnSubmit1(self):
        self.button = ctk.CTkButton(self.register_itens_window, text='Enviar', width=40, command=self.get_input_data)
        self.button.place(x=120, y=460)

    def get_input_data(self):

        Log().printLog("Clicado o botão de Enviar")
        print("é", self.drop_var_ref.get(), self.drop_ref_item.get(), self.string_cor.get(),
                                              self.string_tamanho.get(), self.PrecoName.get(), self.inputDesc.get())

        self.control = Register_Control_Itens(self.drop_var_ref.get(), self.drop_ref_item.get(), self.string_cor.get(),
                                              self.string_tamanho.get(), self.PrecoName.get(), self.inputDesc.get())

        # self.respost = self.__createLabel('User created successfully', 40)



