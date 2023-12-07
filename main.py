import sqlite3
from fpdf import * 
from datetime import datetime

# Conectar ao banco de dados
conn = sqlite3.connect('gerenciador_financeiro.db')
cursor = conn.cursor()

# Criar tabelas (se ainda não existirem)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS receitas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT,
        data TEXT,
        valor REAL
    )
''')

# Executa um comando SQL para criar uma tabela chamada 'despesas', se ela ainda não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS despesas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT,
        data TEXT,
        valor REAL
    )
''')

# Confirma as alteracoes no banco de dados
conn.commit()

def test_data(data):
    try:
        datetime.strptime(data, '%d/%m/%Y')
        return True
    except ValueError:
        return False

# Funcao para adicionar uma receita ao banco de dados
def add_receita(x, y, z):
    descricao = x
    data_receita = y
    valor_recebimento = float(z)
    # Executa um comando SQL para inserir uma nova entrada na tabela 'receitas'
    cursor.execute('''
        INSERT INTO receitas (descricao, data, valor)
        VALUES (?, ?, ?)
    ''', (descricao, data_receita, valor_recebimento))
    # Confirma as alterações no banco de dados
    conn.commit()
    # Retorna o total de receitas após a adição da nova entrada
    return total_receitas()


# Funcao para adicionar uma despesa ao banco de dados
def add_despesas(x, y, z):
    descricao = x
    data_receita = y
    valor_recebimento = float(z)
    # Executa um comando SQL para inserir uma nova entrada na tabela 'despesas'
    cursor.execute('''
        INSERT INTO despesas (descricao, data, valor)
        VALUES (?, ?, ?)
    ''', (descricao, data_receita, valor_recebimento))
    # Confirma as alterações no banco de dados
    conn.commit()


# Funcao para obter a listagem das receitas cadastradas no banco de dados
def listagem_receitas():
    # Executa um comando SQL para selecionar a descricao, data e valor das receitas
    cursor.execute('''
        SELECT descricao, data, valor FROM receitas
    ''')
    # Obtem todas as linhas resultantes da consulta e armazena em 'receitas'
    receitas = cursor.fetchall()
    # Retorna a lista de receitas
    return receitas


# Funcao para obter a listagem das despesas cadastradas no banco de dados
def listagem_despesas():
    # Executa um comando SQL para selecionar descricao, data e valor no das despesas
    cursor.execute('''
        SELECT descricao, data, valor FROM despesas
    ''')
    # Obtem todas as linhas resultantes da consulta e armazena em 'despesas'
    despesas = cursor.fetchall()
    # Retorna a lista de despesas
    return despesas


# Funcao para calcular o total de receitas cadastradas no banco dados
def total_receitas():
    # Executa um comando SQL para somar os valores da coluna 'valor' da tabela receitas
    cursor.execute('''
        SELECT SUM(valor) FROM receitas
    ''')
    # Obtem o resultado da consulta e acessa o valor total de receitas
    total_recebimento = cursor.fetchone()[0]
    # Retorna o total de receitas, se disponivel; caso contrario, retorna 0
    return total_recebimento if total_recebimento is not None else 0


# Funcao para calcular o total de despesas cadastradas no banco de dados
def total_despesas():
    # Executa um comando SQL para somar os valores da coluna 'valor' da tabela despesas
    cursor.execute('''
        SELECT SUM(valor) FROM despesas
    ''')
    # Obtem o resultado da consulta  e acessa o valor total de despesas
    total_despesa = cursor.fetchone()[0]
    # Retorna o total de despesas, se disponivel, caso contrario, retorna 0
    return total_despesa if total_despesa is not None else 0


# Funcao para excluir uma receita do banco de dados com base na descricao
def exclusao_receita(descricao):
    # Exibe uma mensagem indicando a tentativa de exclusao da receita com descricao fornecida
    print(f'Tentativa de exclusão da receita com descrição: {descricao}')
    # Executa um comando SQL para excluir a receita com base na descricao correspondente
    cursor.execute('''
        DELETE FROM receitas WHERE descricao = ?
    ''', (descricao[0],))
    # Confirma as alteracoes no banco de dados
    conn.commit()

