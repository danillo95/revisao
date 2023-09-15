import tkinter as tk
from tkinter import messagebox

def enviar_mensagem():
    nome = entry_nome.get()
    mensagem = entry_mensagem.get() 
    if nome and mensagem:
        nova_janela = tk.Toplevel(root)
        nova_janela.title("Mensagem Enviada")
        label_nome = tk.Label(nova_janela, text=f"Nome: {nome}")
        label_nome.pack()
        label_mensagem = tk.Label(nova_janela, text=f"Mensagem: {mensagem}")
        label_mensagem.pack()
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos!")

root = tk.Tk()
root.title("Envio de Mensagem")  

label_nome = tk.Label(root, text="Nome:")
label_nome.pack()
entry_nome = tk.Entry(root)
entry_nome.pack()


botao_enviar = tk.Button(root, text="Enviar", command=enviar_mensagem)
botao_enviar.pack()

root.mainloop()
# Ryan alves de oliveira lopes tentei bunquei infomações na internet 
