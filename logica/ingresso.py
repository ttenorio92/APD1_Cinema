ingressos = []

def listar_ingressos():
    return ingressos

def buscar_ingresso(cod_ingresso):
    for i in ingressos :
        if (i[0] == cod_ingresso):
            return i    
        return None
        
def remover_ingresso(cod_ingresso):
    for i in ingressos:
        if (i[0] == cod_ingresso):
            ingressos.remove(i)
        return True
    return False       

def remover_todos_ingressos():
    global ingressos
    ingressos = []  
    
def iniciar_ingresso():
    iniciar_ingressos(111)    
        
        