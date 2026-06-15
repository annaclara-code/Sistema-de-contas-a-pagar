import tkinter as tk
from lancamento import (
    listar_contas,
    adicionar_conta,
    deletar_conta,
    alternar_status,
    criar_tabela
)

# ---------------- FUNÇÕES ----------------

def mostrar_contas():
    lista.delete("1.0", tk.END)

    contas = listar_contas()

    if not contas:
        lista.insert(tk.END, "Nenhuma conta encontrada.\n")
        return

    for c in contas:
        lista.insert(tk.END,
f"""ID: {c[0]}
Descrição: {c[1]}
Valor: R$ {c[2]:.2f}
Lançamento: {c[3]}
Vencimento: {c[4]}
Status: {c[5]}
------------------------
""")

def adicionar():
    try:
        desc = entrada_desc.get()
        valor = float(entrada_valor.get())
        venc = entrada_venc.get()
        lanc = "2026-01-01"
        status = "Pendente"

        adicionar_conta(desc, valor, lanc, venc, status)

        mostrar_contas()

        entrada_desc.delete(0, tk.END)
        entrada_valor.delete(0, tk.END)
        entrada_venc.delete(0, tk.END)

    except ValueError:
        lista.insert(tk.END, "Erro: valor inválido!\n")


def deletar():
    try:
        id_conta = int(entrada_id.get())
        deletar_conta(id_conta)

        mostrar_contas()
        entrada_id.delete(0, tk.END)
    except ValueError:
        lista.insert(tk.END, "Erro: ID inválido!\n")


def alternar():
    try:
        id_conta = int(entrada_id.get())
        alternar_status(id_conta)

        mostrar_contas()
        entrada_id.delete(0, tk.END)
    except ValueError:
        lista.insert(tk.END, "Erro: ID inválido!\n")


# ---------------- JANELA ----------------

janela = tk.Tk()
janela.title("Contas a Pagar")
janela.geometry("750x600")

criar_tabela()

# ---------------- TÍTULO ----------------

tk.Label(janela, text="SISTEMA DE CONTAS A PAGAR", font=("Arial", 16)).pack(pady=10)

# ---------------- FORMULÁRIO ----------------

tk.Label(janela, text="Descrição").pack()
entrada_desc = tk.Entry(janela)
entrada_desc.pack()

tk.Label(janela, text="Valor").pack()
entrada_valor = tk.Entry(janela)
entrada_valor.pack()

tk.Label(janela, text="Vencimento").pack()
entrada_venc = tk.Entry(janela)
entrada_venc.pack()

tk.Button(janela, text="Adicionar Conta", command=adicionar).pack(pady=5)

# ---------------- AÇÕES ----------------

tk.Label(janela, text="ID da conta").pack()
entrada_id = tk.Entry(janela)
entrada_id.pack()

tk.Button(janela, text="Alternar Pago/Pendente", command=alternar).pack(pady=5)
tk.Button(janela, text="Deletar Conta", command=deletar, bg="red", fg="white").pack(pady=5)

tk.Button(janela, text="Listar Contas", command=mostrar_contas).pack(pady=10)

# ---------------- LISTA COM SCROLL ----------------

frame_lista = tk.Frame(janela)
frame_lista.pack(fill="both", expand=True, padx=10, pady=10)

scroll = tk.Scrollbar(frame_lista)
scroll.pack(side="right", fill="y")

lista = tk.Text(frame_lista, yscrollcommand=scroll.set, font=("Consolas", 10))
lista.pack(side="left", fill="both", expand=True)

scroll.config(command=lista.yview)

# ---------------- INICIO ----------------

mostrar_contas()

janela.mainloop()

