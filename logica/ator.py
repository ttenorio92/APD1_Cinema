atores = []

def cadastrar_ator(cod_ator, nome, nacionalidade, idade):
    ator = [cod_ator, nome, nacionalidade, idade]
    atores.append(ator)

def buscar_ator(cod_ator):
    for a in atores:
        if (a[0] == cod_ator):
            return a
        return None

def remover_ator(cod_ator):
    for a in atores:
        if (a[0] == cod_ator):
            atores.remove(a)
        return True
    return False
    
def remover_todos_atores():
    global atores
    atores = []
    
def iniciar_atores():
    cadastrar_ator(111, 'Edson', 'Brasileiro', 30 )

