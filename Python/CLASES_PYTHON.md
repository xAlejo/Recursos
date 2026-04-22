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

# Encapsulación

La encapsulación en Python consiste en proteger los atributos de una clase para evitar que sean modificados desde fuera del objeto.  
Para encapsular un atributo se colocan dos guiones bajos (`__`) antes del nombre del atributo.

## ¿Cómo se encapsula código en Python?

Los atributos se encapsulan agregando `__` al inicio del nombre.

```python
def __init__(self, nombre, fuerza):
    self.__nombre = nombre
    self.__fuerza = fuerza
```

En este ejemplo `__nombre` y `__fuerza` quedan protegidos dentro de la clase.

---

## ¿Para qué se usan los métodos get y set?

Los métodos `get` y `set` permiten acceder o modificar atributos encapsulados de forma controlada.

### Método get

El método `get` devuelve el valor de un atributo privado.

```python
def get_fuerza(self):
    return self.__fuerza
```

Ejemplo de uso:

```python
print(mi_personaje.get_fuerza())
```

### Método set

El método `set` modifica el valor del atributo validando antes la información.

```python
def set_fuerza(self, fuerza):
    if fuerza < 0:
        print("Error, has introducido un valor negativo")
    else:
        self.__fuerza = fuerza
```

Ejemplo de uso:

```python
mi_personaje.set_fuerza(20)
```

---

## ¿Se puede acceder a los métodos o atributos una vez encapsulados?

Sí, se puede acceder a los atributos encapsulados, pero no directamente de la forma normal.  
Python cambia internamente el nombre del atributo para protegerlo del acceso accidental.  
La forma correcta es usar métodos como `get` y `set`, porque permiten mantener el control sobre los datos del objeto.

```python
print(mi_personaje.get_fuerza())
mi_personaje.set_fuerza(15)
```

También es posible acceder usando el nombre interno generado por Python, aunque no es recomendable.

```python
mi_personaje._Personaje__fuerza = -5
```

Esto rompe la encapsulación porque modifica el atributo privado desde fuera de la clase.

## Archivo del código fuente

[personaje.py](personaje.py) <br>
[personaje_encapsulado.py](personaje_encapsulado.py)
