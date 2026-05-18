# Base de Datos
(Faltan las fotos)
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

# Cardinalidad

La cardinalidad indica cuántos registros de una tabla se relacionan con registros de otra tabla.

---

# Caso A - Relación 1 a 1

En una veterinaria solamente se permite un dueño por mascota.

Entonces:

- Una mascota tiene un solo dueño
- Un dueño tiene una sola mascota

La relación sería:

1 : 1

o también:

(1..1)

---

# Caso B - Relación Muchos a Muchos

En un hotel para mascotas, varias personas pueden retirar a una mascota y además un tutor puede tener varias mascotas.

Entonces:

- Una mascota puede tener varios tutores
- Un tutor puede tener varias mascotas

La relación sería:

N : M

---

# Tabla Intermedia

Para resolver relaciones Muchos a Muchos se utiliza una tabla intermedia.

También se conoce como:

- Tabla asociativa
- Tabla pivote
- Junction table

En clases se creó la tabla:

Mascota_Tutor

porque los motores de bases de datos relacionales no pueden manejar directamente una relación Muchos a Muchos.

Por eso se transforma en dos relaciones Uno a Muchos.

---
