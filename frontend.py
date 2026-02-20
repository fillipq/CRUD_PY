import tkinter as tk
from tkinter import ttk, messagebox
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
    novo_status = entrada_status_atualizar.get()

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
    entrada_status_atualizar.delete(0, tk.END)

janela = tk.Tk()
janela.title("Sistema de Pagamentos")
janela.geometry("600x450")

abas = ttk.Notebook(janela)
abas.pack(expand=True, fill="both")

# ABA CADASTRO
aba_cadastro = tk.Frame(abas)
abas.add(aba_cadastro, text="Cadastro")

tk.Label(aba_cadastro, text="Tipo (Pagar/Receber):").grid(row=0, column=0)
entrada_tipo = tk.Entry(aba_cadastro)
entrada_tipo.grid(row=0, column=1)

tk.Label(aba_cadastro, text="Descrição:").grid(row=1, column=0)
entrada_descricao = tk.Entry(aba_cadastro)
entrada_descricao.grid(row=1, column=1)

tk.Label(aba_cadastro, text="Beneficiário:").grid(row=2, column=0)
entrada_beneficiario = tk.Entry(aba_cadastro)
entrada_beneficiario.grid(row=2, column=1)

tk.Label(aba_cadastro, text="Data (AAAA-MM-DD):").grid(row=3, column=0)
entrada_data = tk.Entry(aba_cadastro)
entrada_data.grid(row=3, column=1)

tk.Label(aba_cadastro, text="Valor:").grid(row=4, column=0)
entrada_valor = tk.Entry(aba_cadastro)
entrada_valor.grid(row=4, column=1)

tk.Label(aba_cadastro, text="Status (Pendente/Pago):").grid(row=5, column=0)
entrada_status = tk.Entry(aba_cadastro)
entrada_status.grid(row=5, column=1)

tk.Button(aba_cadastro, text="Cadastrar", command=cadastrar).grid(row=6, column=0, columnspan=2, pady=10)

aba_listagem = tk.Frame(abas)
abas.add(aba_listagem, text="Listagem")

tk.Button(aba_listagem, text="Listar Registros", command=listar).pack(pady=10)

texto_lista = tk.Text(aba_listagem, height=15, width=70)
texto_lista.pack()

aba_editar = tk.Frame(abas)
abas.add(aba_editar, text="Atualizar / Excluir")

tk.Label(aba_editar, text="ID:").grid(row=0, column=0)
entrada_id = tk.Entry(aba_editar)
entrada_id.grid(row=0, column=1)

tk.Label(aba_editar, text="Novo Status:").grid(row=1, column=0)
entrada_status_atualizar = tk.Entry(aba_editar)
entrada_status_atualizar.grid(row=1, column=1)

tk.Button(aba_editar, text="Atualizar Status", command=atualizar).grid(row=2, column=0, pady=10)

tk.Button(aba_editar, text="Excluir", command=excluir).grid(row=2, column=1, pady=10)


janela.mainloop()