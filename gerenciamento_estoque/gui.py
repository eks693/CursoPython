import tkinter as tk
from tkinter import ttk
from estoque import Estoque
from database import conectar_mongo

class EstoqueApp:
    def __init__(self, root):
        self.db = conectar_mongo()
        self.estoque = Estoque(self.db)

        self.root = root
        self.root.title('Gerenciamento de Estoque')
        self.root.geometry('340x400')
        
        #widgets
        self.nome_label = ttk.Label(root, text='Nome:')
        self.nome_label.grid(row=0, column=0, padx = 5, pady = 5)
        self.nome_entry = ttk.Entry(root)
        self.nome_entry.grid(row=0, column=1, padx = 5, pady = 5)

        self.quantidade_label = ttk.Label(root, text='Quantidade:')
        self.quantidade_label.grid(row=1, column=0, padx = 5, pady = 5)
        self.quantidade_entry = ttk.Entry(root)
        self.quantidade_entry.grid(row=1, column=1, padx = 5, pady = 5)

        self.adicionar_button = ttk.Button(root, text='Adicionar', command=self.adicionar_produto)
        self.adicionar_button.grid(row=2, column=0, padx = 5, pady = 5)

        self.remover_button = ttk.Button(root, text='Remover', command=self.remover_produto)
        self.remover_button.grid(row=2, column=1, padx = 5, pady = 5)

        self.listar_button = ttk.Button(root, text='Listar', command=self.listar_itens)
        self.listar_button.grid(row=3, column=0, padx = 5, pady = 5)

        self.limpar_button = ttk.Button(root, text='Limpar', command=self.limpar_resultado)
        self.limpar_button.grid(row=3, column=1, padx = 5, pady = 5)

        self.resultado_text = tk.Text(root, width=40, height=10)
        self.resultado_text.grid(row=4, column=0, columnspan=2, padx = 5, pady = 5)


    def adicionar_produto(self):
        nome = self.nome_entry.get()
        quantidade = int(self.quantidade_entry.get())
        self.estoque.adicionar_produto(nome, quantidade)
        self.nome_entry.delete(0, tk.END)
        self.quantidade_entry.delete(0, tk.END)
        self.resultado_text.insert(tk.END, f'Item {nome} adicionado com sucesso \n')   

    def remover_produto(self):
        nome = self.nome_entry.get()
        quantidade = int(self.quantidade_entry.get())
        self.estoque.remover_produto(nome, quantidade) 
        self.nome_entry.delete(0, tk.END)
        self.quantidade_entry.delete(0, tk.END)       
        self.resultado_text.insert(tk.END, f'Item {nome} removido com sucesso \n')


    def listar_itens(self):
        itens = self.estoque.listar_itens()
        self.resultado_text.delete('1.0', tk.END)
        for item in itens:
            self.resultado_text.insert(tk.END, f'Nome: {item["nome"]}, Quantidade: {item["quantidade"]}\n')

    def limpar_resultado(self):
        self.resultado_text.delete('1.0', tk.END)

if __name__ == '__main__':
    root = tk.Tk()
    app = EstoqueApp(root)
    root.mainloop()