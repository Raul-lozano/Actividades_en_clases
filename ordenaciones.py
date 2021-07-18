#semana28-06-2021
class Ordenar:
    def _init_(self,lista):
        self.lista=lista 
    
    def recorrerElemento(self):   
        for ele in self.lista:
            print(ele)
        
    def recorrerEnumerate(self):
        for pos,ele in enumerate(self.lista):
            print(pos,ele)
   
    def recorrerRange(self):
        for pos in range(len(self.lista)):
            print(pos,self.lista[pos])  
            
    def buscar(self,buscado):
        enc=False
        for pos,ele in enumerate(self.lista):
            if ele ==  buscado:
                enc=True
                break
        if enc ==True:return pos
        else:return -1
            
       
    def ordenarAsc(self):
        for pos in range(0,len(self.lista)): 
                for sig in range(pos+1,len(self.lista)): 
                    if self.lista[pos] > self.lista[sig]:
                        aux = self.lista[pos]
                        self.lista[pos]=self.lista[sig]
                        self.lista[sig]=aux
                    
# ord1.recorrerElemento()
# ord1.recorrerEnumerate()
# ord1.recorrerRange()
# print(ord1.buscar(3))
# buscado=9
# resp = ord1.buscar(buscado)
# if resp !=-1:
#     print("Numero={}se encuentra en la Posicion:({})de la lista:{}".format(buscado,resp, ord1.lista))
# else:
#     print("Numero={} no se encuentra en la lista:{}".format(buscado,ord1.lista))     
    def ordenarDesc(self):
        for pos,ele in enumerate(self.lista):
                for sig in range(pos+1,len(self.lista)): 
                    if ele < self.lista[sig]:
                     aux = self.lista[pos]
                     self.lista[pos]=self.lista[sig]
                     self.lista[sig]=aux
    
    def primer(self):
        return self.lista[0] 
    
    def primer(self):
        return self.lista[-1]    
       
lista = [2,3,1,5,8,10] 
ord1 = Ordenar(lista)
print("primer",ord1.primer())
print("segundo",ord1.ultimo())
print("Normal",ord1.lista)
ord1.ordenarAsc()
print("Asc",ord1.lista)
ord1.ordenarDesc()
print("Desc",ord1.lista)