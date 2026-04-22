# Clase Personaje en Python

## Creación del constructor

El constructor es el método especial `__init__()`.  
Se ejecuta automáticamente cuando creamos un objeto.

```python
def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
    self.nombre = nombre
    self.fuerza = fuerza
    self.inteligencia = inteligencia
    self.defensa = defensa
    self.vida = vida
```

Sirve para inicializar los atributos del personaje.


---

## ¿Qué es self?

`self` representa al objeto actual de la clase.

```python
self.nombre = nombre
```

Esto significa que el atributo `nombre` del objeto guardará el valor recibido.


---

## ¿Qué es def?

La palabra `def` se usa para definir métodos o funciones.

```python
def atributos(self):
    print(self.nombre)
```

Aquí se define el método `atributos()`.

---

## ¿Cómo acceder a un atributo del personaje?

Se usa el nombre del objeto seguido de punto.

```python
print(mi_personaje.nombre)
```

Esto muestra el nombre del personaje.

---

## ¿Cómo acceder a un método de la clase Personaje?

Se llama usando el objeto y paréntesis.

```python
mi_personaje.atributos()
```

Esto ejecuta el método `atributos()` del objeto.

---

## Ejemplo de creación de objetos

```python
mi_personaje = Personaje("BitBoss", 10, 1, 5, 100)
mi_enemigo = Personaje("Enemy Stando", 8, 5, 3, 100)
```

Aquí se crean dos objetos de la clase `Personaje`.

---

## Archivo del código fuente

[personaje.py](personaje.py)
