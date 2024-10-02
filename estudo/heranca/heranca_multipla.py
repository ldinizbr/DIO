class Animal:
    def __init__(self, numPatas):
        self.numPatas= numPatas
    
    def __str__(self):
        return f'\n{self.__class__.__name__}:\n\t{"\n\t".join([f"{chave} : {valor}" for chave, valor in self.__dict__.items()])}'


class Mamifero(Animal):
    def __init__(self, corPelo, **kwargs):
        self.corPelo= corPelo
        super().__init__(**kwargs)
        
        
class Ave(Animal):
    def __init__(self, corBico, **kwargs):
        self.corBico= corBico
        super().__init__(**kwargs)


class Gato(Mamifero):
    pass


class GrunirMixin:
    def grunir(self):
        return "_grunido_"


class Ornitorrinco(Mamifero, Ave, GrunirMixin):
    def __init__(self, corPelo, corBico, numPatas): #nao é necessario nesse exemplo
        super().__init__(corPelo= corPelo, corBico= corBico, numPatas= numPatas)

#devido ao uso de kwargs é necessário passar o parametro por chave-valor
gato= Gato(numPatas=4, corPelo="Laranja")
print(gato)

ornitorrinco= Ornitorrinco(numPatas=4, corPelo="Marrom", corBico="Amarelo")
print(ornitorrinco)
print(ornitorrinco.grunir())