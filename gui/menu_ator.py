# -*- coding: utf-8 -*-

from logica import ator


def imprimir_ator(ator):
    print ("Código: ",  ator[0])
    print ("Nome: ", ator[1])
    print ("Nacionalidade: ", ator[2])
    print ("Idade: ",  ator[3])
    print ()

def menu_adicionar():
    print ("\nAdicionar ator \n")
    cod_ator = int(input("Codigo: "))
    nome = str (input("Nome: "))
    nacionalidade = str (input("Nacionalidade: "))
    idade = int(input("Idade: "))
    ator.adicionar_ator(cod_ator, nome, nacionalidade, idade)

def menu_listar():
    print ("\nListar atores \n")
    atores = ator.listar_atores()
    for a in atores:
        imprimir_ator(a)


def menu_buscar():
    print ("\nBuscar ator por codigo\n")
    cod_ator = int(input("Codigo: "))
    a = ator.buscar_ator(cod_ator)
    if (a == None):
        print ("ator nao encontrado")
    else:
        imprimir_ator(a)
  
def menu_remover():
    print ("\nRemover ator \n")
    cod_ator = int(input("Codigo: "))
    a = ator.remover_ator(cod_ator)
    if (a == False):
        print ("ator nao encontrado")
    else:
        print ("ator removido")
    

def mostrar_menu():
    run_ator = True
    menu = ("\n----------------\n"+
             "(1) Adicionar novo ator \n" +
             "(2) Listar atores \n" +
             "(3) Buscar ator por codigo \n" +
             "(4) Remover ator  \n" +
             "(0) Voltar\n"+
            "----------------")
    
    while(run_ator):
        print (menu)
        op = int(input("Digite sua escolha: "))

        if (op == 1):
            menu_adicionar()
        elif(op == 2):
            menu_listar()
        elif(op == 3):       
            menu_buscar()
        elif (op == 4):
            menu_remover()
        elif (op == 0):
            run_medico = False

if __name__ == "__main__":
    mostrar_menu()
    
