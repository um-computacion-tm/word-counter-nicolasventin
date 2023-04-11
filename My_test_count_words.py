import unittest

from count_words import contadorpalabras

class TestCountWords(unittest.TestCase):
    
    def test1(self):
        res = contadorpalabras("hola")
        self.assertEqual(res,{"hola":1})
    
    def test2 (self):
        res=contadorpalabras("hola mundo")
        self.assertEqual(
            res,
            {
                "hola":1,
                "mundo":1,
            }
        )

    def test3 (self):
        res=contadorpalabras("que onda")
        self.assertEqual(
            res,
            {
            "que":1,
            "onda":1,
            }
        )

    def test4 (self):
        res=contadorpalabras("el primer servicio es muy muy malo")
        self.assertEqual(
            res,
            {
                "el":1,
                "primer":1,
                "servicio":1,
                "es":1,
                "muy":2,
                "malo":1,
            }
        )

if __name__== '__main__':
    unittest.main()