import sqlite3

conexao = sqlite3.connect("pagamentos.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS titulos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT,
    descricao TEXT,
    beneficiario TEXT,
    data TEXT,
    valor REAL,
    status TEXT
);
""")
conexao.commit()

def cadastrar(tipo, descricao, beneficiario, data, valor, status):
    cursor.execute("""
    INSERT INTO titulos (tipo, descricao, beneficiario, data, valor, status)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (tipo, descricao, beneficiario, data, valor, status))
    conexao.commit()


def listar():
    cursor.execute("SELECT * FROM titulos")
    return cursor.fetchall()


def atualizar(id_titulo, novo_status):
    cursor.execute("UPDATE titulos SET status = ? WHERE id = ?", 
                   (novo_status, id_titulo))
    conexao.commit()


def excluir(id_titulo):
    cursor.execute("DELETE FROM titulos WHERE id = ?", 
                   (id_titulo,))
    conexao.commit()
