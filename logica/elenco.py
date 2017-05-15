# -*- coding: utf-8 -*-

import ator
import filme

elencos = []

def adicionar_ator(cod_elenco, cod_ator, cod_filme, tipo):
    elenco = [cod_elenco, cod_ator, cod_filme, tipo]
    elencos.append(elenco)

#def consultar_atores_por_filme(cod_elenco)
#    pass

def buscar_elenco(cod_elenco):
    for e in elencos:
        if (e[0] == cod_elenco):
            return e
        return None
#def buscar_elenco_por_filme()
#    pass

def remover_elenco(cod_elenco):
    for e in elencos:
        if (e[0] == cod_elenco):
            elencos.remove(e)
        return True
    return False
    
def remover_todos_elencos():
    global elencos
    elencos = []
    
def iniciar_elencos():
    cadastrar_elenco(1234, 1111, 4, "Suspense")