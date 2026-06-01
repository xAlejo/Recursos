# CREACION DE BASE DE DATOS (GIMNASIO)

- Realizado por Alejo Burgos y Romina Valenzuela.

* A continuacion se hace muestra de la creacion y modificacion del trabajo solicitado.

## Foto del ejercicio como boceto.
![trabajo](https://github.com/xAlejo/Recursos/blob/main/Imagenes/IMG-20260529-WA0097.jpg?raw=true)

### Respuestas De Las Preguntas Realizadas
1- ¿Que formas normales uso y por que?

Formas normales que usamos: 1FN, 2FN y 3FN.

* 1FN : Campo atómicos, sin listas. PK en Clientes, Planes, etc.
* 2FN : Con PK simples, todo depense de la PKcompleta.
* 3FN : Sin dependencias transitiva. Ej : Nombre en Cliente depende solo de la Id_cliente.

2- ¿Cual fue la parte más compleja de resolver y por qué?

 Parte más compleja : Tabla Membresía. Es relación muchos a muchos entre Clientes y Planes. Tuvimos que usar Id_cliente + Id_plan como FK para unirlas sin repetir datos.

3- ¿Que tablas aun le faltaría a su sistema para producción y por qué?

Tablas que faltan para producción:

* Usuarios/Roles para login y permiso del sistema.
* Pagos para registrar cobro de membresías.
* Asistencia para control entrada de clientes a clases.
