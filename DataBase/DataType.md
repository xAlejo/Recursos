# Tipos de datos en DB

*  CHAR <br>
¿Cuál es la característica principal del tipo de dato CHAR en cuanto a su almacenamiento y qué sucede si el contenido ingresado es menor a la longitud definida?
- se encarga de almacenar datos con una longitud fija, osea si se suben datos a la red esta siempre va a ocupar el mismo espacio y si el contenido ingresado es menor a la longitud definida la misma base de datos va a rellenar los espacios faltantes con espacios en blanco hasta rellenar el espacio fijo

![char](https://github.com/xAlejo/Recursos/blob/main/Imagenes/1.png?raw=true)

* VARCHAR <br>
¿En qué se diferencia principalmente VARCHAR de CHAR y por qué se considera más eficiente para almacenar datos como nombres o direcciones?
- Permite almacenar cadenas de longitud variable y solo ocupa el espacio necesario y esto permite poder poner direcciones, nombres y datos sin preocuparnos del espacio o tamaño que tiene o va a ocupar

![Varchar](https://github.com/xAlejo/Recursos/blob/main/Imagenes/2.png?raw=true)

* TEXT <br>
¿Para qué tipo de escenarios está diseñado el tipo de dato TEXT y cuál es su ventaja respecto a la limitación de caracteres en comparación con los otros tipos vistos?
- esta diseñada para almacenar grandes cantidades de texto o cadenas muy largas, y su ventaja es que no tiene limitacion ya que permite almacenar mayor cantidad de caracteres que CHAR Y VARCHAR.

* Análisis de caso práctico <br>
Si tuvieras que diseñar una base de datos para almacenar matrículas vehiculares que siempre tienen un formato estándar de 7 caracteres, ¿qué tipo de dato elegirías y por qué?
- Usaria CHAR ya que todas las matricular tendrian el mismo tamaño y este sera fijo y que la busqueda de los datos suele ser mas rapida y eficiente para datos constantes.

* Gestión de almacenamiento <br>
 ¿Qué riesgo existe al definir una longitud de caracteres excesivamente grande en un campo VARCHAR si los datos reales son pequeños?
- Si un VARCHAR tiene un tamaño demasiado grande, la base de datos puede volverse más lenta y usar recursos innecesarios, aunque los datos guardados sean pequeños. Por eso es mejor usar un tamaño adecuado
