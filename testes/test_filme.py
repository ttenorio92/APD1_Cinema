# -*- coding: utf-8 -*-

import unittest
from logica import filme


class TestFilme(unittest.TestCase):
    
    def setUp(self):
        filme.remover_todos_filmes()
        
        
    def test_sem_filmes(self):
        filmes = filme.listar_filmes()
        self.assertEqual(0, len(filmes))    
        
        
    def test_adicionar_um_filme(self):
        filmes.adicionar_filmes(121,'StarWars', 120, 17, 'George Lucas', 'LucasFilm', 'Cartaz', 'Ficcao' )

        filmes = filme.listar_filmes()
        self.assertEqual(1, len(filmes))

        f = filmes[0]
        
        self.assertEqual(121, f[0])        
        self.assertEqual("StarWars", f[1])
        self.assertEqual(120, f[2])
        self.assertEqual(17, f[3])
        self.asserEqual('GeogeLucas', f[4])
        self.asserEqual('LucasFilm', f[5])
        self.asserEqual('Cartaz', f[6])
        self.asserEqual('Ficcao', f[7])
        
        
    def test_adicionar_dois_filmes(self):
        filme.adicionar_filme(121,'StarWars', 120, 17, 'George Lucas', 'LucasFilm', 'Cartaz', 'Ficcao')
        filme.adicionar_filme(122,'StraightOuttaCompton', 130, 18, 'F Gary Gray', 'Universal', 'Cartaz', 'Drama')
        filmes = filme.listar_filmes()
        self.assertEqual(2, len(filmes))    
        
        
        
        
        
if __name__ == '__main__':
    unittest.main(exit=False)
     