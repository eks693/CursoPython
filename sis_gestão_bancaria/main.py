import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import  messagebox, ttk
import sv_ttk

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

def on_closing():
    root.destroy()

def login():
    user = entrada_usuario.get()
    senha = entrada_senha.get()
    
    users = {
    "nome": "Erick",
    "senha": "1234",
    }
    
    if user == users.get("nome") and senha == users.get("senha"):
        print(f"Logado com sucesso" + user)
        tela_principal(user)
    else:
        messagebox.showerror('Mensagem', 'Usuario ou senha incorretos')

contas = {
    "1234": ContaBancaria("Erick", "1234", 0),
    "5678": ContaBancaria("Maria", "5678", 0),
    "4321": ContaBancaria("João", "4321", 0),
}

def tela_principal(user):

    def verificar_saldo():
        conta_saldo = entrada_conta.get()

        if conta_saldo in contas:
            if entrada_conta.get() == '':
              messagebox.showinfo('Mensagem', 'Digite um valor')
              entrada_valor.delete(0, tk.END)
              entrada_conta.delete(0, tk.END)
            else:
                saldo = contas[conta_saldo].consultar_saldo()
                messagebox.showinfo('Mensagem', f'Seu saldo é: {saldo}')
                entrada_valor.delete(0, tk.END)
                entrada_conta.delete(0, tk.END)
        else:
            messagebox.showinfo('Mensagem', 'Conta nao encontrada')
            entrada_conta.delete(0, tk.END)

    def depositar():
        conta = entrada_conta.get()
        valor = (entrada_valor.get())
        
        if conta in contas:
            if valor == '':
                messagebox.showinfo('Mensagem', 'Digite um valor')
                entrada_valor.delete(0, tk.END)
                entrada_conta.delete(0, tk.END)
            else:
                valor = float(valor)
                contas[conta].depositar(valor)
                messagebox.showinfo('Mensagem', 'Deposito realizado com sucesso')
                messagebox.showinfo('Mensagem', f'Seu saldo é: {contas[conta].consultar_saldo()}')
                entrada_valor.delete(0, tk.END)
                entrada_conta.delete(0, tk.END)
        else:
            messagebox.showinfo('Mensagem', 'Conta nao encontrada')
            entrada_conta.delete(0, tk.END)
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
    
    def consulta_conta():
        conta = entrada_conta.get()
        if conta in contas:
            messagebox.showinfo('Mensagem', f'Titular: {contas[conta].titular}, Saldo: {contas[conta].consultar_saldo()}')
            entrada_conta.delete(0, tk.END)
        else:
            messagebox.showinfo('Mensagem', 'Conta nao encontrada')
            entrada_conta.delete(0, tk.END)
    
    def listar_contas():
        mensagem = "Lista de Contas:\n"
        for conta in contas:
            mensagem += f"Titular: {contas[conta].titular}\n"
            mensagem += f"Conta: {conta}\n"
            mensagem += f"Saldo: {contas[conta].consultar_saldo()}\n\n"

        messagebox.showinfo('Contas Cadastradas', mensagem)
            
    # Janela tela principal
    root.withdraw()
    main_window = tk.Toplevel()
    main_window.title('Tela Principal')
    main_window.geometry('520x240')
    root.protocol("WM_DELETE_WINDOW", on_closing)

    ttk.Label(main_window, text = 'Operações com a conta \n', font = ('Arial', 20)).grid(row=0, column=1)
    
    ttk.Label(main_window, text = 'Número da Conta').grid(row=1, column=0) 
    entrada_conta = tk.Entry(main_window)
    entrada_conta.grid(row=1, column=1)

    ttk.Label(main_window, text = 'Valor').grid(row=2, column=0)
    entrada_valor = tk.Entry(main_window)
    entrada_valor.grid(row=2, column=1)

    ttk.Label(main_window, text = '\n', font = ('Arial', 5)).grid(row=3, column=1)
    
    ttk.Button(main_window, text= 'Mostrar Saldo',command=verificar_saldo).grid(row=4, column=0)
    ttk.Button(main_window, text= 'Sacar', command=novo_saque).grid(row=4, column=1)
    ttk.Button(main_window, text= 'Depositar', command= depositar).grid(row=4, column=2)

    ttk.Label(main_window, text = '\n', font = ('Arial', 2)).grid(row=5, column=1)

    ttk.Button(main_window, text= 'Adicionar Conta', command= tela_nova_conta).grid(row=6, column=0)
    ttk.Button(main_window, text= 'Consultar Conta', command= consulta_conta).grid(row=6, column=1)
    ttk.Button(main_window, text= 'Listar Contas', command= listar_contas).grid(row=6, column=2)

    ttk.Label(main_window, text = '\n', font = ('Arial', 2)).grid(row=7, column=1)

    ttk.Button(main_window, text='Sair', command= on_closing).grid(row=8, column=1)

