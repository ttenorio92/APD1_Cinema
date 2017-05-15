salas = []

def adicionar_sala(cod_sala, lotacao):
    sala = [cod_sala, lotacao]
    salas.append(sala)
    
#def definir_status_ocupada(cod_sala)    

#def definir_status_livre(cod_sala)

def buscar_sala(cod_sala):
    for s in salas:
        if (s[0] == cod_sala):
            return s
        return None
        
def listar_salas(): 
    return salas

def remover_sala(cod_sala):
    for s in salas:
        if (s[0] == cod_salas):
            salas.remove(s)
        return True
    return False
    
def remover_todas_salas():
    global salas
    salas = []
    
def iniciar_salas():
    adicionar_sala(111, 4, 1, 20)
