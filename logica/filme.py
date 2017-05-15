# -*- coding: utf-8 -*-

filmes = []

def cadastrar_filme(cod_filme, titulo, duracao, classificacao, diretor, distribuidora, status, genero):
    filmes.append(filmes)

def listar_filmes(): 
    return filmes

def buscar_filme(cod_filme):
    for f in filmes:
        if (f[0] == cod_filme):
            return f
        return None

def remover_todos_filmes():
    global filmes
    filmes = []
    
def iniciar_filmes():
    cadastrar_filme(121,'StarWars', 120, 17, 'George Lucas', 'LucasFilm', 'Cartaz', 'Ficcao' )