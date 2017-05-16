sessoes = []

def criar_sessao(cod_sessao, cod_filme, cod_sala, horario):
    sessao = [cod_sessao, cod_filme, cod_sala, horario]
    sessoes.append(sessao)

#def recuperar_sessao(cod_sessao)

#def verificar_lotacao(cod_sessao)

def listar_sessoes(): 
    return sessoes  

def remover_sessao(cod_sessao):
    for se in sessoes:
        if (se[0] == cod_sessao):
            sessoes.remove(se)
        return True
    return False

def iniciar_atores():
    cadastrar_ator(111, 'Edson', 'Brasileiro', 30 )
