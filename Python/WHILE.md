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
