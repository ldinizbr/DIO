class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro=18, marcha=0):
        self.cor= cor
        self.modelo= modelo
        self.ano= ano
        self.valor= valor
        self.aro= aro
        self.marcha= marcha
    
    def buzinar(self):
        print("_buzinando_")
    
    def parar(self):
        print("Parando bicileta.\nBicicleta parada.")
        
    def correr(self):
        print("_acelerando_")
        
    def trocarMarcha(self, numMarcha):
        
        def _trocarMarcha():
            if numMarcha > self.marcha:
                print(f"Marcha trocada para {numMarcha}.")
            else:
                print("Não foi possível trocar a marcha.")
    
        print("Trocando marcha...")
        _trocarMarcha()
        
        

                
        
    def __str__(self):
        return f'{self.__class__.__name__}:\n\t{"\n\t".join([f"{chave} : {valor}" for chave, valor in self.__dict__.items()])}'
        
    
        
bike1= Bicicleta("preta", "caloi", 2021, 500)

bike1.buzinar()
bike1.correr()
bike1.parar()
print(bike1.ano, bike1.cor, bike1.modelo, bike1.valor)
    
b2= Bicicleta("verde", "monark", 2002, 900, 15, 2)
Bicicleta.buzinar(b2) # == b2.buzinar(), pois o self é explicito
print(b2)

b2.trocarMarcha(3)