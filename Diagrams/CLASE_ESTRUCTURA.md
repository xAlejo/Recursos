# DIAGRAMA ECHO EN CLASES
## CLASE: MASCOTA
```mermaid
classDiagram
class Mascota {
    +str nombre
    -int energia
    +int hambre
    +jugar() void
    +comer() void
    +dormir() void
    +get_energia() int
    +set_energia(nueva_energia : int) void
    +mostrar_estado() void
}
```
# ¿Mi clase tiene relaciones con otras clases? ¿Por qué?

* Mi clase Mascota es independiente y no tiene relaciones con otras clases, ya que:

* No hay herencia, porque no estoy usando ninguna otra clase como base.
* Los atributos que tiene (nombre, energía y hambre) son datos simples, no objetos de otras clases.
* Los métodos no reciben ni utilizan objetos de otras clases como parámetros.
* Aunque tenga mascota1 y mascota2, todas son de la misma clase y no interactúan con otras clases diferentes.

- Por eso, puedo decir que mi clase funciona de forma autónoma y no necesita relacionarse con otras clases dentro de este programa.

# ¿Mi diagrama refleja la estructura POO?

* Sí, mi diagrama refleja correctamente la estructura de Programación Orientada a Objetos, ya que representa la clase Mascota con sus atributos y métodos tal como los programé en Python.
Se respeta el encapsulamiento, porque el atributo energía es privado (__energia) y solo se puede acceder mediante métodos como get_energia y set_energia.
Además, los métodos como jugar, comer y dormir modifican el estado del objeto, lo que demuestra cómo se manejan los datos dentro de la clase.
También se distingue claramente entre atributos (datos) y métodos (acciones), lo cual es fundamental en POO.

- Por eso, el diagrama coincide con la lógica y estructura de mi código.
