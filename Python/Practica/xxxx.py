# Ejercicios Propios


 1. # Calculadora simple
# se ingresan ambos digitos de forma separada y el simbolo matematico para que se calcule y de el resultado correcto.

num1 = float(input("Primer número: "))
operador = input("Operador (+, -, *, /): ")
num2 = float(input("Segundo número: "))

if operador == "+":
    print("Resultado:", num1 + num2)

elif operador == "-":
    print("Resultado:", num1 - num2)

elif operador == "*":
    print("Resultado:", num1 * num2)

elif operador == "/":
    if num2 != 0:
        print("Resultado:", num1 / num2)
    else:
        print("No se puede dividir por cero")

else:
    print("Operador no válido")

2. # Juego de adivinar un número
# El sistema te pide ingresar un número entre el 1 al 100, si es el número que piensa la máquina, ganas.
import random

print("\nJUEGO: ADIVINA EL NUMERO")
print("Estoy pensando un numero entre 1 y 100")

secreto = random.randint(1, 100)
intentos = 0
adivinado = False

while not adivinado:
            try:
                intento = int(input("Tu intento: "))
                intentos = intentos + 1

                if intento < secreto:
                    print("El numero es mayor")
                elif intento > secreto:
                    print("El numero es menor")
                else:
                    print(f"Correcto en {intentos} intentos")
                    adivinado = True
            except ValueError:
                print("Ingresa un numero entero")

3. # Lista de tareas
# Se selecciona una de las opciones en pantalla, se pueden agregar, ver, marcar y eliminar tareas como un "to do list".

print("\nLISTA DE TAREAS")
tareas = []
salir_tareas = False

while not salir_tareas:
            print("\n1. Agregar")
            print("2. Ver")
            print("3. Marcar hecha")
            print("4. Eliminar")
            print("5. Volver")

            operacion_tarea = input("Elige opcion: ")

            if operacion_tarea == "1":
                nueva = input("Escribe la tarea: ")
                tareas.append({"texto": nueva, "hecha": False})
                print("Tarea agregada")

            elif operacion_tarea == "2":
                if len(tareas) == 0:
                    print("No hay tareas")
                else:
                    for i in range(len(tareas)):
                        estado = "X" if tareas[i]["hecha"] else " "
                        print(f"{i + 1}. [{estado}] {tareas[i]['texto']}")

            elif operacion_tarea == "3":
                if len(tareas) == 0:
                    print("No hay tareas")
                else:
                    for i in range(len(tareas)):
                        print(f"{i + 1}. {tareas[i]['texto']}")
                    try:
                        n = int(input("Numero de tarea: ")) - 1
                        if 0 <= n < len(tareas):
                            tareas[n]["hecha"] = True
                            print("Tarea marcada")
                        else:
                            print("Numero fuera de rango")
                    except ValueError:
                        print("Debes ingresar un numero")

            elif operacion_tarea == "4":
                if len(tareas) == 0:
                    print("No hay tareas")
                else:
                    for i in range(len(tareas)):
                        print(f"{i + 1}. {tareas[i]['texto']}")
                    try:
                        n = int(input("Numero a eliminar: ")) - 1
                        if 0 <= n < len(tareas):
                            tareas.pop(n)
                            print("Tarea eliminada")
                        else:
                            print("Numero fuera de rango")
                    except ValueError:
                        print("Debes ingresar un numero")

            elif operacion_tarea == "5":
                salir_tareas = True
            else:
                print("Opcion no valida")

4. # Calculador de IMC
# Se ingresa una variable peso, la altura y el sistema calcula el IMC de la persona, indicándole su grado de peso.

print("\nCALCULADOR DE IMC")

try:
    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en metros (ej: 1.75): "))

    if altura <= 0:
                print("La altura debe ser mayor que 0")
    else:
        imc = peso / (altura * altura)
        print(f"Tu IMC es: {imc:.2f}")

        if imc < 18.5:
                    print("Categoria: Bajo peso")
        elif imc < 25:
                    print("Categoria: Normal")
        elif imc < 30:
                    print("Categoria: Sobrepeso")
        else:
                    print("Categoria: Obesidad")
except ValueError:
    print("Debes ingresar numeros validos")
            
