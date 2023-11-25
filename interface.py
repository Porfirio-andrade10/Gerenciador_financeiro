# Importa a biblioteca PySimpleGUI para a criação de interfaces gráficas simples
import PySimpleGUI as sg
# Importa funcionalidades do módulo Gerenciador
from main import *

# Define o tema visual da interface gráfica
sg.theme('DarkBlue')

# Calcular o total de receitas e despesas
total_receitas_inicial = total_receitas()
total_despesas_inicial = total_despesas()
saldo_inicial = total_receitas_inicial - total_despesas_inicial

# Definir cores para os totais na interface
cor_receitas = 'green'
cor_despesas = 'red'

# Define a função para criar a interface de pesquisa
def interface_pesquisa():
    # Layout para a interface de pesquisa
    layout_pesquisa = [
        [sg.Text('Pesquisar Receitas/Despesas', font=('Helvetica', 14, 'bold'))],
        [sg.Text('Digite a descrição:'), sg.InputText(key='-DESCRICAO_PESQUISA-', size=(30, 1))],
        [sg.Button('Pesquisar', key='-PESQUISAR-', size=(12, 1))],
        [sg.Text('Resultados:', font=('Helvetica', 12, 'bold'))],
        [sg.Multiline(size=(60, 5), key='-LISTA_PESQUISA-')],
        [sg.Button('Sair', size=(8, 1))],
    ]
    # Cria uma janela para a interface de pesquisa
    pesquisa_window = sg.Window('Pesquisa de Receitas e Despesas', layout_pesquisa)

    while True:
        event, values = pesquisa_window.read()
        # Verifica se a janela foi fechada ou o botão 'Sair' foi pressionado
        if event == sg.WIN_CLOSED or event == 'Sair':
            break
        # Verifica se o botão 'Pesquisar' foi pressionado
        elif event == '-PESQUISAR-':
            descricao_pesquisa = values['-DESCRICAO_PESQUISA-'].strip().lower()

            # Chame a função de pesquisa
            resultados_receitas, resultados_despesas = pesquisar_por_descricao(descricao_pesquisa)

            # Atualizar a lista na interface
            pesquisa_window['-LISTA_PESQUISA-'].update('')
            
        # Adiciona os resultados de receitas à lista na interface
        for resultado in resultados_receitas:
            data_formatado = f"R$ {float(resultado[2]):.2f}" if isinstance(resultado[2], (float, int)) else resultado[2]
            linha_receita = f'Receita - Descrição: {resultado[1]}, Dia: {data_formatado}, Valor: {resultado[3]:.2f}'
            pesquisa_window['-LISTA_PESQUISA-'].print(linha_receita)
        # Adiciona os resultados de despesas à lista na interface
        for resultado in resultados_despesas:
            data_formatado = f"R$ {float(resultado[2]):.2f}" if isinstance(resultado[2], (float, int)) else resultado[2]
            linha_despesa = f'Despesa - Descrição: {resultado[1]}, Dia: {data_formatado}, Valor: {resultado[3]:.2f}'
            pesquisa_window['-LISTA_PESQUISA-'].print(linha_despesa)

    pesquisa_window.close()

