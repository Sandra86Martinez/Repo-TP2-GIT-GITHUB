import math

#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”

print("Hola Mundo!")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla

nombre = input("Ingrese su nombre:")
print(f"Hola {nombre}!")

#3) Crear un programa que pida al usuario su nombre,
# apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar_residencia = input("Lugar de Residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}.")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
#su perímetro. 

radio=float(input("Ingrese el radio de un círculo:"))
area=math.pi*(radio**2)
perimetro=2*math.pi*radio
print(f"El área del circulo es: {area:.2f}, y el perímetro del círculo es: {perimetro:.2f}.")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
#cuántas horas equivale. 

segundos=int(input("Ingrese el valor en segundos:"))
horas=segundos/3600

if horas == 1:
   print(f"El valor ingresado equivale a: {horas} hora.")
else:
   print(f"El valor ingresado equivale a: {horas:.2f} horas.")
   
#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
#multiplicar de dicho número. 

numero=int(input("Ingrese el numero entero a multiplicar: "))

for i in range(1, 11):  # range(5) genera 0, 1, 2, 3, 4
    resultado=numero*i
    print(f"{numero} x {i} = {resultado}")

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 

num1=int(input("Ingrese el primer valor positivo: "))
num2=int(input("Ingrese el segundo valor positivo: "))
suma=num1+num2
division=num1/num2
multiplicacion=num1*num2
resta=num1-num2
print(f"Suma: {suma}, División {division}, Multiplicación {multiplicacion}, Resta {resta}." )

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente 
#modo:  IMC=peso en kg//altura en m)2

peso=float(input("Ingrese su peso: "))
altura=float(input("Ingrese su altura: "))
IMC=peso/(altura**2)
print(f"Su IMC es: {IMC:.2f}.")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 
#Temperatura 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖t = 9/5.Temperatura en Celsius+32

GradosCelsius=float(input ("Ingrese el valor en Grados Celsius: "))
Fahrenheit= (9/5)*GradosCelsius + 32
print(f"El equivalente en Grados Fahrenheit es: {Fahrenheit}.")

 #10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
#dichos números.

num1=float(input("Ingrese el primer numero: "))
num2=float(input("Ingrese el segundo numero: "))
num3=float(input("Ingrese el tercer numero: "))
promedio=(num1+num2+num3)/3
print(f"El promedio de los valores ingresados es: {promedio:.2f}.")





