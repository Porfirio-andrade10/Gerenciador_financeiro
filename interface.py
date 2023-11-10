import PySimpleGUI as sg


layout_menu=[
    [sg.Text('MENU', font=('Helvetica', 16, 'bold'))],
    [sg.Button('Cadastrar receitas/ Despesas',size=(50,0))],
    [sg.Button('Remover receitas/ Despesas',size=(50,0))],
    [sg.Button('Imprimir',size=(50,0))],
    [sg.Text('',)],  
]


janela_menu = sg.Window('Gerenciador financeiro',layout_menu, size=(300, 300), element_justification='center' )
while True:
    event, values = janela_menu.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': 
        break
    

janela_menu.close()