from tkinter import *


receitas = {}
despesas = {}

def interface_receita():
    def add_receita():
        descricao= entrada1.get() #input('Informe a descrição da receita: ')
        data_receita=entrada2.get() #input('Informe o dia do recebimento: ')
        valor_recebimento =entrada3.get()  #float(input('Informe o valor do recebimento: '))
        tempo= entrada4.get() #int(input('Por quanto tempo vc ira receber: '))
        return receitas.update({descricao:[data_receita,valor_recebimento,tempo]})


    adReceitas=Tk()
    adReceitas.configure(background="#dde")
    adReceitas.geometry("500x500")
    adReceitas.title('Receitas')
    Button(adReceitas, text="Cadastrar",width=22, bg='white', fg='black',command=add_receita, font='None 14 bold').grid(row=8, column=0,columnspan=3, sticky=W)

    entrada1=Entry(adReceitas, width=25, bg='white')
    entrada1.grid(row=1, column=1, sticky=W)
    entrada2=Entry(adReceitas, width=25, bg='white')
    entrada2.grid(row=2, column=1, sticky=W)
    entrada3=Entry(adReceitas, width=25, bg='white')
    entrada3.grid(row=3, column=1, sticky=W)
    entrada4=Entry(adReceitas, width=25, bg='white')
    entrada4.grid(row=4, column=1, sticky=W)
    
    Label(adReceitas, text="Descrição da Receita").grid(row=1, column=0, sticky=W)
    Label(adReceitas, text="Dia do recebimento da receita").grid(row=2, column=0, sticky=W)
    Label(adReceitas, text="Valor").grid(row=3, column=0, sticky=W)
    Label(adReceitas, text="duração").grid(row=4, column=0, sticky=W)

    adReceitas.mainloop()
def interface_despesa():
    def add_despesas():
        descricao= str(entrada1.get)#input('Informe a descrição da despesa: ')
        data_receita= entrada2.get#input('Informe o dia do pagamento: ')
        valor_recebimento =entrada3.get #float(input('Informe o valor da despesa: '))
        tempo= entrada4.get#int(input('Por quanto tempo durara a fatura: '))
        return despesas.update({descricao:[data_receita,valor_recebimento,tempo]})
    
    addespesa=Tk()
    addespesa.configure(background="#dde")
    addespesa.geometry("500x500")
    addespesa.title('Receitas')
    Button(addespesa, text="Cadastrar",width=22, bg='white', fg='black',command=add_despesas, font='None 14 bold').grid(row=8, column=0,columnspan=3, sticky=W)

    entrada1=Entry(addespesa, width=25, bg='white')
    entrada1.grid(row=1, column=1, sticky=W)
    entrada2=Entry(addespesa, width=25, bg='white')
    entrada2.grid(row=2, column=1, sticky=W)
    entrada3=Entry(addespesa, width=25, bg='white')
    entrada3.grid(row=3, column=1, sticky=W)
    entrada4=Entry(addespesa, width=25, bg='white')
    entrada4.grid(row=4, column=1, sticky=W)
    
    Label(addespesa, text="Descrição da Despesa").grid(row=1, column=0, sticky=W)
    Label(addespesa, text="Dia do Pagamento").grid(row=2, column=0, sticky=W)
    Label(addespesa, text="Valor").grid(row=3, column=0, sticky=W)
    Label(addespesa, text="duração").grid(row=4, column=0, sticky=W)
    addespesa.mainloop()


def listagem(receitas= receitas,despesas= despesas):
    for keys, dados in receitas.items():
        data,valor,tempo=dados
        print(f'{keys},dia do recebimento {data},valor do recebimento {valor},esse recebimento durara {tempo} meses')
    for keys, dados in despesas.items():
        data,valor,tempo=dados
        print(f'{keys},dia do pagamento {data},valor do pagamento {valor},essa fatura durara {tempo} meses')

def total(receitas,despesas):
    for dados in receitas.values():
        data,valor,tempo = dados
        total_recebimento= valor*tempo

    for dados in despesas.values():
        data,valor,tempo=dados
        total_despesa= valor*tempo
    return total_recebimento,total_despesa

def interface_ex_receita():
    def exclusao_receita():
        
        receita_excluir= entrada1.get #input('Informe qual receita deseja excluir: ')
        chaves_a_excluir = []
        for chave in receitas.keys():
            if chave == receita_excluir :
                chaves_a_excluir.append(chave)
        for chave in chaves_a_excluir:
            del receitas[chave]


    ex_receita = Tk()
    ex_receita.configure(background='#dde')
    ex_receita.geometry('500x500')
    ex_receita.title('Exclusão de receita')
    entrada1=Entry(ex_receita, width=25, bg='white')
    entrada1.grid(row=1, column=1, sticky=W)
    Label(ex_receita, text="Descrição da receita: ").grid(row=1, column=0, sticky=W)
    Button(ex_receita, text="Excluir",width=22, bg='white', fg='black',command=exclusao_receita, font='None 14 bold').grid(row=8, column=0,columnspan=3, sticky=W)
    ex_receita.mainloop()





def interface_ex_despesas():
    def exclusao_despesas():
        despesas_excluir=entrada1.get #input('Informe qual receita deseja excluir: ')
        chaves_a_excluir = []

        for chave in despesas.keys():
            if despesas_excluir == chave:
                chaves_a_excluir.append(chave)

        for chave in chaves_a_excluir:
            del despesas[chave]


    ex_despesas = Tk()
    ex_despesas.configure(background='#dde')
    ex_despesas.geometry('500x500')
    ex_despesas.title('Exclusão de Despesas')
    entrada1=Entry(ex_despesas, width=25, bg='white')
    entrada1.grid(row=1, column=1, sticky=W)
    Label(ex_despesas, text="Descrição da Despesa").grid(row=1, column=0, sticky=W)
    Button(ex_despesas, text="Excluir",width=22, bg='white', fg='black',command=exclusao_despesas, font='None 14 bold').grid(row=8, column=0,columnspan=3, sticky=W)
    ex_despesas.mainloop()





'''
while True:
    print('-------------------------')
    print('|---------MENU----------|')
    print('| 1- -Adicionar receita-|')
    print('| 2- -Adicionar despesa-|')
    print('| 3- ----Listar Tudo----|')
    print('| 4- --Remover receita--|')
    print('| 5- --Remover despesa--|')
    print('| 6- ------Sair---------|')
    print('-------------------------')

    op = input('')
    match op:
      case '1':
          interface_receita()
      case '2':
          interface_despesa()
      case '3':
          listagem(receitas,despesas)
      case '4':
          interface_ex_receita()
      case '5':
          interface_ex_despesas()
      case '6':
          break
      case _:
          print('Opção invalida')
'''