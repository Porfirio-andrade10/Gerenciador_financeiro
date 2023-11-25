import PySimpleGUI as sg
from main import *

def interface_cadastro():

    layout_cadastro = [

        [sg.Text('Cadastro de Receitas:', font=('Helvetica', 14, 'bold'))],
        [sg.Text('Descrição da Receita:   '), sg.InputText(key='-DESCRICAO_RECEITA-', size=(30, 1))],
        [sg.Text('Valor da Receita:          '), sg.InputText(key='-VALOR_RECEITA-', size=(30, 1))],
        [sg.Text('Dia do Recebimento:     '), sg.InputText(key='-DIA_RECEBIMENTO-', size=(30, 1))],
        [sg.Text('Por quanto tempo durar:'), sg.InputText(key='-TEMPO_RECEBIMENTO-', size=(30, 1))],
        [sg.Button('Cadastrar:', key='-CADASTRAR_RECEITA-', size=(12, 1), button_color=('white', 'green'))],
        [sg.Text('Receitas:', font=('Helvetica', 12, 'bold'))],
        [sg.Multiline(size=(60, 5), key='-LISTA_RECEITAS-')],
        [sg.HorizontalSeparator(color='black')],
        [sg.Text('Cadastro de Despesas', font=('Helvetica', 14, 'bold'))],
        [sg.Text('Descrição da Despesa: '), sg.InputText(key='-DESCRICAO_DESPESA-', size=(30, 1))],
        [sg.Text('Valor da Despesa:        '), sg.InputText(key='-VALOR_DESPESA-', size=(30, 1))],
        [sg.Text('Dia do Pagamento:       '), sg.InputText(key='-DIA_PAGAMENTO-', size=(30, 1))],
        [sg.Text('Por quanto tempo durar:'), sg.InputText(key='-TEMPO_PAGAMENTO-', size=(30, 1))],
        [sg.Button('Cadastrar', key='-CADASTRAR_DESPESA-', size=(12, 1), button_color=('white', 'red'))],
        [sg.Text('Despesas:', font=('Helvetica', 12, 'bold'))],
        [sg.Multiline(size=(60, 5), key='-LISTA_DESPESAS-')],
        [sg.Text('', key='-RESULTADO-', size=(30, 1))],
        [sg.Button('Calcular Receita Total', key='-CALCULAR_RECEITA_TOTAL-', size=(20, 1),),
        sg.Button('Calcular Despesas Total', key='-CALCULAR_DESPESAS_TOTAL-', size=(20, 1),),
        sg.Button('Sair', key='-SAIR-', size=(8, 1), )],

    ]
    cadastro_window = sg.Window('Gerenciador Financeiro', layout_cadastro,)

    while True:
        event, values = cadastro_window.read()

        if event == sg.WIN_CLOSED or event == "-SAIR-":
            break
        elif event == '-CADASTRAR_RECEITA-':
            cadastro_window['-LISTA_RECEITAS-'].update('')
            add_receita(x=values['-DESCRICAO_RECEITA-'],y=values['-VALOR_RECEITA-'],z=values['-DIA_RECEBIMENTO-'],a=values['-TEMPO_RECEBIMENTO-'])
            for keys, dados in receitas.items():
                data,valor,tempo=dados
                cadastro_window['-LISTA_RECEITAS-'].print(f'Descrição: {keys},Dia do Recebimento: {data} ,Valor: {valor:.2f} ,Duração: {tempo} meses')
            cadastro_window['-DESCRICAO_DESPESA-'].update('')   
            
        elif event == '-CADASTRAR_DESPESA-':  
            cadastro_window['-LISTA_DESPESAS-'].update('')
            add_despesas(x=values['-DESCRICAO_DESPESA-'],y=values['-VALOR_DESPESA-'],z=values['-DIA_PAGAMENTO-'],a=values['-TEMPO_PAGAMENTO-'])
            for keys, dados in despesas.items():
                data,valor,tempo=dados
                cadastro_window['-LISTA_DESPESAS-'].print(f'Descrição: {keys},Dia do Pagamento: {data} ,Valor {valor:.2f} ,Duração: {tempo} meses')
        
        elif event == '-CALCULAR_RECEITA_TOTAL-':
            resultado=total_receitas()
            cadastro_window['-RESULTADO-'].update(f'O total de receita é de R$: {resultado:.2f}')
        elif event == '-CALCULAR_DESPESAS_TOTAL-':
            resultado1=total_despesas()
            cadastro_window['-RESULTADO-'].update(f'O total de despesa é de R$: {resultado1:.2f}')
    cadastro_window.close()
            
