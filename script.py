import os
import pandas as pd
from datetime import date
MaxRows = 5000
def convertir_numero(numero):
    numero = numero.replace(',', '.')
    numero = str(round(float(numero), 2))
    partes = numero.split('.')

    if len(partes) == 2:
        decimales = partes[1]
        if len(decimales) == 1:
            decimales += '0'
        numero = partes[0] + '.' + decimales
    elif len(partes) == 1:
        numero += '.00'

    return numero

files = []
carpeta_import = os.getcwd() + '/import'
carpeta_export = os.getcwd() + '/export'

if not os.path.exists(carpeta_export):
    os.makedirs(carpeta_export)

for file in os.listdir(carpeta_import):
    if file.endswith('.csv'):
        files.append(file)

if len(files) == 0:
    print('No hay archivos CSV en la carpeta de importación.')

file_num = 1
for file in files:
    # Load the data from the CSV file into a DataFrame
    df = pd.read_csv(os.path.join(carpeta_import, file), sep=';')

    # Apply the convertir_numero function to the specified columns
    df['Netto-Einkaufspreis (indiv., falls vorh.)'] =\
     df['Netto-Einkaufspreis (indiv., falls vorh.)'].apply(convertir_numero)

    df['Katalogpreis / empf. VK - VK Brutto Preis ./. Rabatt'] =\
     df['Katalogpreis / empf. VK - VK Brutto Preis ./. Rabatt'].apply(convertir_numero)

    # Split the 'Gebindemenge / BMEcat Verpackungsmenge' column and keep only the first part
    df['Gebindemenge / BMEcat Verpackungsmenge'] =\
     df['Gebindemenge / BMEcat Verpackungsmenge'].astype(str).str.split(',').str[0]

    # Set the 'Preisdatum EK / Konditionsdatum' column to today's date
    today = date.today()
    formatted_date = today.strftime('%d/%m/%Y')
    df['Preisdatum EK / Konditionsdatum'] = formatted_date

    # Split the DataFrame into parts of 15000 rows each
    result_parts = [df[i:i+MaxRows] for i in range(0, len(df), MaxRows)]

    for part in result_parts:
        export_file = os.path.join(carpeta_export, f'resultado_{file_num}.csv')

        # Write the part to a new CSV file
        part.to_csv(export_file, index=False)

        file_num += 1
