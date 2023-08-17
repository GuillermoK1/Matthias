import os
from archivo_py import funciones
files = []
archivo_import = os.getcwd() + '/import'
archivo_export = os.getcwd() + '/export'

if not os.path.exists(archivo_export):
    os.makedirs(archivo_export)

for file in os.listdir(archivo_import):
    if file.endswith('.csv'):
        files.append(file)

if len(files) == 0:
    print('No hay archivos CSV en la carpeta de importación.')

file_num = 1
for file in files:
    result = funciones(os.path.join(archivo_import, file))
    
    # Get the column names from the first row of the result
    column_names = result[0]
    
    result_parts = [result[i:i+14999] for i in range(0, len(result), 14999)]
    
    for part in result_parts:
        export_file = os.path.join(archivo_export, f'resultado_{file_num}.csv')
        with open(export_file, 'w') as f:
        
            f.write(','.join(column_names) + '\n')
            
            for row in part:
                f.write(','.join(row) + '\n')
        file_num += 1
