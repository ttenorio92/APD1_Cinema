import unittest
import sala

class TestSala(unittest.TestCase):
    
    def setUp(self):
        sala.remover_todas_salas()
        
    def test_sem_salas(self):
        salas = sala.listar_salas()
        self.assertEqual(0, len(salas))
        
    def test_adicionar_uma_sala(self):
        sala.adicionar_sala(23, 200)

        salas = sala.listar_salas()
        self.assertEqual(1, len(salas))

        s = salas[0]
        
        self.assertEqual(23, s[0])        
        self.assertEqual(200, s[1])
        

    def test_adicionar_duas_salas(self):
        sala.adicionar_sala(23,200)
        sala.adicionar_sala(24,309)
        salas = sala.listar_salas()
        self.assertEqual(2, len(salas))

    def test_buscar_sala(self):
        sala.adicionar_sala(23, 200)
        
        s = sala.buscar_sala(23)
        
        self.assertEqual(23, s[0])
        self.assertEqual(200, s[1])
        
    def test_remover_sala(self):
        sala.adicionar_sala(23, 200)
        
        sala.remover_sala(23)
        
        s = sala.buscar_sala(23)        
        self.assertIsNone(s)
     
    def test_remover_todas_sala(self):
        sala.adicionar_sala(23, 200)
        sala.adicionar_sala(24, 300)
        
        sala.remover_todas_salas()
        
        s = sala.listar_salas()
        self.assertEqual([], s)       
        
        
    def test_iniciar_salas(self)  :
        sala.iniciar_salas()
        salas = sala.listar_salas()
        self.assertEqual(1, len(salas))
        
        
            
if __name__ == '__main__':
    unittest.main(exit=False)
