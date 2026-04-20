# Funciones
las funciones son bloque de código que se puede reutilizar para hacer una tarea específica., son basicas para entender como extraer la logica de algo que queremos aplicar y separarla de los datos sobre los que se aplicar, esta sirve para crear listas de elementos

```python
#Ejemplo

def puntuacion(clase):
    returm sum(clase) / len(clase)

clase = [7, 8, 9]
media = puntuacion(clase)
print("la puntuacion clase es:", media)
```
