class For:
    def _init_(self):
        pass
    
    def usoFor(self):
        # ciclo repetitivo de incremento o decremento se ejecuta por verdadero 
        nombre = "Daniel"
        datos=["Daniel",50,True]
        numeros=(2,5,6,4,1)
        docente = {'nombre':'daniel','edad': 50,'fac': 'faci'}
        listaNotas = [(30,40),(20,40,50),(50,40)]
        listaAlumnos = [{"nombre":"Erick","final":70},{"nombre":"Yady","final":60},{"nombre":"Danny","final":90}]
        
        # j=0
        # while j<5:
        #     j=j+1
            
        # for i in range(5): #rango(0,1,2,3,4)
        #     print('for',i,end=" ")
        # print()
        # for i in range(1,5): #rango(1,2,3,4)
        #     print('for',i,end=" ")
        # print()
        # for i in range(2,10,2):#rango(2,4,6,8)
        #     print('for',i,end=" ")
        # print()
        # for i in range(12,3,-3):#rango(12,9,6)
        #     print('for',i,end=" ")
            
             
        # lon = len(nombre)   
        # for pos in range(lon):
        #     if pos%2 == 0 and pos !=0:
        #        print(pos,nombre[pos])
        
        
        # vocal = ('a','e','i','o','u')    
        # for elen in datos:
        #     print(elen,end=" ")
        # for elen in nombre:
        #     print(elen,end=" ")
        
        
        # lon = len(datos)   
        # for pos in range(lon):
        #     print(pos,datos[pos])
            
        # for pos,valor in  enumerate(datos):
        #     print(pos,valor) 
            
        # for clave,valor in docente.items():
        #     print(clave,valor,end=" ")
        
        # print(listaNotas)
        # for notas in listaNotas:
        #     print("for externo", notas)
        #     for nota in notas:
        #         print(nota,end=" ")
        #     print("saliendo del for interno")
            
        # print(listaNotas)
        # for notas in listaNotas:
        #     acum=0
        #     for nota in notas:
        #         acum=acum+nota
        #     print(acum/len(notas),end=" ")
        # listaAlumnos = [{"nombre":"Juan","final":70},{"nombre":"Carmen","final":60},{"nombre":"Andrea","final":90}]
        # print("\nDiccionario de alumnos")
        # print(listaAlumnos)
        # acum=0
        
        # for alumnos in listaAlumnos:
        #     print(alumnos)
            
        #     for clave,valor in alumnos.items():
        #         print(clave,":",valor,len(valor),end="  ")
        #         if clave == "final":
        #            acum+acum+valor 
                   
        #     print()
        # print("Promedio",acum/len(listaAlumnos)) 
        listaNotas = [(30,40,10,20),(20,40,50),(50,40,10)(10,20)] 
        acum=0
        cont=0
        for notas in listaNotas:
            print(notas)  
            acumparcial=0
            for nota in notas:
                acumparcial +=nota   
            cont+cont+len(notas)
            acum=acum+acumparcial
            print("TotalParcial:{} PromParcial{}".format(acumparcial,acumparcial/len(notas))) 
        print("TotalGeneral:{} PromGeneral{}".format(acum,acum/cont))            
bucle = For() 
bucle.usoFor()