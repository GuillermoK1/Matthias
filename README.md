# Modificar CSV
## Situación
Un cliente quiere una carpeta, en la que pueda, 1º poner un archivo para modificar, 2º ejecutar un programa, 3º sacar el/los archivo/s modificado/s.

El cliente necesita conservar todos los archivos. El archivo sin modificacion y los archivos modificados. Todos tienen que estar en el mismo formato (letras/seperador).
Un archivo modificado sólo puede tener 15000 filas máximo. Si hay mas filas para modificar, dividirlo. 
Ejemplo division: `Total rows: 42000 - 1. Archivo 15000 - 2. Archivo 15000 - 3. Archivo 12000`

Crea una carpeta con una estructura para que el cliente sepa qué hacer.
La carpeta debe contener el programa para ejecutar. Y una structura para que el cliente puede poner y sacar sus archivos.

### Datos para modificar.
Forzar los diferentes formatos de las columnas a un solo formato, que sea consistente. 

Precios: Tiene que tener dos decimales despues de la coma y redondeado
`1234,5678 -> 1234,57`
Column-Index: 10 y 14

Fecha: Tiene que agregar la fecha de modificacion en una columna. Formato: 15.08.2023
Column-Index: 13