# Funcao para excluir uma despesa do banco de dados com base descricao
def exclusao_despesa(descricao):
    # Exibe uma mensagem indicando a tentativa de exclusao da despesa com descricao fornecida
    print(f'Tentativa de exclusão da despesa com descrição: {descricao}')
    # Executa um comando SQL para excluir a despesa com base na descricao correspondente
    cursor.execute('''
        DELETE FROM despesas WHERE descricao = ?
    ''', (descricao[0],))
    # Confirma as alteracoes no banco de dados
    conn.commit()


# Função para pesquisar registros por descrição nas tabelas de receitas e despesas
def pesquisar_por_descricao(descricao):
    conn = sqlite3.connect("gerenciador_financeiro.db")  # Substitua pelo caminho correto
    cursor = conn.cursor()

    try:
        # Verificar se a tabela receitas existe
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='receitas'")
        tabela_receitas_existe = cursor.fetchone()

        if tabela_receitas_existe:
            # Restante do código para pesquisar por descrição
            cursor.execute("SELECT * FROM receitas WHERE LOWER(descricao) LIKE ?", (f"%{descricao}%",))
            resultados_receitas = cursor.fetchall()

            # Verificar se a tabela despesas existe
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='despesas'")
            tabela_despesas_existe = cursor.fetchone()

            if tabela_despesas_existe:
                # Código para pesquisar por descrição na tabela 'despesas'
                cursor.execute("SELECT * FROM despesas WHERE LOWER(descricao) LIKE ?", (f"%{descricao}%",))
                resultados_despesas = cursor.fetchall()
            else:
                resultados_despesas = []
            # Retorna os resultados das pesquisas nas tabelas 'receitas' e 'despesas'
            return resultados_receitas, resultados_despesas
        # Retorna listas vazias se a tabela 'receitas' não existir
        return [], []  # Retorna listas vazias se a tabela não existir

    finally:
        # Fecha a conexão com o banco de dados
        conn.close()


# Função para Gerar um PDF com os dados receitas e despesas
def imprimir_pdf():
    # Executa um comando SQL para selecionar a descricao, data e valor das receitas
    cursor.execute('''
        SELECT descricao, data, valor FROM receitas
    ''')
    # Obtem todas as linhas resultantes da consulta e armazena em 'receitas'
    receitas = cursor.fetchall()
    
    #criação da tabela de receitas
    tabela_receitas = [
    ("Descrição", "Data", "Valor")
    ]
    for x in receitas:
        descrição,data,valor = x
        auxi_valor=(f'R${valor:.2f}')
        tabela_receitas.append((descrição,data,auxi_valor))


    # Executa um comando SQL para selecionar descricao, data e valor das despesas
    cursor.execute('''
        SELECT descricao, data, valor FROM despesas
    ''')
    # Obtem todas as linhas resultantes da consulta e armazena em 'despesas'
    despesas = cursor.fetchall()

    #criação da tabela de despesas
    tabela_despesas = [
    ("Descrição", "Data", "Valor")
    ]
    for x in despesas:
        descrição,data,valor = x
        auxi_valor=(f'R${valor:.2f}')
        tabela_despesas.append((descrição,data,auxi_valor))

    #criação do layout do pdf
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times", size=16)
    pdf.cell(w=0, h=20, txt='Relatório Receita e Despesas', ln=True, align='C')
    pdf.cell(w=0, h=16, txt='Tabela de Receitas', ln=True, align='C')

    with pdf.table() as table:
        for data_row in tabela_receitas:
            row = table.row()
            for datum in data_row:
                row.cell(datum)
    pdf.ln()

    pdf.cell(w=0, h=16, txt='Tabela de Despesas', ln=True, align='C')
    with pdf.table() as table:
        for data_row in tabela_despesas:
            row = table.row()
            for datum in data_row:
                row.cell(datum)
    pdf.ln()
    pdf.cell(w=0, h=16, txt=f'Total Receitas: R${total_receitas():.2f}', ln=True, align='C')
    pdf.cell(w=0, h=16, txt=f'Total Despesas: R${total_despesas():.2f}', ln=True, align='C')
    total_saldo=total_receitas()-total_despesas()
    pdf.cell(w=0, h=16, txt=f'Saldo restante: R${total_saldo:.2f}')
    pdf.output('RELATORIO_RECEITAS_DESPESAS.pdf')
    