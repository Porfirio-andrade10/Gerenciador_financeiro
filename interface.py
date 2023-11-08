from tkinter import *
from main import interface_receita, interface_despesa, listagem, interface_ex_receita, interface_ex_despesas



menu= Tk()
menu.configure(background="#dde")
menu.geometry("500x500")
menu.title('Gerenciamento Financeiro')

Label(menu, text="MENU Gerenciamento Financeiro",width=35, bg='#dde', fg='black', font='None 14 bold').grid(row=1, column=0,columnspan=3, sticky=W, padx=50, pady=5)
Button(menu, text="Adicionar Receita",width=35, bg='white', fg='black',command=interface_receita, font='None 12 ').grid(row=2, column=0, sticky=W, padx=100, pady=5)
Button(menu, text="Adicionar Dispesa",width=35, bg='white', fg='black',command=interface_despesa, font='None 12 ').grid(row=3, column=0, sticky=W, padx=100, pady=5)
Button(menu, text="Consulta",width=35, bg='white', fg='black',command=listagem, font='None 12 ').grid(row=4, column=0, sticky=W, padx=100, pady=5)
Button(menu, text="Remover Receita",width=35, bg='white', fg='black',command=interface_ex_receita, font='None 12 ').grid(row=5, column=0, sticky=W, padx=100, pady=5)
Button(menu, text="Remover Dispesa",width=35, bg='white', fg='black',command=interface_ex_despesas, font='None 12 ').grid(row=6, column=0, sticky=W, padx=100, pady= 5)
'''Button(menu, text="sair",width=9, bg='white', fg='black',command=break, font='None 12 ').grid(row=2, column=5, sticky=W, padx=150, pady=5)''' 

menu.mainloop()

