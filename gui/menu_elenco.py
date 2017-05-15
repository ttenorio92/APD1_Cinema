# -*- coding: utf-8 -*-

from logica import elenco
     

def imprimir_elenco(elenco):
    print ("Código do Elenco: ", elenco[0])
    print ("Codigo do Ator: ", elenco[1])
    print ("Codigo do Filme:", elenco[2])
    print ("Tipo:",  elenco[3])
    print ()

def menu_adicionar():
    print ("\nAdicionar elenco \n")
    cod_elenco = int(input("Codigo do Elenco: "))
    cod_ator = int(input("Codigo do Ator: "))
    cod_filme = (input("Codigo do Filme: "))
    tipo = str(input("Tipo: "))
    elenco.adicionar_elenco(cod_elenco,cod_ator, cod_filme, tipo )

def menu_listar():
    print ("\nListar elencos \n")
    elenco = elenco.listar_elencos()
    for e in elencos:
        imprimir_elenco(e)


def menu_buscar():
    print ("\nBuscar elenco por codigo\n")
    cod_elenco = int(input("Codigo do Elenco: "))
    e = elenco.buscar_elenco(cod_elenco)
    if (e == None):
        print ("elenco nao encontrado")
    else:
        imprimir_elenco(e)
  
def menu_remover():
    print ("\nRemover elenco \n")
    cod_elenco = int(input("Codigo do Elenco: "))
    e = elenco.remover_elenco(cod_elenco)
    if (e == False):
        print ("elenco nao encontrado")
    else:
        print ("elenco removido")
    

def mostrar_menu():
    run_elenco = True
    menu = ("\n----------------\n"+
             "(1) Adicionar novo elenco \n" +
             "(2) Listar elencos \n" +
             "(3) Buscar elenco por codigo \n" +
             "(4) Remover elenco  \n" +
             "(0) Voltar\n"+
            "----------------")
    
    while(run_elenco):
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
    