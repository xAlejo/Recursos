# Pasos instalacion Postgres 9.5 en Windows
## Paso 1: Descarga del PostgreSQL
* Nos dirigimos a la pagina del programa: https://www.enterprisedb.com/download-postgresql-binaries y seleccionamos la version mas actual o recomendada ( En mi caso descargare la version 9.5 ).

![paso1](https://github.com/xAlejo/Recursos/blob/main/DataBase/Postgresql/pg_pasos/paso_1.png?raw=true.png)

## Paso 2: Extraccion del archivo
* Una vez descargado el archivo nos vamos a la ubicacion de descarga y seguimos los siguentes pasos: click derecho en el archivo, seleccionar extrar todo, esperar a que termine la extraccion, abrimos el archivo.

![paso2](https://github.com/xAlejo/Recursos/blob/main/DataBase/Postgresql/pg_pasos/paso_2.png?raw=true.png)

## Paso 3: Apertura de PowerShell en la carpeta pgsql
* apretamos la barra de direcciones y escribimos powershell, seguido apretamos enter para que se ejecute la terminal

![Paso3](https://github.com/xAlejo/Recursos/blob/main/DataBase/Postgresql/pg_pasos/paso_3.png?raw=true.png)

* asi deberia verse la terminal con la ruta del archivo.
![paso4](https://github.com/xAlejo/Recursos/blob/main/DataBase/Postgresql/pg_pasos/paso_4.png?raw=true.png)

## Paso 4: inicar postgres

1. Crear el clúster de datos
* Con la termianl abierta ejecutamos el siguente comando:
```powershell
.\bin\initdb.exe -D data -U postgres -W -E UTF8
```
* Este comando lo utilizamos para la creacion de la estructura de carpetas y archivos donde el servidor almacenará las bases de datos, usuarios, configuraciones y demás información necesaria para funcionar.

![paso5](https://github.com/xAlejo/Recursos/blob/main/DataBase/Postgresql/pg_pasos/paso_5.png?raw=true.png)

2. Iniciar el servidor:
```powershell
.\bin\pg_ctl.exe -D data -l logfile start
```
3. Verificar que está funcionando:
```powershell
.\bin\pg_isready.exe
```
* Como deberia verse:

![paso6](https://github.com/xAlejo/Recursos/blob/main/DataBase/Postgresql/pg_pasos/paso_6.png?raw=true.png)

4. Conectarse:
```powershell
.\bin\psql.exe -U postgres
```
o
```powershell
.\bin\psql.exe -h localhost -U postgres
```
* si sale de la siguente forma es porque ya estamos conectados correctamente al servidor PostgreSQL

![paso7](https://github.com/xAlejo/Recursos/blob/main/DataBase/Postgresql/pg_pasos/paso_7.png?raw=true.png)

4.1 verificamos la version
* para salir del comando anterior ingresamos el comando \q
```powershell
.\bin\postgres.exe --version
```

![paso_8](https://github.com/xAlejo/Recursos/blob/main/DataBase/Postgresql/pg_pasos/paso_8.png?raw=true.png)

5. Ejecutar pg admin

![paso9](https://github.com/xAlejo/Recursos/blob/main/DataBase/Postgresql/pg_pasos/paso_9.png?raw=true.png)

6. Pgadmin3 abierto

![paso10](https://github.com/xAlejo/Recursos/blob/main/DataBase/Postgresql/pg_pasos/paso_10.png?raw=true.png)

7. Conexion
* Hacemos click en el icono del enchufe para agregar una conexion a un servidor ( esperar a que se abra la pestaña para registrar el nuevo servidor).

![paso11](https://github.com/xAlejo/Recursos/blob/main/DataBase/Postgresql/pg_pasos/paso_11.png?raw=true.png)

8. formulario
* En esta seccion rellenaremos el formulario con los siguentes datos y le damos al boton OK:
- Name: mi base de datos
- Host: localhost
- Port: 5432
- Maintenance DB: postgres
- Username: postgres
- Password: 123

