# Resumen Video Cardinalidad

## 1. Notación Clásica

### Uno a Uno (1:1)

Cada elemento de una entidad se relaciona únicamente con un elemento de otra entidad.

Ejemplos:

- Vehículo y número de bastidor
- Cuenta bancaria e IBAN
- Persona y DNI

---

### Uno a Muchos (1:N)

Un elemento de una entidad puede relacionarse con varios elementos de otra, pero no al revés.

Ejemplos:

- Cliente y pedidos
- Libro y capítulos
- Cuenta bancaria y movimientos
- Paciente y citas médicas

---

### Muchos a Muchos (N:M)

Varios elementos de una entidad se relacionan con varios elementos de otra.

Ejemplos:

- Persona e idiomas
- Actor y películas
- Alumno y asignaturas
- Pedido y transportista

---

# 2. Notación de Mínimos y Máximos

Esta notación indica la participación mínima y máxima en una relación.

---

### 0..1

La relación puede no existir o ser única.

Ejemplo:

- Persona y DNI en menores de edad

---

### 0..N

Permite desde cero hasta muchas relaciones.

Ejemplo:

- Persona y coches poseídos

---

### 1..1

La relación es obligatoria y única.

Ejemplo:

- Vehículo y número de bastidor

---

### 1..N

La relación exige al menos una relación, pero puede tener muchas.

Ejemplos:

- Profesor y asignaturas
- Madre e hijo

---

# Conclusión

La cardinalidad depende del contexto del negocio y de las reglas definidas por la organización.


# 7 Ejemplos (Fotos)
![ejemplos1](https://github.com/xAlejo/Recursos/blob/main/Imagenes/20260521_165851.jpg?raw=true)
