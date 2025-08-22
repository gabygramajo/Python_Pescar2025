### Ejercicio 1
#Escribir un programa que muestre por la pantalla la cadena ¡Hola Mundo!
print("Hola Mundo")

### Ejercicio 2
# Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido
# de la variable.

cadena = "¡Hola Mundo!"
print(cadena)


### Ejercicio 3
# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca
# muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.

nombre_del_usuario = input("¿Cuál es tu nombre? ")
print("¡Hola " + nombre_del_usuario + "!")


### Ejercicio 4
# Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética $(3+2 / 2,5)^2$.

resultado = ((3 + 2) / 2.5) ** 2
print(f'(3+2/2,5)^2 = {resultado}')


### Ejercicio 5
# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el costo por hora. Después debe
# mostrar por pantalla el sueldo que le corresponde.

horas_trabajadas = int(input("¿Cuántas horas has trabajado?: "))
costo_por_hora = float(input("¿Cuál es el costo por hora? $"))
sueldo = horas_trabajadas * costo_por_hora
print(f"Sueldo correspondiente: ${sueldo}")


### Ejercicio 6
# Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en la pantalla la suma
# de todos los enteros desde 1 hasta N. La suma de los N primeros enteros positivos puede ser calculada de la siguiente
# forma. $suma = n(n + 1 ) / 2$

entero_positivo = int(input("Introduce un número entero positivo: "))
suma = (entero_positivo * (entero_positivo + 1)) // 2
print(f'El Resultado es: {suma}')


###  Ejercicio 7
# Escribir un programa que pida al usuario su peso (kg) y estatura ( en metros), calcule el índice de masa corporal y lo
# almacene en una variable, y muestre por pantalla la frase **Tu índice de masa corporal es \<imc\>** donde \<imc\> es el
# índice de masa corporal calculado redondeado con dos decimales.

peso = float(input("¿Cuál es tu peso en kg? "))
estatura = float(input("¿Cuál es tu estatura en metros? "))
imc = peso / (estatura ** 2)
print(f"Tu índice de masa corporal es {imc:.2f}")


### Ejercicio 8
# Escribir un programa que pida al usuario dos números enteros por pantalla la \<n> entre \<m> da un cociente \<c> y un
# resto \<r>, donde \<n> y \<m> son los números introducidos por el usuario, y \<c> y \<r> son el cociente y el resto de la división entera respectivamente.

n = int(input("Introduce un número entero: "))
m = int(input("Introduce otro número entero: "))
c = n // m
r = n % m
print(f'{n} entre {m} da un cociente {c} y un resto {r}')


### Ejercicio 9
# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años y muestre
# por pantalla el capital obtenido en la inversión. $capital + (cantidad * (intereses / 100 + 1)^{años})$

cantidad = float(input("¿Cuál es la cantidad a invertir? $"))
capital = cantidad
interes_anual = float(input("¿Cuál es el interés anual? "))
anios = int(input("¿Cuál es el número de años? "))
capital_obtenido = capital + (cantidad*(interes_anual/100+1)**anios)
print(f'Capital obtenido: ${capital_obtenido:.2f}')


### Ejercicio 10
# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por web y la empresa
# de logística les cobra por peso de cada paquete así que deben calcular el de los payasos y muñecas que saldrán en cada
# paquete a demanda. Cada payaso pesa 112 gr y cada muñeca 75 gr. Escribir un programa que lea el número de
# payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

peso_payaso = 112
peso_munieca = 75
cantidad_payasos = int(input("¿Cuántos payasos se vendieron? "))
cantidad_muniecas = int(input("¿Cuántas muñecas se vendieron? "))
peso_total = cantidad_payasos * peso_payaso + cantidad_muniecas * peso_munieca
print(f'Se vendieron {cantidad_payasos} Payasos y {cantidad_muniecas} Muñecas. Peso total del paquete: {peso_total} gr')

### Ejercicio 11
# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a
# intereses, que no se cobran hasta finales de año, se te suman al saldo final de tu cuenta de ahorros. Escribir un
# programa que comience leyendo la cantidad de dinero en la cuenta de ahorros introducida por el usuario. Después el
# programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear
# cada cantidad a dos decimales.

interes_anual = 0.04
cantidad_ahorros = float(input("¿Cuál es la cantidad de dinero en la cuenta de ahorros? $"))
ahorros_primer_anio = cantidad_ahorros * (1 + interes_anual)
print(f'Cantidad de ahorros tras el primer año: ${ahorros_primer_anio:.2f}')
ahorros_segundo_anio = ahorros_primer_anio * (1 + interes_anual)
print(f'Cantidad de ahorros tras el segundo año: ${ahorros_segundo_anio:.2f}')
ahorros_tercer_anio = ahorros_segundo_anio * (1 + interes_anual)
print(f'Cantidad de ahorros tras el tercer año: ${ahorros_tercer_anio:.2f}')


### Ejercicio 12
# Una panadería vende barras de pan a $3.499 cada una. El pan que no es del día tiene un descuento de un 60%. Escribir
# un programa que comience leyendo el numeros de barras de pan vendidas que no son del día. Después el programa
# debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser del día y el costo final total.

barra_de_pan = 3499
descuento = 0.6
cantidad_vendida = int(input("Cantidad de barras de pan vendidas que no son del día: "))
print(f'Precio habitual de una barra de pan: ${barra_de_pan}')
descuento_barra_de_pan = barra_de_pan * descuento
print(f'Descuento por no ser del día: ${descuento_barra_de_pan}')
print(f'Costo final total: ${(descuento_barra_de_pan * cantidad_vendida):.2f}')