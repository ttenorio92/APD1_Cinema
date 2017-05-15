import unittest
import elenco

class TestElenco(unittest.TestCase):
    
    def setUp(self):
        elenco.remover_todos_elencos()
        
    def test_sem_elenco(self):
        elencos = elenco.listar_elencos()
        self.assertEqual(0, len(elencos))
        
    def test_adicionar_um_elenco(self):
        elenco.adicionar_elenco(1234, 111, 4, "Suspense")

        elencos = elenco.listar_elencos()
        self.assertEqual(1, len(elencos))

        e = elencos[0]
        
        self.assertEqual(1234, e[0])        
        self.assertEqual(111, e[1])
        self.assertEqual(4, e[2])
        self.assertEqual("Suspense", e[3])

    def test_adicionar_dois_elencos(self):
        elenco.adicionar_elenco(1234, 111, 4, "Suspense")
        elenco.adicionar_elenco(1235, 222, 2, "Acao")
        elencos = elenco.listar_elencos()
        self.assertEqual(2, len(elencos))

    def test_buscar_elenco(self):
        elenco.adicionar_elenco(1234, 111, 4, "Suspense")
        
        e = elenco.buscar_elenco(1234)
        
        self.assertEqual(1234, e[0])
        self.assertEqual(111, e[1])
        self.assertEqual(4, e[2])
        self.assertEqual("Suspense", e[3])
        
    def test_remover_elenco(self):
        elenco.adicionar_elenco(1234, 111, 4, "Suspense")
        
        elenco.remover_elenco(1234)
        
        e = elenco.buscar_elenco(1234)        
        self.assertIsNone(e)
     
    def test_remover_todos_elencos(self):
        elenco.adicionar_elenco(1234, 111, 4, "Suspense")
        elenco.adicionar_elenco(1235, 222, 3, "Acao")
        
        elenco.remover_todos_elencos()
        
        e = elenco.listar_elencos()
        self.assertEqual([], e)       
        
        
    def test_iniciar_elencos(self)  :
        elenco.iniciar_elencos()
        elencos = elenco.listar_elencos()
        self.assertEqual(1, len(elencos))
        
        
            
if __name__ == '__main__':
    unittest.main(exit=False)