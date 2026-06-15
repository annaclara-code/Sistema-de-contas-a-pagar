import sqlite3

def conectar():
    return sqlite3.connect("contas.db")


def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL,
        valor REAL NOT NULL,
        lancamento TEXT NOT NULL,
        vencimento TEXT NOT NULL,
        status TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def adicionar_conta(descricao, valor, lancamento, vencimento, status):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO contas (descricao, valor, lancamento, vencimento, status)
    VALUES (?, ?, ?, ?, ?)
    """, (descricao, valor, lancamento, vencimento, status))

    conn.commit()
    conn.close()


def listar_contas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM contas")
    dados = cursor.fetchall()

    conn.close()
    return dados


def deletar_conta(id_conta):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM contas
    WHERE id = ?
    """, (id_conta,))

    conn.commit()
    conn.close()


def alternar_status(id_conta):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT status FROM contas WHERE id = ?", (id_conta,))
    atual = cursor.fetchone()

    if not atual:
        conn.close()
        return

    novo_status = "Pendente" if atual[0] == "Pago" else "Pago"

    cursor.execute("""
    UPDATE contas
    SET status = ?
    WHERE id = ?
    """, (novo_status, id_conta))

    conn.commit()
    conn.close()