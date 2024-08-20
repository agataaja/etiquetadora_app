import tkinter as tk
from tkinter import ttk
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import customtkinter as ctk

# Global variables for "Do and Undo" functionality
actions_stack = []

# Google Sheets API setup
def setup_google_sheet():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    # Replace with the path to your downloaded JSON key file
    creds = ServiceAccountCredentials.from_json_keyfile_name('eloquent-surge-425220-q6-68988a48d003.json', scope)

    client = gspread.authorize(creds)

    # Open the sheet by name
    sheet = client.open("pyhton_etiquetas_app").sheet1

    return sheet


sheet = setup_google_sheet()


# Function to handle the "Iniciar" button click
def start_entry():
    donor_name = entry_donor.get()
    cpf = entry_cpf.get()
    nucleo = nucleo_var.get()

    # Store the data into Google Sheets
    sheet.append_row([donor_name, cpf, nucleo])

    # Save the action to the stack for undo
    actions_stack.append([donor_name, cpf, nucleo])

    # Clear the input fields
    entry_donor.delete(0, tk.END)
    entry_cpf.delete(0, tk.END)
    nucleo_dropdown.current(0)

    # Open the new window
    show_frame(donations_frame)




def undo_last_action():

    if actions_stack:
        last_action = actions_stack.pop()
        # Add logic here to undo the last action in Google Sheets if needed
        # For simplicity, we only remove the last entry from the stack here
        print(f"Undone action: {last_action}")


def show_frame(frame):
    frame.tkraise()


def search_ref_vars(event):

    item = item_var.get()

    item_ref_values = []
    if item == "Vestuário":
        item_ref_values = ['Calça', 'Blusa', 'Camisa']
    elif item == "Acessórios":
        item_ref_values = ['Brinco', 'Colar', 'Pulseira']
    elif item == "Decoração":
        item_ref_values = ['Vaso', 'Quadro', 'Tapete']
    elif item == "Utilidades":
        item_ref_values = ['Copo', 'Prato', 'Talher']
    elif item == "Eletrônicos/Eletrodomésticos":
        item_ref_values = ['Televisão', 'Geladeira', 'Micro-ondas']

    item_ref_dropdown['values'] = item_ref_values

    item_ref_dropdown.current(0)  # Set default value


# Main application window
root = ctk.CTk()

root.title("Christmas Bazaar System")
root.geometry("400x300")

# --- Styles (for a more modern look) ---
style = ttk.Style()
style.theme_use("clam")  # Choose a modern theme like 'clam', 'alt', etc.
style.configure("TButton", padding=6, relief="flat", background="#5cb85c", foreground="white")
style.configure("TLabel", padding=(5, 0))
style.configure("TEntry", padding=5)
style.configure("TCombobox", padding=5)

root.configure(background="#2f2f2f", bg="#2f2f2f", highlightbackground="black", highlightcolor="black", width= 100)
entry_style = {"bg": "#585858", "fg": "white", "font": ("Roboto", 9), "width": 35}


# Creating a menu bar
menu_bar = ctk.CTkOptionMenu(root)
root.configure(menu=menu_bar)

# Adding menu items
atividade_menu = tk.Menu(menu_bar, tearoff=0)
atividade_menu.add_command(label="Undo", command=undo_last_action)
dados_menu = tk.Menu(menu_bar, tearoff=0)
ajuda_menu = tk.Menu(menu_bar, tearoff=0)

#menu_bar.option_add(label="Atividade", menu=atividade_menu)
#menu_bar.add_cascade(label="Dados", menu=dados_menu)
#menu_bar.add_cascade(label="Ajuda", menu=ajuda_menu)

# Creating frames for different pages
main_frame = tk.Frame(root)
donations_frame = tk.Frame(root)

for frame in (main_frame, donations_frame):
    frame.grid()

# Main Page Widgets
label_donor = tk.Label(main_frame, text="Doador")
label_donor.grid(row=0, column=0, padx=10, pady=10)
entry_donor = tk.Entry(main_frame, **entry_style)
entry_donor.grid(row=0, column=1, padx=10, pady=10)

label_cpf = tk.Label(main_frame, text="CPF")
label_cpf.grid(row=1, column=0, padx=10, pady=10)
entry_cpf = tk.Entry(main_frame)
entry_cpf.grid(row=1, column=1, padx=10, pady=10)

# Dropdown menu for Núcleo
label_nucleo = tk.Label(main_frame, text="Núcleo")
label_nucleo.grid(row=2, column=0, padx=10, pady=10)
nucleo_var = tk.StringVar()
nucleo_dropdown = ttk.Combobox(main_frame, textvariable=nucleo_var)
nucleo_dropdown['values'] = ("Reio Hoasqueiro", "Canário Verde")
nucleo_dropdown.grid(row=2, column=1, padx=10, pady=10)
nucleo_dropdown.current(0)  # Set default value

# Iniciar button
button_start = tk.Button(main_frame, text="Iniciar", command=start_entry)
button_start.grid(row=3, column=0, columnspan=2, pady=20)

# Donations Page Widgets
# Donations Page Widgets
# Donations Page Widgets
# Donations Page Widgets

# donations_label = tk.Label(donations_frame, text="Welcome to the Donations page!")
# donations_label.grid(pady=20)

# Dropdown menu for Item
label_item = tk.Label(donations_frame, text="Item")
label_item.grid(row=0, column=0, padx=10, pady=10)
item_var = tk.StringVar()
item_dropdown = ttk.Combobox(donations_frame, textvariable=item_var)
item_dropdown['values'] = ("Acessórios", "Vestuário", "Decoração", "Utilidades", "Eletronicos/eletrodoméstico", "Outros" )
item_dropdown.grid(row=0, column=1, padx=10, pady=10)
item_dropdown.current(1)  # Set default value
item_dropdown.bind("<<ComboboxSelected>>", search_ref_vars)

# Dropdown menu for item referencias
label_item_ref = tk.Label(donations_frame, text="Referência")
label_item_ref.grid(row=1, column=0, padx=10, pady=10)
item_ref_var = tk.StringVar()
item_ref_dropdown = ttk.Combobox(donations_frame, textvariable=item_ref_var)

item_ref_dropdown['values'] = ""
item_ref_dropdown.grid(row=1, column=1, padx=10, pady=10)
item_ref_dropdown.current()  # Set default value


# Dropdown menu for cor
label_cor = tk.Label(donations_frame, text="Cor")
label_cor.grid(row=2, column=0, padx=10, pady=10)
cor_var = tk.StringVar()
cor_dropdown = ttk.Combobox(donations_frame, textvariable=cor_var)
cor_dropdown['values'] = (
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
    "Vermelho")

cor_dropdown.grid(row=2, column=1, padx=10, pady=10)
cor_dropdown.current(1)  # Set default value
cor_dropdown.bind("", )


label_descricao = tk.Label(donations_frame, text="Descrição")
label_descricao.grid(row=3, column=0, padx=10, pady=10)
entry_desc_prod = tk.Entry(donations_frame)
entry_desc_prod.grid(row=3, column=1, padx=10, pady=10)




# Button to go back to Main Page
button_back_to_main = tk.Button(donations_frame, text="Voltar", command=lambda: show_frame(main_frame))
button_back_to_main.grid(pady=10)

# Show the main page by default
show_frame(main_frame)

# Start the Tkinter event loop
root.mainloop()