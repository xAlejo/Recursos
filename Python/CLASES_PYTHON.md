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

# Herencia

La herencia permite crear nuevas clases a partir de una clase existente.  
Esto significa que una clase hija puede reutilizar atributos y métodos de una clase padre sin escribir nuevamente el mismo código.

---

### ¿Por qué cuando se crea la clase Guerrero heredando de Personaje genera error el código?

El error aparece porque la clase `Guerrero` tiene un atributo nuevo llamado `espada`, pero si no se llama correctamente al constructor de la clase padre, los atributos originales como `nombre`, `fuerza` o `vida` no se inicializan.

```python
class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada
```

La función `super()` permite iniciar primero la clase padre.

---

### ¿Cuándo en el video se menciona la superclase a qué se refiere?

La superclase es la clase principal de la cual otras clases heredan.

En este ejemplo:

```python
class Personaje:
```

`Personaje` es la superclase porque `Guerrero` y `Mago` heredan de ella.

---

### ¿Para qué se usa la instrucción pass en Python?

La instrucción `pass` se usa para dejar una clase, función o bloque vacío sin producir error.

```python
class Arquero(Personaje):
    pass
```

Sirve como marcador cuando todavía no se quiere escribir código dentro de la clase.

---

### ¿Qué es la función integrada super() y para qué se usa?

`super()` es una función que nos deja acceder a métodos de la clase padre desde una clase hija.

```python
super().__init__(nombre, fuerza, inteligencia, defensa, vida)
```

Se usa para reutilizar código y evitar repetir instrucciones.

Beneficios:
- evita duplicar código
- mejora la organización
- facilita el mantenimiento del programa

---

### ¿En el video se menciona la herencia múltiple a qué se refiere?

La herencia múltiple ocurre cuando una clase hereda de varias clases al mismo tiempo.

```python
class PersonajeMagico(Guerrero, Mago):
    pass
```

Esto permite combinar características de varias clases en una sola.

---

### ¿Cuál es el beneficio de aplicar herencia en POO?

La herencia ayuda a reutilizar código y crear programas más ordenados.

Sus beneficios principales son:
- permite compartir métodos entre clases
- reduce código repetido
- facilita crear nuevas clases especializadas
- mejora la organización del programa

---

### Nuevo personaje agregado

Se agregó un nuevo personaje para practicar herencia.

```python
Miyu = Guerrero("Miyu", 18, 12, 9, 120, 6)
Miyu.atributos()
```

Este personaje tiene valores diferentes para demostrar cómo crear nuevos objetos a partir de una clase hija.

# Polimorfismo

Permite que diferentes clases utilicen un mismo método con comportamientos distintos.
Esto significa que varios objetos pueden responder al mismo mensaje de manera diferente según su tipo.

---

### ¿Para qué se usa el polimorfismo?

El polimorfismo se usa para escribir código más flexible y reutilizable.  
Permite trabajar con distintos objetos sin cambiar la función que los utiliza.  
Cada objeto ejecuta su propia versión del método.

Ejemplo:

```python
def definicion_bebida(bebida):
    bebida.que_soy()
```

La misma función puede recibir diferentes objetos:

```python
definicion_bebida(Cafe())
definicion_bebida(Te())
```

Cada objeto responde de forma distinta aunque se llame al mismo método.

---

### ¿Qué ocurre en el método daño(self, enemigo) si la fuerza es menor a la defensa?

Si la fuerza es menor que la defensa, el resultado del daño puede ser negativo.  
Eso provocaría que el enemigo recupere vida en lugar de perderla.  
Para evitarlo se debe comprobar que el daño mínimo sea cero.

Ejemplo corregido:

```python
def daño(self, enemigo):
    daño = self.fuerza - enemigo.defensa
    if daño < 0:
        daño = 0
    return daño
```

Así nunca se producirá daño negativo.

---

### Ejemplo de polimorfismo con otro objeto

En este ejemplo se usa el polimorfismo con vehículos.

```python
class Auto:
    def mover(self):
        print("El auto avanza por la carretera")

class Barco:
    def mover(self):
        print("El barco navega por el agua")

def desplazamiento(vehiculo):
    vehiculo.mover()

desplazamiento(Auto())
desplazamiento(Barco())
```

La función `desplazamiento()` usa el mismo método `mover()`,  
pero cada objeto realiza una acción diferente según su clase.

## Archivo del código fuente

[personaje.py](personaje.py) <br>
[personaje_encapsulado.py](personaje_encapsulado.py) <br>
[personaje_herencia.py](personaje_herencia.py) <br>
[personaje_polimorfismo.py](personaje_polimorfismo.py)