# Define a função para criar a interface de cadastro
def interface_cadastro():
    # Layout para a interface de cadastro
    layout_cadastro = [
        [sg.Text('Cadastro de Receitas:', font=('Helvetica', 14, 'bold'))],
        [sg.Text('Descrição da Receita:   '), sg.InputText(key='-DESCRICAO_RECEITA-', size=(30, 1))],
        [sg.Text('Valor da Receita:          '), sg.InputText(key='-VALOR_RECEITA-', size=(30, 1))],
        [sg.Text('Dia do Recebimento:     '), sg.InputText(key='-DIA_RECEBIMENTO-', size=(30, 1))],
        [sg.Button('Cadastrar:', key='-CADASTRAR_RECEITA-', size=(12, 1), button_color=('white', 'green'))],
        [sg.Text('Receitas:', font=('Helvetica', 12, 'bold'))],
        [sg.Multiline(size=(60, 5), key='-LISTA_RECEITAS-')],
        [sg.HorizontalSeparator(color='black')],
        [sg.Text('Cadastro de Despesas', font=('Helvetica', 14, 'bold'))],
        [sg.Text('Descrição da Despesa: '), sg.InputText(key='-DESCRICAO_DESPESA-', size=(30, 1))],
        [sg.Text('Valor da Despesa:        '), sg.InputText(key='-VALOR_DESPESA-', size=(30, 1))],
        [sg.Text('Dia do Pagamento:        '), sg.InputText(key='-DIA_PAGAMENTO-', size=(30, 1))],
        [sg.Button('Cadastrar', key='-CADASTRAR_DESPESA-', size=(12, 1), button_color=('white', 'red'))],
        [sg.Text('Despesas:', font=('Helvetica', 12, 'bold'))],
        [sg.Multiline(size=(60, 5), key='-LISTA_DESPESAS-')],
        [sg.Text('', key='-RESULTADO-', size=(30, 1))],
        [sg.Button('Calcular Receita Total', key='-CALCULAR_RECEITA_TOTAL-', size=(20, 1),),
        sg.Button('Calcular Despesas Total', key='-CALCULAR_DESPESAS_TOTAL-', size=(20, 1),),
        sg.Button('Sair', key='-SAIR-', size=(8, 1), )],
    ]
    
    # Cria uma janela para a interface de cadastro
    cadastro_window = sg.Window('Gerenciador Financeiro', layout_cadastro)

    while True:
        event, values = cadastro_window.read()
        # Verifica se a janela foi fechada ou o botão 'Sair' foi pressionado
        if event == sg.WIN_CLOSED or event == "-SAIR-":
            break
        # Verifica se o botão 'Cadastrar Receita' foi pressionado
        elif event == '-CADASTRAR_RECEITA-':
            descricao = values['-DESCRICAO_RECEITA-']
            dia_recebimento = values['-DIA_RECEBIMENTO-']
            valor_recebimento = values['-VALOR_RECEITA-']
            # Chama a função para cadastrar a receita com os valores fornecidos
            add_receita(descricao, dia_recebimento, valor_recebimento)
            
            # Atualizar a lista na interface
            cadastro_window['-LISTA_RECEITAS-'].update('')
            for receita in listagem_receitas():
                cadastro_window['-LISTA_RECEITAS-'].print(f'Descrição: {receita[0]}, Dia do Recebimento: {receita[1]}, Valor: {receita[2]:.2f}')
            
            # Limpar os campos
            cadastro_window['-DESCRICAO_DESPESA-'].update('')   
        # Verifica se o botão 'Cadastrar Despesa' foi pressionado
        elif event == '-CADASTRAR_DESPESA-':
            descricao = values['-DESCRICAO_DESPESA-']
            dia_pagamento = values['-DIA_PAGAMENTO-']
            valor_despesa = values['-VALOR_DESPESA-']
            add_despesas(descricao, dia_pagamento, valor_despesa)
            
            # Atualizar a lista na interface
            cadastro_window['-LISTA_DESPESAS-'].update('')
            for despesa in listagem_despesas():
                cadastro_window['-LISTA_DESPESAS-'].print(f'Descrição: {despesa[0]}, Dia do Pagamento: {despesa[1]}, Valor: {despesa[2]:.2f}')
        # Verifica se o botão 'Calcular Receita Total' foi pressionado
        elif event == '-CALCULAR_RECEITA_TOTAL-':
            # Calcula o total de receitas
            resultado = total_receitas()
            # Atualiza o campo de resultado na interface
            cadastro_window['-RESULTADO-'].update(f'O total de receita é de R$: {resultado:.2f}')
        # Verifica se o botão 'Calcular Despesas Total' foi pressionado
        elif event == '-CALCULAR_DESPESAS_TOTAL-':
            resultado1 = total_despesas()
            # Atualiza o campo de resultado na interface
            cadastro_window['-RESULTADO-'].update(f'O total de despesa é de R$: {resultado1:.2f}')
    # Fecha a janela de cadastro ao sair do loop
    cadastro_window.close()

# Define a função para criar a interface de remoção
def interface_remover():
    # Layout para a interface de remoção
    layout_remover = [
        [sg.Text('Remover Receita/Despesa', font=('Helvetica', 14, 'bold'))],
        [sg.Text('Receitas:', font=('Helvetica', 12, 'bold'))],
        [sg.Listbox(values=listagem_receitas(), size=(60, 5), key='-LISTA_RECEITAS-', enable_events=True)],
        [sg.Text('Despesas:', font=('Helvetica', 12, 'bold'))],
        [sg.Listbox(values=listagem_despesas(), size=(60, 5), key='-LISTA_DESPESAS-', enable_events=True)],
        [sg.Button('Excluir Receita', key='-EXCLUIR_RECEITA-', size=(20, 1))],
        [sg.Button('Excluir Despesa', key='-EXCLUIR_DESPESA-', size=(20, 1))],
        [sg.Button('Sair', key='-SAIR-', size=(8, 1))],
    ]
    # Cria uma janela para a interface de remoção
    remover_window = sg.Window('REMOÇÃO', layout_remover)
    # Loop principal para a interface de remoção
    while True:
        event, values = remover_window.read()
        # Verifica se a janela foi fechada ou o botão 'Sair' foi pressionado
        if event == sg.WIN_CLOSED or event == '-SAIR-':
            break
        # Verifica se o botão 'Excluir Receita' foi pressionado
        elif event == '-EXCLUIR_RECEITA-':
            # Verifica se há uma receita selecionada na lista
            if values['-LISTA_RECEITAS-']:
                descricao_selecionada = values['-LISTA_RECEITAS-'][0]
                # Chama a função para excluir a receita com a descrição selecionada
                exclusao_receita(descricao_selecionada)

                # Atualizar a lista na interface
                remover_window['-LISTA_RECEITAS-'].update(values=listagem_receitas())
        # Verifica se o botão 'Excluir Despesa' foi pressionado
        elif event == '-EXCLUIR_DESPESA-':
            # Verifica se há uma despesa selecionada na lista
            if values['-LISTA_DESPESAS-']:
                descricao_selecionada = values['-LISTA_DESPESAS-'][0]
                # Chama a função para excluir a despesa com a descrição selecionada
                exclusao_despesa(descricao_selecionada)

                # Atualizar a lista na interface
                remover_window['-LISTA_DESPESAS-'].update(values=listagem_despesas())
    # Fecha a janela de remoção ao sair do loop
    remover_window.close()

