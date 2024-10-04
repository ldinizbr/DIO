class Passaro:
    def voar(self):
        print(f"Voando - {self.__class__.__name__}")
    
class Pardal(Passaro):
    def voar(self):
        super().voar()
        
class Avestruz(Passaro):
    def voar(self):
        print('Avestruz nao voa')
        
#FIXME: exemplo ruim de herança
class Aviao(Passaro):
    def voar(self):
        print("Aviao está decolando")
        
def plano_de_voo(passaro):
    passaro.voar()
    
plano_de_voo(Pardal())
plano_de_voo(Avestruz())
plano_de_voo(Aviao())