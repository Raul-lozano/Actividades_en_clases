class ejercicios:
    def __init__(Self):
       pass
   
    def parImpar(self,numero):
        if numero %  2 == 0:
           print("{}es Par".format(numero))
        else: 
            print("{}es Impar".format(numero))
ejer =  ejercicios()
num = int(input("ingrese un numero"))
ejer.parImpar(num)
input() 
lista = [2,3,1,5,6,8,10]
print("llamada 2")
for num in lista:
     ejer.parImpar(num)
input() 
print("llamada 3")
ejer.parImpar(23)
