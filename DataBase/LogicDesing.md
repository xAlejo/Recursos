# Base de Datos
Tablas: <br>
![tabla mascota](https://github.com/xAlejo/Recursos/blob/main/Imagenes/20260521_152654.jpg?raw=true)
![tabla mascota 2](https://github.com/xAlejo/Recursos/blob/main/Imagenes/20260521_153112.jpg?raw=true)
# ¿Qué es una Base de Datos?

Una base de datos es un conjunto organizado de información almacenada de forma estructurada en un sistema, para que pueda ser fácilmente consultada, modificada y gestionada.

Sirve para guardar información sin perderla y poder acceder a ella rápidamente.

---

# Componentes Claves

## Tablas
Lugar donde se guardan los datos en filas y columnas.

## Registros
Cada fila de la tabla. Representa un dato específico.

## Campos
Cada columna de la tabla. Representa un atributo del dato.

---

# Tipos de Base de Datos

## Relacionales (SQL)

Usan tablas relacionadas entre sí.

Ejemplos:

- MySQL
- PostgreSQL
- SQL Server
- SQLite

## No Relacionales (NoSQL)

Guardan datos más flexibles y sin estructura fija.

Ejemplo:

- MongoDB

---

# ¿Por qué usar FLOAT en vez de INT?

En el ejemplo visto en clases era mejor usar FLOAT porque permite usar números decimales, mientras que INT solamente permite números enteros.

Por ejemplo:

- 0.5 representa 6 meses
- 0.2 podría representar algunos meses

Con INT solamente podríamos usar:

- 0
- 1

y se perdería precisión.

Aun así, usar FLOAT para edad no es lo más recomendable en una base de datos real.

---

# Problema de guardar la edad

El problema de ingresar directamente la edad es que ese número quedará guardado sin cambiar automáticamente.

Por ejemplo:

Si hoy una mascota tiene 3 años, el próximo año seguirá diciendo 3 años si nadie actualiza el dato manualmente.

Esto puede generar:

- Información desactualizada
- Confusión
- Errores en el sistema

La mejor opción es guardar la fecha de nacimiento usando el tipo DATE y calcular la edad automáticamente cuando sea necesaria.

Así se obtiene:

- Años
- Meses
- Días

con mayor precisión.

---

# Dato vs Realidad

En la pizarra se usó el ejemplo de guardar 0.5 en FLOAT para representar un cachorro de 6 meses.

El problema técnico es que el sistema no sabría el día exacto de nacimiento.

Entonces, si el sistema tuviera que enviar automáticamente un mensaje de:

"Feliz Cumpleaños"

no podría saber cuándo corresponde realmente.

Además, 0.5 representa solamente la mitad de un entero, pero un año tiene 12 meses, por lo que el cálculo sería incorrecto y podría generar errores en fechas o recordatorios.

Con DATE sí se puede calcular correctamente el cumpleaños y la edad exacta.

---

# Modelo Entidad Relación (MER)

En clases también se trabajó con un Modelo Entidad Relación.

Las entidades fueron:

- Mascota
- Tutor

---

# Corrección de Cardinalidad

## 1. Detección de Error

Una tabla intermedia como MASCOTA_TUTOR se utiliza realmente para relaciones Muchos a Muchos (N:M). Esto ocurre porque una mascota puede tener varios tutores y un tutor puede tener varias mascotas.

En bases de datos relacionales no se puede crear directamente una relación N:M, por eso se utiliza una tabla intermedia que divide la relación en dos relaciones 1:N.

Si en la pizarra se indicó una relación N:1, entonces crear MASCOTA_TUTOR sería una contradicción, ya que para N:1 no se necesita tabla intermedia.

---

## 2. Contexto de Negocio

### Caso A: Clínica Veterinaria Hogar

Una mascota solo puede tener un dueño responsable.

Cardinalidad:

- Un tutor → muchas mascotas
- Una mascota → un tutor

Relación:

1:N

---

### Caso B: Hotel de Mascotas Premium

Una mascota puede ser retirada por varios tutores y un tutor puede tener varias mascotas.

Cardinalidad:

N:M

En este caso sí es necesario usar una tabla intermedia como MASCOTA_TUTOR.

porque los motores de bases de datos relacionales no pueden manejar directamente una relación Muchos a Muchos.

Por eso se transforma en dos relaciones Uno a Muchos.

---
