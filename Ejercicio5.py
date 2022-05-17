''''
Ejercicio N°12: Ingresar dos números y realizar todas las operaciones aritméticas.
'''
numero1 = int(input("Ingrese un número: ")) #Permite que el usuario ingrese el primer número
numero2 = int(input("Ingrese un número: ")) #Permite que el usuario ingrese el segundo número
suma = numero1+numero2  #Operación suma 
resta = numero1-numero2  #Operación resta
multiplicacion = numero1*numero2  #Operación multiplicacion
potenciacion = numero1**numero2  #Operación potenciacion

if numero2 != 0:    #Condicional para la operación de la división, si numero2 es diferente de 0 se realiza la operación. Caso contrario se muestra un mensaje para que el usuario ingrese un valor diferente de 0. 
    division = numero1/numero2  #Opreación divisón
    divisionEntera = numero1 // numero2 #Opreación divisón entera 
    print("\n La suma es:", suma, "\n La resta:", resta,
          "\n La multiplicación es:", multiplicacion, "\n La división es:", division, "\n La división entera es:", divisionEntera ,"\n La potencición es:", potenciacion)#Imprime por consola 
else:
    print("Ingrese un número entero diferente de 0")#Imprime el mesaje por consola de la condicional 
