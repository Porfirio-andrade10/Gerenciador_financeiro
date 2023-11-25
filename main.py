receitas = {}
despesas = {}


def add_receita(x,y,z,a):
    descricao= x #DESCRICAO RECEITA
    data_receita=y  #dia do recebimento 
    valor_recebimento =float(z)#(input('Informe o valor do recebimento: '))
    tempo= int(a) #int(input('Por quanto tempo vc ira receber: '))
    return receitas.update({descricao:[data_receita,valor_recebimento,tempo]})

def add_despesas(x,y,z,a):
    descricao=x #input('Informe a descrição da despesa: ')
    data_receita=y #input('Informe o dia do pagamento: ')
    valor_recebimento =float(z) #float(input('Informe o valor da despesa: '))
    tempo=int (a) #int(input('Por quanto tempo durara a fatura: '))
    return despesas.update({descricao:[data_receita,valor_recebimento,tempo]})

def listagem_receitas(receitas=receitas):
    for keys, dados in receitas.items():
        data,valor,tempo=dados
        listagem=(f'Descrição: {keys},Dia do Recebimento: {data} ,Valor: {valor} ,Duração: {tempo} meses')
        return listagem
def listagem_despesas(despesas=despesas):        
    for keys, dados in despesas.items():
        data,valor,tempo=dados
        listagem =(f'{keys},dia do pagamento {data} ,valor do pagamento {valor} ,essa fatura durara {tempo}meses')
        return listagem

def total_receitas(receitas=receitas):
    total_recebimento=0
    for dados in receitas.values():
        data,valor,tempo = dados
        mult = (valor*tempo)
        total_recebimento +=mult
    return total_recebimento

def total_despesas(despesas=despesas):
    total_despesa=0
    for dados in despesas.values():
        data,valor,tempo=dados
        mult= valor*tempo
        total_despesa+=mult
    return total_despesa

def exclusao_receita(X):
    receita_excluir= X    #input('Informe qual receita deseja excluir: ')
    chaves_a_excluir = []

    for chave in receitas.keys():
        if receita_excluir == chave:
            chaves_a_excluir.append(chave)

    for chave in chaves_a_excluir:
        iten_excluido=receitas.pop(chave)
        return iten_excluido

def exclusao_despesas(X):
    despesas_excluir=X #input('Informe qual receita deseja excluir: ')
    chaves_a_excluir = []

    for chave in despesas.keys():
        if despesas_excluir == chave:
            chaves_a_excluir.append(chave)

    for chave in chaves_a_excluir:
        iten_excluido=despesas.pop(chave)
        return iten_excluido
    
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
          add_receita()
      case '2':
          add_despesas()
      case '3':
          listagem(receitas,despesas)
      case '4':
          exclusao_receita()
      case '5':
          exclusao_despesas()
      case '6':
          break
      case _:
          print('Opção invalida')
'''