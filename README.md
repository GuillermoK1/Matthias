# Modificar CSV
## Situación:
Un cliente quiere una carpeta en la que pueda:
1º Poner un archivo para modificar.
2º Ejecutar un programa.
3º Sacar el/los archivo/s modificado/s.

>[!IMPORTANT]
>El cliente necesita conservar todos los archivos (el archivo sin modificacion y los archivos modificados).
>Todos tienen que estar en el mismo formato (CSV).
>Un archivo modificado sólo puede tener 15000 filas máximo (si hay mas filas para modificar, dividirlo).
>
>[!NOTE]
>Ejemplo division: `Total rows: 42000 - 1. Archivo 15000 - 2. Archivo 15000 - 3. Archivo 12000`

Crea una carpeta raíz con una estructura para que el cliente sepa qué hacer.
La carpeta debe contener el programa para ejecutar.
EL cliente puede introducir el archivo en esa carpeta.
Al ejecutar el programa, este buscará el archivo automáticamente dentro de la carpeta raíz y procesará la información dentro del archivo, luego creará los archivos modificados dentro de la carpeta raíz. Como resultado, en la carpeta raíz habrán los siguientes objetos:
EL PROGRAMA EJECUTABLE
EL ARCHIVO ORIGINAL
EL/LOS ARCHIVO/S MODIFICADO/S

Luego el cliente podrá llevarse sus archivos y para almacenarlos donde desee.

### Datos para modificar.
Formatear las columnas y el dataframe para que el esquema sea consistente.

Precios: Tiene que tener dos decimales despues de la coma y redondeado
`1234,5678 -> 1234,57`
Column-Index: 10 y 14

Fecha: Tiene que agregar la fecha de modificacion en una columna (formato: dd/mm/yyyy).
