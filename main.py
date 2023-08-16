import os
#import shutil
from archivo_py import funciones
'''
Mirar carpeta_import y carpeta_export.
'''
files = []
archivo_import = os.getcwd() + '/import'
archivo_export = os.getcwd() + '/export'

# Crear la carpeta de exportación si no existe
if not os.path.exists(archivo_export):
    os.makedirs(archivo_export)

for file in os.listdir(archivo_import):
    if file.endswith('.csv'):
        files.append(file)

if len(files) == 0:
    print('No hay archivos CSV en la carpeta de importación.')

file_num = 1
for file in files:
    # Realizar las funciones del archivo.py en el archivo CSV
    result = funciones(os.path.join(archivo_import, file))
    
    # Dividir el resultado en partes de 15000 filas
    '''
    result_parts = [result[i:i+15000] for i in range(0, len(result), 15000)]
    
    # Exportar cada parte a un archivo separado
    for part in result_parts:
        export_file = os.path.join(archivo_export, f'resultado_{file_num}.csv')
        with open(export_file, 'w') as f:
            for row in part:
                f.write(','.join(row) + '\n')
        file_num += 1
