import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ContaBancaria:
    def __init__(self, titular, conta, saldo):
        self.titular = titular
        self.conta = conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente')
            return
        else:
            self.saldo -= valor
            print('Saque realizado com sucesso')

    def consultar_saldo(self):
        return self.saldo

def inserir_conta():
    conta =  entrada_nova_conta.get()
    titular = entrada_novo_titular.get()
        
    if titular == '' or conta == '':
        messagebox.showinfo('Mensagem', 'Preencha todos os campos')
        entrada_novo_titular.delete(0, tk.END)
        entrada_nova_conta.delete(0, tk.END)

    else:
        if conta in contas:
            messagebox.showinfo('Mensagem', 'Numero de conta já criado')
            entrada_novo_titular.delete(0, tk.END)
            entrada_nova_conta.delete(0, tk.END)
        else:
            contas[conta] = ContaBancaria(titular, conta, 0)
            messagebox.showinfo('Mensagem', 'Conta cadastrada com sucesso')
            entrada_novo_titular.delete(0, tk.END)
            entrada_nova_conta.delete(0, tk.END)

contas = {
    '1234': ContaBancaria('Erick', '1234', 0),
    '5678': ContaBancaria('Orlando', '5678', 0),
}

def verificar_conta():
    numero_conta = entrada_conta.get()
    if numero_conta in contas:
        saldo = contas[numero_conta].consultar_saldo()
        messagebox.showinfo('Mensagem', f'Seu saldo é: {saldo}')
        entrada_conta.delete(0, tk.END)
    else:
        messagebox.showinfo('Mensagem', 'Conta nao encontrada')
        entrada_conta.delete(0, tk.END)

def novo_deposito():
    numero_conta = entrada_conta.get()
    saldo_conta = (entrada_valor.get())

    if numero_conta in contas:
        if entrada_valor.get() == '':
            messagebox.showinfo('Mensagem', 'Digite um valor')
            entrada_valor.delete(0, tk.END)
            entrada_conta.delete(0, tk.END)

        else:
            saldo_conta = float(saldo_conta)
            contas[numero_conta].depositar(saldo_conta)
            messagebox.showinfo('Mensagem', 'Deposito realizado com sucesso')
            messagebox.showinfo('Mensagem', f'Seu saldo é: {contas[numero_conta].consultar_saldo()}')
            entrada_valor.delete(0, tk.END)
            entrada_conta.delete(0, tk.END)

    else:
        messagebox.showinfo('Mensagem', 'Conta nao encontrada')

def novo_saque():
    numero_conta = entrada_conta.get()
    valor_saque = entrada_valor.get()
    
    if numero_conta in contas and entrada_valor.get() != '':
        valor_saque = float(valor_saque)
        if valor_saque > contas[numero_conta].consultar_saldo():
            messagebox.showinfo('Mensagem', f'Saldo insuficiente, seu saldo é: {contas[numero_conta].consultar_saldo()}')
            entrada_valor.delete(0, tk.END)
            entrada_conta.delete(0, tk.END)

        else:
            contas[numero_conta].sacar(valor_saque)
            messagebox.showinfo('Mensagem', 'Saque realizado com sucesso')
            messagebox.showinfo('Mensagem', f'Seu saldo é: {contas[numero_conta].consultar_saldo()}')
            entrada_valor.delete(0, tk.END)
            entrada_conta.delete(0, tk.END)

    else:
        messagebox.showinfo('Mensagem', 'Conta nao encontrada ou valor invalido')
        entrada_valor.delete(0, tk.END)

def limpar():
    entrada_conta.delete(0, tk.END)
    entrada_valor.delete(0, tk.END)
    entrada_nova_conta.delete(0, tk.END)
    entrada_novo_titular.delete(0, tk.END)

root = tk.Tk()
root.title('Caixa Eletrônico')
root.geometry('520x320')

ttk.Label(root, text = 'Operações com a conta \n', font = ('Arial', 20)).grid(row=0, column=1)

ttk.Label(root, text = 'Número da Conta').grid(row=1, column=0) 
entrada_conta = tk.Entry(root)
entrada_conta.grid(row=1, column=1)

ttk.Label(root, text = 'Valor').grid(row=2, column=0)
entrada_valor = tk.Entry(root)
entrada_valor.grid(row=2, column=1)

ttk.Button(root, text= 'Mostrar Saldo', command= verificar_conta).grid(row=3, column=0)
ttk.Button(root, text= 'Sacar', command= novo_saque).grid(row=3, column=1)
ttk.Button(root, text= 'Depositar', command= novo_deposito).grid(row=3, column=2)

ttk.Label(root, text = '\n', font = ('Arial', 10)).grid(row=4, column=1)
ttk.Label(root, text = 'Incluir nova conta\n', font = ('Arial', 20)).grid(row=5, column=1)

ttk.Label(root, text = 'Número da Conta').grid(row=6, column=0) 
entrada_nova_conta = tk.Entry(root)
entrada_nova_conta.grid(row=6, column=1)

ttk.Label(root, text = 'Titular').grid(row=7, column=0)
entrada_novo_titular = tk.Entry(root)
entrada_novo_titular.grid(row=7, column=1)

ttk.Button(root, text= 'Adicionar', command= inserir_conta).grid(row=8, column=0)
ttk.Button(root, text= 'Limpar', command= limpar).grid(row=8, column=1)

root.mainloop()
