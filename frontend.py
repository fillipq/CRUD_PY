import tkinter as tk
from tkinter import messagebox
import main


def cadastrar():
    tipo = entrada_tipo.get()
    descricao = entrada_descricao.get()
    beneficiario = entrada_beneficiario.get()
    data = entrada_data.get()
    valor = entrada_valor.get()
    status = entrada_status.get()

    if not tipo or not descricao:
        messagebox.showwarning("Erro", "Preencha os campos obrigatórios!")
        return

    main.cadastrar(tipo, descricao, beneficiario, data, valor, status)
    messagebox.showinfo("Sucesso", "Título cadastrado com sucesso!")
    listar()
    limpar_campos()


def listar():
    registros = main.listar()
    texto_lista.delete("1.0", tk.END)

    for r in registros:
        texto_lista.insert(tk.END, f"{r}\n")


def atualizar():
    id_titulo = entrada_id.get()
    novo_status = entrada_status.get()

    if not id_titulo:
        messagebox.showwarning("Erro", "Informe o ID!")
        return

    main.atualizar(id_titulo, novo_status)
    messagebox.showinfo("Sucesso", "Status atualizado!")
    listar()

    limpar_campos()


def excluir():
    id_titulo = entrada_id.get()

    if not id_titulo:
        messagebox.showwarning("Erro", "Informe o ID!")
        return

    main.excluir(id_titulo)
    messagebox.showinfo("Sucesso", "Título excluído!")
    listar()

    limpar_campos()

def limpar_campos():
    entrada_tipo.delete(0, tk.END)
    entrada_descricao.delete(0, tk.END)
    entrada_beneficiario.delete(0, tk.END)
    entrada_data.delete(0, tk.END)
    entrada_valor.delete(0, tk.END)
    entrada_status.delete(0, tk.END)
    entrada_id.delete(0, tk.END)


janela = tk.Tk()
janela.title("Sistema de Pagamentos")

tk.Label(janela, text="Tipo (Pagar/Receber):").grid(row=0, column=0)
entrada_tipo = tk.Entry(janela)
entrada_tipo.grid(row=0, column=1)

tk.Label(janela, text="Descrição:").grid(row=1, column=0)
entrada_descricao = tk.Entry(janela)
entrada_descricao.grid(row=1, column=1)

tk.Label(janela, text="Beneficiário:").grid(row=2, column=0)
entrada_beneficiario = tk.Entry(janela)
entrada_beneficiario.grid(row=2, column=1)

tk.Label(janela, text="Data (AAAA-MM-DD):").grid(row=3, column=0)
entrada_data = tk.Entry(janela)
entrada_data.grid(row=3, column=1)

tk.Label(janela, text="Valor:").grid(row=4, column=0)
entrada_valor = tk.Entry(janela)
entrada_valor.grid(row=4, column=1)

tk.Label(janela, text="Status (Pendente/Pago):").grid(row=5, column=0)
entrada_status = tk.Entry(janela)
entrada_status.grid(row=5, column=1)

tk.Label(janela, text="ID Atualizar/Excluir:").grid(row=6, column=0)
entrada_id = tk.Entry(janela)
entrada_id.grid(row=6, column=1)

tk.Button(janela, text="Cadastrar", command=cadastrar).grid(row=7, column=1)
tk.Button(janela, text="Atualizar Status", command=atualizar).grid(row=7, column=0)
tk.Button(janela, text="Listar", command=listar).grid(row=8, column=1)
tk.Button(janela, text="Excluir", command=excluir).grid(row=8, column=0)

texto_lista = tk.Text(janela, height=10, width=60)
texto_lista.grid(row=9, column=0, columnspan=2)

janela.mainloop()
