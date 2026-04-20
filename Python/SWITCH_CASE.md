#SWITCH CASE
lo que hace es evaluar un valor y lo va a comparar con cada uno de los casos y si coincide con alguno de esos caso recien empezara a ejecutar la funcion, en otras palabras es una estructura que sirve para tomar decisiones según el valor de una variable, como una forma más ordenada de reemplazar muchos if y elif

```python
# Ejemmplo

dia = int (input("Ingrese el valor numerico del dia de la semana: "))

match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miércoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")
    case _:
        print("dia de la semana inexistente")
        ```