# Define a função para criar uma tabela formatada com receitas e despesas
def criar_tabela_dados(receitas, despesas):
    # Cria o cabeçalho da tabela
    header = ['Descrição', 'Dia', 'Valor',]
    # Inicializa listas para armazenar os dados formatados
    data_receitas = []
    data_despesas = []
    # Formata os dados das receitas
    for receita in receitas:
        data_receitas.append([receita[0], receita[1], f'R$ {receita[2]:.2f}', sg.Button('Excluir', key=f'-EXCLUIR_RECEITA_{receita[0]}-')])
    # Formata os dados das despesas
    for despesa in despesas:
        data_despesas.append([despesa[0], despesa[1], f'R$ {despesa[2]:.2f}', sg.Button('Excluir', key=f'-EXCLUIR_DESPESA_{despesa[0]}-')])
    # Define o layout da tabela
    layout = [
        [sg.Text('Receitas:', font=('Helvetica', 12, 'bold'))],
        [sg.Table(values=data_receitas, headings=header, auto_size_columns=False, justification='right', num_rows=min(25, len(data_receitas)))],
        [sg.Text('Despesas:', font=('Helvetica', 12, 'bold'))],
        [sg.Table(values=data_despesas, headings=header, auto_size_columns=False, justification='right', num_rows=min(25, len(data_despesas)))],
        [sg.Button('OK')]
    ]
    # Cria uma janela para a listagem de receitas e despesas
    window = sg.Window('Listagem de Receitas e Despesas', layout, resizable=True, finalize=True)
    # Loop principal para a interface de listagem
    while True:
        event, values = window.read()
        # Verifica se a janela foi fechada ou o botão 'OK' foi pressionado
        if event == sg.WINDOW_CLOSED or event == 'OK':
            break

        # Tratar eventos de exclusão
        if event.startswith('-EXCLUIR_RECEITA_'):
            # Extrai a descrição selecionada a partir da chave do botão
            descricao_selecionada = event.split('_')[-1]
            # Chama a função para excluir a receita com a descrição selecionada
            exclusao_receita(descricao_selecionada)
            # Atualiza a lista de receitas na interface
            window['-LISTA_RECEITAS-'].update(values=listagem_receitas())

        elif event.startswith('-EXCLUIR_DESPESA_'):
            # Extrai a descrição selecionada a partir da chave do botão
            descricao_selecionada = event.split('_')[-1]
            # Chama a função para excluir a despesa com a descrição selecionada
            exclusao_despesa(descricao_selecionada)
            # Atualiza a lista de despesas na interface
            window['-LISTA_DESPESAS-'].update(values=listagem_despesas())
    # Fecha a janela de listagem
    window.close()

# Define o layout do menu
layout_menu = [
    [sg.Text('MENU', font=('Helvetica', 16, 'bold'))],
    [sg.Button('Cadastrar receitas/ Despesas', size=(50, 0))],
    [sg.Button('Remover receitas/ Despesas', size=(50, 0))],
    [sg.Button('Listar Receitas e Despesas', size=(50, 0))],
    [sg.Button('Pesquisar Receitas/Despesas', size=(50, 0))],
    [sg.Button('Gerar PDF',key='gerar_pdf',size=(50,0))],
    [sg.Button('Sair', key='-SAIR-', size=(50, 0))]
]
# Cria uma janela para o menu
janela_menu = sg.Window('Gerenciador financeiro', layout_menu, size=(500, 500), element_justification='center' )


# Loop principal para a interface do menu
while True:
    event, values = janela_menu.read()
    # Verifica se a janela foi fechada ou o botão 'Sair' foi pressionado
    if event == sg.WIN_CLOSED or event == '-SAIR-':
        break

    # Trata os eventos dos botões do menu
    elif event == 'Cadastrar receitas/ Despesas':
        interface_cadastro()

    elif event == 'Remover receitas/ Despesas':
        interface_remover()

    elif event == 'Listar Receitas e Despesas':
        # Obtém a lista de receitas e despesas
        x_receitas = listagem_receitas()
        x_despesas = listagem_despesas()
        # Cria uma tabela com os dados
        criar_tabela_dados(x_receitas, x_despesas)

    elif event == 'Pesquisar Receitas/Despesas':
        # Chama a interface de pesquisa
        interface_pesquisa()

    elif event == 'gerar_pdf':
        imprimir_pdf()

# Fecha a janela do menu ao sair do loop
janela_menu.close()