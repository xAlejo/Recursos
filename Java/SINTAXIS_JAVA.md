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

# Módulos y Clases

¿Para qué se usan los módulos?

Los módulos se usan para organizar el código en diferentes partes, facilitando la reutilización y el orden dentro de un proyecto.

¿Qué es el comando javac y cuál es su función?

El comando javac se utiliza para compilar archivos de Java. Su función es transformar el código fuente (.java) en código ejecutable (.class) que la máquina virtual de Java puede interpretar.

# Mascota.java y Main.java

* Para este ejercicio creé una clase Mascota con atributos y métodos similares a los usados en Python, aplicando conceptos de POO.
* Además, utilicé una clase principal (Main) para ejecutar el programa y crear instancias de la clase.
* Esto permite entender cómo se organizan las clases en Java y cómo interactúan entre sí dentro de un programa.