5. # Generador de contraseña
# Se ingresa un valor hasta el 12. El sistema creará una contraseña aleatoria.

import random
import string

print("\nGENERADOR DE CONTRASENA")

try:
    longitud = int(input("Longitud (por defecto 12): ") or "12")
    if longitud <= 0:
        print("La longitud debe ser mayor que 0")
    else:
        caracteres = string.ascii_letters + string.digits + "!@#$%^&*"
        nueva_contrasena = ""

        for _ in range(longitud):
                    nueva_contrasena = nueva_contrasena + random.choice(caracteres)

        print(f"Contrasena generada: {nueva_contrasena}")
except ValueError:
    print("Debes ingresar un numero entero")

6. # Conversor de unidades
# Se selecciona una de las opciones mostradas en pantalla y se ingresan los valores a convertir.

print("\nCONVERSOR DE UNIDADES")
print("1. Celsius a Fahrenheit")
print("2. Fahrenheit a Celsius")
print("3. Km a millas")
print("4. Millas a km")
print("5. Kg a libras")
print("6. Libras a kg")

tipo = input("Elige conversion (1-6): ")

try:
            valor = float(input("Ingresa el valor: "))

            if tipo == "1":
                resultado = (valor * 9 / 5) + 32
                print(f"Resultado: {resultado:.2f} F")
            elif tipo == "2":
                resultado = (valor - 32) * 5 / 9
                print(f"Resultado: {resultado:.2f} C")
            elif tipo == "3":
                resultado = valor * 0.621371
                print(f"Resultado: {resultado:.2f} millas")
            elif tipo == "4":
                resultado = valor / 0.621371
                print(f"Resultado: {resultado:.2f} km")
            elif tipo == "5":
                resultado = valor * 2.20462
                print(f"Resultado: {resultado:.2f} lb")
            elif tipo == "6":
                resultado = valor / 2.20462
                print(f"Resultado: {resultado:.2f} kg")
            else:
                print("Opcion de conversion no valida")
except ValueError:
    print("Debes ingresar un numero")

7. # Validador de contraseña segura
# Se ingresa una contraseña deseada y el sistema avisará lo que le falta para ser una contraseña segura.

print("\nVALIDADOR DE CONTRASENA")
contrasena = input("Ingresa una contrasena: ")

valida = True

if len(contrasena) < 8:
            print("- Debe tener al menos 8 caracteres")
            valida = False

tiene_mayuscula = False
tiene_minuscula = False
tiene_numero = False

for c in contrasena:
            if c.isupper():
                tiene_mayuscula = True
            if c.islower():
                tiene_minuscula = True
            if c.isdigit():
                tiene_numero = True

if not tiene_mayuscula:
            print("- Debe tener al menos una mayuscula")
            valida = False
if not tiene_minuscula:
            print("- Debe tener al menos una minuscula")
            valida = False
if not tiene_numero:
            print("- Debe tener al menos un numero")
            valida = False

if valida:
            print("Contrasena segura")
else:
            print("Contrasena no valida")

8. # Verificador de año bisiesto
# Aquí se verifica si el año ingresado es bisiesto o no. Ingrese un año.

print("\nVERIFICADOR DE ANO BISIESTO")

try:
    ano = int(input("Ingresa un ano: "))

    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print("Es un ano bisiesto")
    else:
        print("No es un ano bisiesto")
except ValueError:
    print("Debes ingresar un numero entero valido")

9. # Verificador de par e impar
# Se ingresa un número ENTERO para validar si el número es par o impar.

print("\nPAR O IMPAR")

try:
    numero = int(input("Ingresa un numero entero: "))

    if numero % 2 == 0:
        print("El numero es PAR")
    else:
        print("El numero es IMPAR")
except ValueError:
    print("Debes ingresar un numero entero valido")

10. # Contador de vocales
# Se ingresa una palabra y el sistema contará la cantidad de vocales en ella.

print("\nCONTADOR DE VOCALES")

texto = input("Ingresa una frase: ").lower()

cantidad = 0
for letra in texto:
    if letra in "aeiou":
        cantidad = cantidad + 1

print(f"Cantidad de vocales: {cantidad}")



