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

