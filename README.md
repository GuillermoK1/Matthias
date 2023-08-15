# Modificar CSV
## Situacion
Un cliente quiere una carpeta, en la que pueda, 1º poner un archivo para modificar, 2º ejecutar un programa, 3º sacar el/los archivo/s modificado/s.

El cliente necesita conservar todos los archivos. El archivo sin modificacion y los archivos modificados. Todos tienen que estar en el mismo formato (letras/seperador).
Un archivo modificado sólo puede tener 15000 rows máximo. Si hay mas rows para modificar, divídelo. 
Ejemplo division: `Total rows: 42000 - 1. Archivo 15000 - 2. Archivo 15000 - 3. Archivo 12000`

Crea una carpeta con una estructura para que el cliente sepa qué hacer.
La carpeta debe contener el programa para ejecutar. Y una structura para que el cliente puede poner y sacar sus archivos.

### Datos para modificar
Precios: Tiene que tener dos decimales despues de la coma y redondeado
`1234,5678 -> 1234,57`
Column-Index: 10 y 14

Dato: Tiene que tener el dato de modificacion. Formato: 15.08.2023
Column-Index: 13
