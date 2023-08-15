# Modificar CSV
## Situacion
Un cliente quiere una carpeta, en que puede 1. poner un archivo para modificar 2. ejecutar un programa 3. sacar el/los archivo/s modificado/s.
El necesita todos archivos. El archivo sin modificacion y los archivos modificados. Todos tienen que estar en el mismo formato (letros/seperator).
Un archivo modificado solo puede tener 15000 rows. Si hay mas rows para modificar, dividelo. 
Ejemplo division: `Total rows: 42000 - 1. Archivo 15000 - 2. Archivo 15000 - 3. Archivo 7000`

Crea una carpeta con una structura para que el cliente sabe que hacer.
La carpeta tiene que hacer el programa para ejecutar. Y una structura para que el cliente puede poner y sacar sus archivos.

### Datos para modificar
Precios: Tiene que tener dos decimales despues del comma y redondeado
`1234,5678 -> 1234,57`
Column-Index: 10 y 14

Dato: Tiene que tener el dato de modificacion. Formato: 15.08.2023
Column-Index: 13
