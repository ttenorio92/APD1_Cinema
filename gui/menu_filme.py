# -*- coding: utf-8 -*-

from logica import filme


def imprimir_filme(filme):
    print ("Código: ",  filme[0])
    print ("Título: ", filme[1])
    print ("Duraçao: ", filme[2])
    print ("Classificação: ", filme[3])
    print ("Diretor: ", filme[4])
    print ("Distribuidora: ", filme[5])
    print ("status: ", filme[6])
    print ("Genero: ", filme[7])
    print ()

def menu_adicionar():
    print ("\nAdicionar filme \n")
    cod_filme = int(input("Codigo: "))
    titulo = str (input("Titulo: "))
    duracao = str (input("Duração: "))
    classificação = int(input("Classificação: "))
    diretor = int(input("Diretor: "))
    distribuidora = int(input("Distribuidora: "))
    status = (input("Status: "))
    genero = (input("Genero: "))
    filme.adicionar_filme(cod_filme, titulo, duracao, classificacao, diretor, distribuidora, status, genero)

def menu_listar():
    print ("\nListar filmes \n")
    filmes = filme.listar_filmes()
    for f in filmes:
        imprimir_filme(f)


def menu_buscar():
    print ("\nBuscar filme por codigo\n")
    cod_filme = int(input("Codigo: "))
    f = filme.buscar_filme(cod_filme)
    if (f == None):
        print ("filme nao encontrado")
    else:
        imprimir_filme(f)
  
def menu_remover():
    print ("\nRemover filme \n")
    cod_filme = int(input("Codigo: "))
    f = filme.remover_filme(cod_filme)
    if (f == False):
        print ("filme nao encontrado")
    else:
        print ("filme removido")
    

def mostrar_menu():
    run_filme = True
    menu = ("\n----------------\n"+
             "(1) Adicionar novo filme \n" +
             "(2) Listar filmes \n" +
             "(3) Buscar filme por codigo \n" +
             "(4) Remover filme  \n" +
             "(0) Voltar\n"+
            "----------------")
    
    while(run_filme):
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
    

