import unittest
import ator

class TestAtor(unittest.TestCase):
    
    def setUp(self):
        ator.remover_todos_atores()
        
    def test_sem_atores(self):
        atores = ator.listar_atores()
        self.assertEqual(0, len(atores))
        
    def test_adicionar_um_ator(self):
        ator.adicionar_ator(2222, "Charles","Brasileiro", 38)

        atores = ator.listar_atores()
        self.assertEqual(1, len(atores))

        a = atores[0]
        
        self.assertEqual(2222, a[0])        
        self.assertEqual("Charles", a[1])
        self.assertEqual("Brasileiro", a[2])
        self.assertEqual(38, a[3])

    def test_adicionar_dois_atores(self):
        ator.adicionar_ator(2222, "Charles","Brasileiro", 38)
        ator.adicionar_ator(1111, "Maria", "Italiana", 49)
        atores = ator.listar_atores()
        self.assertEqual(2, len(atores))

    def test_buscar_ator(self):
        ator.adicionar_ator(2222, "Charles","Brasileiro", 38)
        
        a = ator.buscar_ator(2222)
        
        self.assertEqual(2222, a[0])
        self.assertEqual("Charles", a[1])
        self.assertEqual("Brasileiro", a[2])
        self.assertEqual(38, a[3])
        
    def test_remover_ator(self):
        ator.adicionar_ator(2222, "Charles","Brasileiro", 38)
        
        ator.remover_ator(2222)
        
        a = ator.buscar_ator(2222)        
        self.assertIsNone(a)
     
    def test_remover_todos_atores(self):
        ator.adicionar_ator(2222, "Charles","Brasileiro", 38)
        ator.adicionar_ator(1111, "Maria", "Italiana", 49)
        
        ator.remover_todos_atores()
        
        a = ator.listar_atores()
        self.assertEqual([], a)       
        
        
    def test_iniciar_atores(self)  :
        ator.iniciar_atores()
        atores = ator.listar_atores()
        self.assertEqual(1, len(atores))
        
        
            
if __name__ == '__main__':
    unittest.main(exit=False)
