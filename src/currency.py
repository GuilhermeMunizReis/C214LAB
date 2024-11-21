class Currency:
    def __init__(self, name:str, shortname:str, value:float = 0.0):
        self.name = name
        self.shortname = shortname 
        self.value = value

    def set_value(self, new_value:float):
        self.value = new_value
    
    #Adiciona um valor à moeda.
    def add_value(self, amount: float):
        self.value += amount

    # Subtrai um valor da moeda, se houver saldo suficiente.Se não houver, o saldo continua igual.
    def subtract_value(self, amount: float):
        if self.value - amount >= 0:
            self.value -= amount
        else:
            print("Valor insuficiente.")
    
    #Retorna uma string representando a moeda, incluindo seu nome, abreviação e valor.
    def __str__(self):
        return f"{self.name} ({self.shortname}): {self.value}"
    

if __name__ == "__main__":
    # Criando uma instância de moeda
    gold = Currency("Gold", "GP", 100.0)
    
    print(gold)  

    gold.set_value(150.0)
    print(gold)  
    

    gold.add_value(50.0)
    print(gold)  
    

    gold.subtract_value(75.0)
    print(gold)  
    

    gold.subtract_value(200.0)  