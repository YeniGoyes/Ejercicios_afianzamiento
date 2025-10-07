#Parte uno

#Ejercicio uno

def ejercicio1():
 número1 = int(input("Ingrese un número: "))
 if número1 > 0 :
    print(f"{número1**2}")

#Ejercicio 2

def ejercicio2():
 nf = int(input("Ingrese un número: "))
 n = nf
 while n != 1:
  if n%2== 0:
   n = n//2
  elif n%2 !=0:
   n = 3*n +1 
   
  print(n, end="  ")
 

#Ejercicio 3 

def ejercicio3():
 A = 25 
 B = 18.9
 D = 2022
 AX = A
 A = AX + AX * 0.02
 BX = B
 B = BX + BX * 0.03
 DI = D
 D = DI + 1

 while B <= A:
 
  AX = A
  A = AX + AX * 0.02
  BX = B
  B = BX + BX * 0.03
  DI = D
  D = DI + 1
 print(A)
 print(B)
 return D

#Ejercicio 5

def ejercicio5():
    h = 1.0   
    while (1.0 + h) != 1.0:   
        h = h / 2.0         
    print("El épsilon de máquina es:", h * 2)


#Parte 2


#Ejercicio 1

def ejerciciouno():
 for a in range(1,101):
  print(f"{a} = {a**2}", end = " , ")

#Ejercicio 2

def ejerciciodos():
 for e in range (1,1000,2):
  print(f"{e}", end = ",")
 
 for i in range(2,1001,2):
  print(f"{i}", end = ",")
  
#Ejercicio 3 

def ejerciciotres():
 o = int(input("Ingrese un núemro:"))
 for o in range(o,1,-2):
  print(f"{o}", end = ",")

#Ejercicio 4

def ejerciciocuatro():
    u = int(input("Ingrese un número: "))
    factorial = 1
    for n in range(1, u + 1):
        factorial *= n
        print(f"{u}! = {factorial}")

#Ejercicio 5

def ejerciciocinco():
 n = int(input("Ingrese un número: "))
 print(f"{2**n}")

#Ejercicio seis

def ejercicioseis():
 x = int(input(" para x^n Ingrese el valor de x: "))
 n = int(input("Ahora ingrese el valor de n: "))
 print(f"{x**n}")

#Ejercicio 7

def ejerciciosiete():
    for p in range(1, 10): 
        print(f"\nTabla del {p}:")
        for a in range(1, 11):  
            print(f"{p} x {a} = {p * a}")

def main():
  print("\n parte 1")
  print("Ejercicio 1")
  ejercicio1()
  
  print("\n Ejercicio 2")
  ejercicio2()

  print("\n Ejercicio 3")
  ejercicio3()

  print("\n Ejericicio 5")
  ejercicio5()

  print("\n\n Parte 2")

  print("\n ejercicio 1")
  ejerciciouno()

  print("\n Ejercicio 2")
  ejerciciodos()
    
  print("\n Ejercicio 3")
  ejerciciotres()
    
  print("\n Ejercicio 4")
  ejerciciocuatro()
    
  print("\n Ejercicio 5")
  ejerciciocinco()
    
  print("\n Ejercicio 6")
  ejercicioseis()
    
  print("\n Ejercicio 7")
  ejerciciosiete()

if __name__ == "__main__":
    main()






  
  





 
 





    
  




 
  

  
 


 



          

