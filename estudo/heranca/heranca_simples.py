class Veiculo:
    def __init__(self, cor, placa, numRodas):
        self.cor= cor
        self.placa= placa
        self.numRodas= numRodas
        
    def ligarMotor(self):
        print("Ligando motor")
        
    def __str__(self):
        return f"\n{self.__class__.__name__}:\n\t{"\n\t".join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"
        

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numRodas, carregado=True):
        super().__init__(cor, placa, numRodas)
        self.carregado= carregado
        
    def estaCarregado(self):
        print("Está carregado" if self.carregado else "Não está carregado.")
        

moto= Motocicleta("verde", "zzz-9z99", 2)
carro= Carro("preto", "abc-1r23", 4)
caminhao= Caminhao("prata", "rta-4t51", 10, False)

caminhao.estaCarregado()
print(caminhao)
print(moto)
print(carro)