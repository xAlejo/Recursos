# WHILE
es un ciclo infinito o un bug infinito que solo se puede ser terminado o se puede salir de el mediante el termino de la condicion o mientras una condicion sea verdadera

```python
#Ejemplo

contrasena = "Miyu"

while True:
    contrasena_input= input("Ingrese la contraseña: ")
    
    if contrasena_input == "Miyu":
        print("Contraseña correcta")
        break   
    else:
        print("Contraseña incorrecta, Introduzca una contraseña correcta")
 ```
* Si se quieren agregar intentos se realizaria de la siguente forma la variable

```Python
# Ejemplo


contrasena = "Miyu"
contador= 0

while True:
    contrasena_input= input("Ingrese la contraseña: ")
    contador += 1
    
    if contador > 3:
        print("Has excedido el número de intentos. Intenta más tarde.")
        break
        
    elif contrasena_input == "Miyu":
        print("Contraseña correcta. ")
        break   
        
    else:
        print("Contraseña incorrecta. Introduzca una contraseña correcta.)
```
