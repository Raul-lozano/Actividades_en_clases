class ejercicio:
    def __init__(self):
        pass
    def parImpar(self, numero):
        numero= int(input("ingrese un numero"))
        if numero % 2 == 0:
            print("{} es Par". format(numero))
        else:
            print("{}es Impar". format(numero))

print(ejer.parImpar(7))            