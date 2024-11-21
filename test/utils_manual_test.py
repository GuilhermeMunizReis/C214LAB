import sys
import pandas as pd

sys.path.append('data')
sys.path.append('src')

from utils import *

class TestGlobalItens:
    def testLoadCsv(self):
        data = pd.read_csv('data/itens.csv', delimiter=';')

        print(data)

        del data

if __name__ == '__main__':  
    t = TestGlobalItens()
    t.testLoadCsv()