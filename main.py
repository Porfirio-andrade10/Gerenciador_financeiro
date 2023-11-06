receitas = {}
despesas = {}

def add_receita():
    descricao= input('Informe a descrição da receita: ')
    data_receita= input('Informe o dia do recebimento: ')
    valor_recebimento =float(input('Informe o valor do recebimento: '))
    tempo= int(input('Por quanto tempo vc ira receber: '))
    return receitas.update({descricao:[data_receita,valor_recebimento,tempo]})

def add_despesas():
    descricao= input('Informe a descrição da despesa: ')
    data_receita= input('Informe o dia do pagamento: ')
    valor_recebimento =float(input('Informe o valor da despesa: '))
    tempo= int(input('Por quanto tempo durara a fatura: '))
    return despesas.update({descricao:[data_receita,valor_recebimento,tempo]})

def listagem(receitas,despesas):
    for keys, dados in receitas.items():
        data,valor,tempo=dados
        print(f'{keys},dia do recebimento {data},valor do recebimento {valor},esse recebimento durara {tempo}meses')
    for keys, dados in despesas.items():
        data,valor,tempo=dados
        print(f'{keys},dia do pagamento {data},valor do pagamento {valor},essa fatura durara {tempo}meses')

def total(receitas,despesas):
    for dados in receitas.values():
        data,valor,tempo = dados
        total_recebimento= valor*tempo

    for dados in despesas.values():
        data,valor,tempo=dados
        total_despesa= valor*tempo
    return total_recebimento,total_despesa

def exclusao_receita():
    receita_excluir=input('Informe qual receita deseja excluir: ')
    chaves_a_excluir = []

    for chave in receitas.keys():
        if receita_excluir == chave:
            chaves_a_excluir.append(chave)

    for chave in chaves_a_excluir:
        del receitas[chave]

def exclusao_despesas():
    despesas_excluir=input('Informe qual receita deseja excluir: ')
    chaves_a_excluir = []

    for chave in despesas.keys():
        if despesas_excluir == chave:
            chaves_a_excluir.append(chave)

    for chave in chaves_a_excluir:
        del despesas[chave]


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