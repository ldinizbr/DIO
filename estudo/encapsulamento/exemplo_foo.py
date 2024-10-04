class Foo:
    def __init__(self, x=None):
        self._x= x
        
    @property
    def x(self):
        return self._x or 0 #se for None
    
    @x.setter
    def x(self, value):
        _x= self._x or 0
        _value= value or 0
        self._x= _x + _value
        
    @x.deleter
    def x(self):
        self._x= -1
        
foo= Foo(10)
print(foo.x) #metodo definido pelo @property
foo.x= 10    #metodo definido pelo @x.setter
print(foo.x)
del foo.x    #metodo definido pelo @x.deleter
print(foo.x)

        