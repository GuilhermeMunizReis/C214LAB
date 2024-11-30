import unittest
import xmlrunner
import sys

sys.path.append('src')

from currency import *

class TestCurrency(unittest.TestCase):
    def testCurrencyInstance(self):
        c = Currency("Ardin", "ard", 11.4)

        self.assertEqual(c.name, "Ardin")
        self.assertEqual(c.shortname, "ard")
        self.assertEqual(c.value, 11.4)

    def testCurrencyInstanceError(self):
        c = Currency("Ardin", "ard", 11.4)

        self.assertEqual(c.name, "Ardin")
        self.assertEqual(c.shortname, "ard")
        self.assertNotEqual(c.value, 20)
        
    # Testando a alteração do valor da moeda
    def testSetValue(self):
        c = Currency("Gold", "GP", 10.0)
        c.set_value(20.0)

        self.assertEqual(c.value, 20.0)
        
    # Testando a adição de valor à moeda
    def testAddValue(self):
        c = Currency("Gold", "GP", 50.0)
        c.add_value(25.0)

        self.assertEqual(c.value, 75.0)   

    # Testando a subtração de valor
    def testSubtractValue(self):
        c = Currency("Gold", "GP", 100.0)
        c.subtract_value(30.0)

        self.assertEqual(c.value, 70.0)
        
    # Testando a subtração de valor com saldo insuficiente
    def testSubtractValueInsufficient(self):
        c = Currency("Gold", "GP", 50.0)
        c.subtract_value(100.0)  

        self.assertEqual(c.value, 50.0)  # O valor não deve ser alterado

   # Testando a subtração de valor que deixa a moeda com saldo 0
    def testSubtractValueZeroBalance(self):
        c = Currency("Gold", "GP", 50.0)
        c.subtract_value(50.0)

        self.assertEqual(c.value, 0.0) 

if __name__ == "__main__":
    # Descobrir e executar todos os testes
    tests = unittest.TestLoader().discover(".")
    # Gerar relatório em formato XML na pasta `test-reports`
    with open('test-reports/results.xml', 'wb') as output:
        xmlrunner.XMLTestRunner(output=output).run(tests)