def tela_nova_conta():
    global nova_conta_window
    tela_nova_conta_window = tk.Toplevel()
    tela_nova_conta_window.title('Cadastro de Conta')
    tela_nova_conta_window.geometry('440x180')

    global entrada_nova_conta, entrada_novo_titular, entrada_novo_saldo

    def limpar():
        entrada_nova_conta.delete(0, tk.END)
        entrada_novo_titular.delete(0, tk.END)
        entrada_novo_saldo.delete(0, tk.END)

    def adicionar_conta():
        numero_conta = entrada_nova_conta.get()
        titular = entrada_novo_titular.get()
        saldo = entrada_novo_saldo.get()

        if numero_conta not in contas:
            contas[numero_conta] = ContaBancaria(titular, numero_conta, saldo)
            messagebox.showinfo('Mensagem', 'Numero de conta cadastrado')
            tela_nova_conta_window.destroy()
        else:
            messagebox.showinfo('Mensagem', 'Numero de conta ja cadastrado')

    def cancelar():
        tela_nova_conta_window.destroy()

    ttk.Label(tela_nova_conta_window, text = 'Cadastro de Conta \n', font = ('Arial', 20)).grid(row=0, column=1)

    ttk.Label(tela_nova_conta_window, text = 'Número da Conta').grid(row=1, column=0) 
    entrada_nova_conta = tk.Entry(tela_nova_conta_window)
    entrada_nova_conta.grid(row=1, column=1)

    ttk.Label(tela_nova_conta_window, text = 'Titular').grid(row=2, column=0)
    entrada_novo_titular = tk.Entry(tela_nova_conta_window)
    entrada_novo_titular.grid(row=2, column=1)

    ttk.Label(tela_nova_conta_window, text = 'Saldo Inicial').grid(row=3, column=0)
    entrada_novo_saldo = tk.Entry(tela_nova_conta_window)
    entrada_novo_saldo.grid(row=3, column=1)

    ttk.Label(tela_nova_conta_window, text = '\n', font = ('Arial', 5)).grid(row=4, column=1)

    ttk.Button(tela_nova_conta_window, text= 'Adicionar', command=adicionar_conta).grid(row=5, column=0)
    ttk.Button(tela_nova_conta_window, text= 'Limpar', command=limpar).grid(row=5, column=1)
    ttk.Button(tela_nova_conta_window, text= 'Voltar', command=cancelar).grid(row=5, column=2)
    

# Criar tela de login
root = tk.Tk()
root.title('Login Caixa Eletrônico')
root.geometry('300x160')

sv_ttk.set_theme('dark')

ttk.Label(root, text = 'Gestão Bancária \n', font = ('Arial', 20)).grid(row=0, column=1)

ttk.Label(root, text = 'Usuario:').grid(row=1, column=0) 
entrada_usuario = tk.Entry(root)
entrada_usuario.grid(row=1, column=1)

ttk.Label(root, text = 'Senha ').grid(row=2, column=0) 
entrada_senha = tk.Entry(root)
entrada_senha.grid(row=2, column=1)

ttk.Label(root, text = '\n', font = ('Arial', 5)).grid(row=3, column=1)

ttk.Button(root, text= 'Entrar', command= login).grid(row=4, columnspan=2)

root.mainloop()
