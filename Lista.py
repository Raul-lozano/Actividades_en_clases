#Listas
listanotas = [4, 6, 8, 10, 12]
prom = (listanotas)
print('promedio: {} = {}'.format(listanotas, prom))
x=int(input("Ingresar un numero entero: "))
if x < 0:
    x= 0
    print("negativo cambiado a cero")
elif x == 0:
    print("cero")
elif x == 1:
    print("uno")
else:
    print("Ninguna opcion")
print("ok") if type(x) == int else print("-")