# -*- coding: utf-8 -*-

from logica import sala


def imprimir_sala(sala):
    print ("Código: ",  sala[0])
    print ("Lotacao ", sala[1])
    print ()

def menu_adicionar():
    print ("\nAdicionar sala \n")
    cod_sala = int(input("Codigo: "))
    lotacao = int (input("Lotacao: "))
    sala.adicionar_sala(cod_sala, lotacao)

def menu_listar():
    print ("\nListar salas \n")
    salas = sala.listar_salas()
    for s in salas:
        imprimir_sala(s)


def menu_buscar():
    print ("\nBuscar sala por codigo\n")
    cod_sala = int(input("Codigo: "))
    s = sala.buscar_sala(cod_sala)
    if (s == None):
        print ("sala nao encontrado")
    else:
        imprimir_sala(s)
  
def menu_remover():
    print ("\nRemover sala \n")
    cod_sala = int(input("Codigo: "))
    s = sala.remover_sala(cod_sala)
    if (s == False):
        print ("sala nao encontrada")
    else:
        print ("sala removida")
    

def mostrar_menu():
    run_sala = True
    menu = ("\n----------------\n"+
             "(1) Adicionar nova sala \n" +
             "(2) Listar salas \n" +
             "(3) Buscar sala por codigo \n" +
             "(4) Remover sala  \n" +
             "(0) Voltar\n"+
            "----------------")
    
    while(run_sala):
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
    