def interface_remover():

    layout_remover=[
        [sg.Text('Remover Receita/Despesa', font=('Helvetica', 14, 'bold'))],
        [sg.Text('Descrição da Receita que deseja excluir'),sg.InputText(key='-DESCRICAO_RECEITA-',size=(30,1))],
        [sg.Button('Excluir',key='-EXCLUIR_RECEITA-',size=(20,1))],
        [sg.Text('Receitas exluidas:', font=('Helvetica', 14, 'bold'))],
        [sg.Multiline(size=(60, 5),key='-LISTA_RECEITAS_EX-')],
        [sg.Text('Descrição da Despesa que deseja excluir'),sg.InputText(key='-DESCRICAO_DESPESA-',size=(30,1))],
        [sg.Button('Excluir',key='-EXCLUIR_DESPESA-',size=(20,1))],
        [sg.Text('Despesas exluidas:', font=('Helvetica', 14, 'bold'))],
        [sg.Multiline(size=(60, 5),key='-LISTA_DESPESAS_EX-')],
        [sg.Button('Sair', key='-SAIR-', size=(8, 1), )]
    ]

    remover_window=sg.Window('REMOÇÃO',layout_remover)

    while True:
        event,values = remover_window.read()

        if event ==  sg.WIN_CLOSED or event=='-SAIR-':
            break 

        elif event== '-EXCLUIR_RECEITA-':
            iten_excluido={}
            entrada=values['-DESCRICAO_RECEITA-']
            iten_excluido.update({entrada:exclusao_receita(X=values['-DESCRICAO_RECEITA-'])})
            print(iten_excluido)
            for keys, dados in iten_excluido.items():
                if dados is not None:
                    data,valor,tempo=dados
                    remover_window['-LISTA_RECEITAS_EX-'].print(f'Descrição: {keys},Dia do Pagamento: {data} ,Valor {valor:.2f} ,Duração: {tempo} meses')
                else:
                    break
        
        elif event== '-EXCLUIR_DESPESA-':
            iten_excluido={}
            entrada=values['-DESCRICAO_DESPESA-']
            iten_excluido.update({entrada:exclusao_despesas(X=values['-DESCRICAO_DESPESA-'])})
            for keys, dados in iten_excluido.items():
                if dados is not None:
                    data,valor,tempo=dados
                    remover_window['-LISTA_DESPESAS_EX-'].print(f'Descrição: {keys},Dia do Pagamento: {data} ,Valor {valor:.2f} ,Duração: {tempo} meses')
                else:
                    break
    

    remover_window.close()




layout_menu=[

    [sg.Text('MENU', font=('Helvetica', 16, 'bold'))],
    [sg.Button('Cadastrar receitas/ Despesas',size=(50,0))],
    [sg.Button('Remover receitas/ Despesas',size=(50,0))],
    [sg.Button('Imprimir',size=(50,0))],
    [sg.Text(size=(50, 0),key='-LISTA_RECEITAS')],
    [sg.Button('Listar Receitas', key='-LISTAGEM_RECEITAS-', size=(50, 0))],
    [sg.Multiline(size=(50, 3),key='-LISTA_RECEITAS-')],
    [sg.Button('Listar Despesas', key='-LISTAGEM_DESPESA-', size=(50, 0))],
    [sg.Multiline(size=(50, 3),key='-LISTA_DESPESAS-')],
    [sg.Button('Sair', key='-SAIR-', size=(50, 0))]
]



janela_menu = sg.Window('Gerenciador financeiro',layout_menu, size=(500, 500), element_justification='center' )
while True:
    event, values = janela_menu.read()
    if event == sg.WIN_CLOSED or event == '-SAIR-': 
        break
    elif event == 'Cadastrar receitas/ Despesas':
        interface_cadastro()
    elif event == 'Remover receitas/ Despesas':
        interface_remover()
    elif event == '-LISTAGEM_RECEITAS-':
        x= listagem_receitas()
        if x is not None:
            janela_menu['-LISTA_RECEITAS-'].update('')
            for keys, dados in receitas.items():
                data,valor,tempo=dados
                janela_menu['-LISTA_RECEITAS-'].print(f'Descrição: {keys},Dia do Recebimento: {data} ,Valor: {valor} ,Duração: {tempo} meses')

        else:
            janela_menu['-LISTA_RECEITAS-'].update('')

    elif event == '-LISTAGEM_DESPESA-':
        x=listagem_despesas()
        if x is not None:
            janela_menu['-LISTA_DESPESAS-'].update('')
            for keys, dados in despesas.items():
                data,valor,tempo=dados
                janela_menu['-LISTA_DESPESAS-'].print(f'Descrição: {keys},Dia do Pagamento: {data} ,Valor: {valor} ,Duração: {tempo} meses')
        else:
            janela_menu['-LISTA_DESPESAS-'].update('')
janela_menu.close()