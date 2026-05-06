# Sintaxis básica de Java

## Texto (String)

```java
String nombre = "Alejo";
```

Comentario: Se usa para almacenar texto o cadenas de caracteres.

---

## Números (int / double)

```java
int edad = 24;
double altura = 1.75;
```

Comentario: int se usa para números enteros y double para números con decimales.

---

## Booleanos (boolean)

```java
boolean activo = true;
```

Comentario: Representa valores de verdadero o falso.

---

## Listas (ArrayList)

```java
import java.util.ArrayList;

ArrayList<String> lista = new ArrayList<>();
lista.add("uno");
lista.add("dos");
```

Comentario: Permite almacenar múltiples valores en una colección dinámica.

---

## Objetos

```java
class Persona {
    String nombre;
}
```

# HashMap

¿Qué es y para qué se utiliza un HashMap?

Un HashMap es una estructura de datos que almacena información en pares clave-valor. Se utiliza para guardar datos donde cada valor tiene una clave única para acceder a él de forma rápida.

¿Cómo se importa?

```java
import java.util.HashMap;
```

¿Cuántos tipos se mencionan en el video?

Se mencionan principalmente dos tipos: la clave (Key) y el valor (Value).

Ejemplo de código:

```java
import java.util.HashMap;

HashMap<String, Integer> edades = new HashMap<>();

edades.put("Alejo", 24);
edades.put("Juan", 30);

System.out.println(edades.get("Alejo"));
```



Comentario: Un objeto es una instancia de una clase que contiene atributos y métodos.

