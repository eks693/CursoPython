import tkinter as tk
from tkinter import ttk
from cadastro import CadastroClientes
from database import conectar_mongo

class ClienteApp:
    def __init__(self, root):
        self.db = conectar_mongo()
        self.cadastro = CadastroClientes(self.db)

        self.root = root
        self.root.title('Gerenciamento de Clientes')
        self.root.geometry('400x400')

        # Widgets
        self.nome_label = ttk.Label(root, text='Nome:')
        self.nome_label.grid(row=0, column=0, padx=5, pady=5)
        self.nome_entry = ttk.Entry(root)
        self.nome_entry.grid(row=0, column=1, padx=5, pady=5)

        self.email_label = ttk.Label(root, text='Email:')
        self.email_label.grid(row=1, column=0, padx=5, pady=5)
        self.email_entry = ttk.Entry(root)
        self.email_entry.grid(row=1, column=1, padx=5, pady=5)

        self.telefone_label = ttk.Label(root, text='Telefone:')
        self.telefone_label.grid(row=2, column=0, padx=5, pady=5)
        self.telefone_entry = ttk.Entry(root)
        self.telefone_entry.grid(row=2, column=1, padx=5, pady=5)

        self.adicionar_button = ttk.Button(root, text='Adicionar', command=self.adicionar_cliente)
        self.adicionar_button.grid(row=3, column=0, padx=5, pady=5)

        self.remover_button = ttk.Button(root, text='Remover', command=self.remover_cliente)
        self.remover_button.grid(row=3, column=1, padx=5, pady=5)

        self.listar_button = ttk.Button(root, text='Listar', command=self.listar_clientes)
        self.listar_button.grid(row=4, column=0, padx=5, pady=5)

        self.limpar_button = ttk.Button(root, text='Limpar', command=self.limpar_resultado)
        self.limpar_button.grid(row=4, column=1, padx=5, pady=5)

        self.resultado_text = tk.Text(root, width=50, height=15)
        self.resultado_text.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def adicionar_cliente(self):
        nome = self.nome_entry.get()
        email = self.email_entry.get()
        telefone = self.telefone_entry.get()
        self.cadastro.adicionar_cliente(nome, email, telefone)
        self.nome_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.telefone_entry.delete(0, tk.END)
        self.resultado_text.insert(tk.END, f'Cliente {nome} adicionado com sucesso\n')

    def remover_cliente(self):
        nome = self.nome_entry.get()
        self.cadastro.remover_cliente(nome)
        self.nome_entry.delete(0, tk.END)
        self.resultado_text.insert(tk.END, f'Cliente {nome} removido com sucesso\n')

    def listar_clientes(self):
        clientes = list(self.cadastro.listar_clientes())
        self.resultado_text.delete('1.0', tk.END)
        if clientes:
            for cliente in clientes:
                self.resultado_text.insert(
                    tk.END, f"Nome: {cliente['nome']}, Email: {cliente['email']}, Telefone: {cliente['telefone']}\n"
                )
        else:
            self.resultado_text.insert(tk.END, "Nenhum cliente cadastrado.\n")

    def limpar_resultado(self):
        self.resultado_text.delete('1.0', tk.END)

if __name__ == '__main__':
    root = tk.Tk()
    app = ClienteApp(root)
    root.mainloop()
