# Ejercicios Propios

# 1
# Calculadora simple

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

