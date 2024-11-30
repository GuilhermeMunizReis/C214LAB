import unittest
import xmlrunner

if __name__ == "__main__":
    # Descobrir e executar todos os testes
    tests = unittest.TestLoader().discover(".")
    # Gerar relatório em formato XML na pasta `test-reports`
    with open('test-reports/results.xml', 'wb') as output:
        xmlrunner.XMLTestRunner(output=output).run(tests)
