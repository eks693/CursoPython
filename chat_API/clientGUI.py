import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import socketio
import requests

# conexão cliente-servidor
sio = socketio.Client()
sio.connect('http://127.0.0.1:5000')

# Variável global para armazenar o nome do usuário
user_name = ""

# Função enviar mensagens
def send_message():
    global user_name
    message = entry_message.get()
    if message and user_name:  # Só envia se houver mensagem e usuário cadastrado
        sio.emit('send_message', {'message': message, 'sender': user_name})  # Envia o nome junto
        scrolled_text.insert(tk.END, f"Você: {message}\n")  # Mostra a mensagem enviada
        scrolled_text.see(tk.END)  # Rola para a última mensagem
        entry_message.delete(0, tk.END)
    elif not user_name:
        messagebox.showwarning("Aviso", "Crie um usuário antes de enviar mensagens.")

# Função para criar usuário
def create_user():
    global user_name
    name = entry_name.get()
    age = entry_age.get()
    if name and age.isdigit():  # Verifica se nome existe e idade é um número válido
        response = requests.post('http://localhost:5000/users', json={'name': name, 'age': age})
        if response.status_code == 201:
            user_name = name  # Salva o nome do usuário
            messagebox.showinfo("Sucesso", f"Usuário {name} criado com sucesso")
        else:
            messagebox.showerror("Erro", "Erro ao criar usuário")
    else:
        messagebox.showerror("Erro", "Preencha um nome válido e uma idade numérica.")

    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)

# Função para receber mensagens do servidor
@sio.on('receive_message')
def receive_message(data):
    sender = data.get('sender', 'Servidor')  # Nome do remetente (se disponível)
    message = data.get('message', '')
    scrolled_text.insert(tk.END, f"{sender}: {message}\n")  # Mostra o nome do remetente
    scrolled_text.see(tk.END)  # Rola para a última mensagem

# interface:
root = tk.Tk()
root.title("Chat API")
root.geometry("400x400")

# Área de exibição de mensagens
scrolled_text = ScrolledText(root, wrap=tk.WORD, height=10, width=50)
scrolled_text.pack(padx=10, pady=10)
scrolled_text.config(state=tk.NORMAL)

# Entrada de mensagens do chat
label_message = tk.Label(root, text="Mensagem:")
label_message.pack()
entry_message = tk.Entry(root, width=40)
entry_message.pack(padx=10, pady=5)

btn_send = tk.Button(root, text="Enviar", command=send_message)
btn_send.pack(pady=5)

# Coleta de dados para a requisição
tk.Label(root, text="Nome:").pack()
entry_name = tk.Entry(root, width=40)
entry_name.pack(padx=10, pady=5)

label_age = tk.Label(root, text="Idade:")
label_age.pack()
entry_age = tk.Entry(root, width=40)
entry_age.pack(padx=10, pady=5)

button_create_user = tk.Button(root, text="Criar usuário", command=create_user)
button_create_user.pack(pady=5)

root.mainloop()
