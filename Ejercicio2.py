'''
Ejercicio N°19: Ingresar cualquier número y calcular su raíz cuadrada.
'''
numero = int(input("Ingrese un número: ")
             )  # Pide al usuario ingresar un número por teclado.

# Se define la función con su parámetro; (numero) es la variable que almacenará el número ingresado por el usuario.
def raizCuadrada(numero):

    x = numero/2  # La variable "x" guardará la dividición del valor ingresado.

    while True:  # Creamos un bluce while true para que detenga el proceso en cuanto se repita un valor en dos iteraciones.

        if x*x == numero:  # Se crea la condición: sí x que contiene la division del numero ingresado, se multiplica por x,
            return x  # Dovelverá la raiz cuadrada del número

        else:         # Caso contario cambiamos el valor de x calculando la media de un rectángulo

            nueva_x = x  # Se reemplaza el valor de x

            ''' Cálculo de la media de un rectangulo haciendo uso de las variables agregadas anteriormente; 
                (x = base(altura = numero/x)  y se divide todo para )/2
                                   numero/x = area /base'''
            x = (x+(numero/x))/2

            if nueva_x == x:

                break     # Rompe el ciclo de iteraciones
    return x


print(raizCuadrada(numero))  # Imprime el resultado por consola
