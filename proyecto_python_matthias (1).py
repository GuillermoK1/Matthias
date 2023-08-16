import pandas as pd
import os

ruta_import = os.getcwd()
archivos = os.listdir(ruta_import)
archivos_csv = [archivo for archivo in archivos if archivo.endswith('.csv')]

for archivo_csv in archivos_csv:
    ruta_archivo = os.path.join(ruta_import, archivo_csv)

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

df['Netto-Einkaufspreis (indiv., falls vorh.)'] =\
 df['Netto-Einkaufspreis (indiv., falls vorh.)'].apply(convertir_numero)

df['Katalogpreis / empf. VK - VK Brutto Preis ./. Rabatt'] =\
 df['Katalogpreis / empf. VK - VK Brutto Preis ./. Rabatt'].apply(convertir_numero)

df['Gebindemenge / BMEcat Verpackungsmenge'] =\
 df['Gebindemenge / BMEcat Verpackungsmenge'].astype(str).str.split(',').str[0]

from datetime import date
df['Preisdatum EK / Konditionsdatum'] = date.today()

def dividir_y_exportar_dataframe(df, num_filas=5000):
    ruta_carpeta = os.getcwd()
    num_archivos = len(df) // num_filas + 1
    carpeta = os.path.join(ruta_carpeta, 'export')
    os.makedirs(carpeta, exist_ok=True)
    for i in range(num_archivos):
        archivo_export = os.path.join(carpeta, f'archivo_{i+1}.csv')
        df[i*num_filas:(i+1)*num_filas].to_csv(archivo_export, index=False)
