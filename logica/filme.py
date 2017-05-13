# -*- coding: utf-8 -*-

filmes = []

def adicionar_filme(cod_filme, titulo, duracao, classificacao, diretor, distribuidora, status, genero):
    filmes.append(filme)

def listar_filmes():
    return filmes

def buscar_filme(cod_filme):
    for f in filmes:
        if (f[0] == cod_filme):
            return f
        return None

def remover_filme(cod_filme):
    for f in filmes:
        if (f[0] == cod_filme):
            filmes.remove(f)
        return True
    return False

    
def remover_todos_filmes():
    global filmes
    filmes = []
    
def iniciar_filmes():
    adicionar_filme(121,'StarWars', 120, 17, 'George Lucas', 'LucasFilm', 'Cartaz', 'Ficcao' )