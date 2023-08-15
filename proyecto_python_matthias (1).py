
import pandas as pd
import os
#EN ESTE PUNTO HAY QUE COLOCAR LA RUTA DE LA CARPETA origen EN LA QUE EL CLIENTE INTRODUCE EL ARCHIVO ORIGINAL SIN CORREGIR.
df = pd.read_csv('https://github.com/GuillermoK1/Matthias/blob/main/import/export.csv', sep=";")
#################'||||||||||||||||||||||||||AQUÍ ARRIBA||||||||||||||||||||||||||||||'
#ESTA ES LA FUNCIÓN PARA CORREGIR EL FORMATO DE LOS NÚMEROS (1234,56)
'''
FALTA EL DETALLE DEL REDONDEO!!!
'''
def convertir_numero(numero):
    numero = numero.replace(',', '.')

    partes = numero.split('.')

    if len(partes) == 2:
        decimales = partes[1]
        if len(decimales) == 1:
            decimales += '0'
        numero = partes[0] + '.' + decimales
    elif len(partes) == 1:
        numero += '.00'

    return numero
#||||||||||||||| EN ESTA SECCIÓN APLCIO LA FUNCIÓN A LAS COLUMNAS INDEX 10 Y 14 ||||||||||||||||
df['Netto-Einkaufspreis (indiv., falls vorh.)'] =\
 df['Netto-Einkaufspreis (indiv., falls vorh.)'].apply(convertir_numero)

df['Katalogpreis / empf. VK - VK Brutto Preis ./. Rabatt'] =\
 df['Katalogpreis / empf. VK - VK Brutto Preis ./. Rabatt'].apply(convertir_numero)
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#Columna J: Si tiene una coma después del primer número, borrar lo que sigue a la coma (por ejemplo: 10,000 tiene que ser 10).
df['Gebindemenge / BMEcat Verpackungsmenge'] =\
 df['Gebindemenge / BMEcat Verpackungsmenge'].astype(str).str.split(',').str[0]

#|||||||Fecha de modificación (dd/mm/yy)||||||||||||
from datetime import date

df['Preisdatum EK / Konditionsdatum'] = date.today()
#|||||||||||||||||||||||||||||||||||||||||||||||||||
# Alinear los datos del Dataframe al lado derecho de cada casilla.
df = df.astype(str).apply(lambda x: x.str.rjust(20))
# ESTA FUNCIÓN DIVIDE EL ARCHIVO MODIFICADO EN ARCHIVOS DE MAX 15000 ROWS Y EXPORTA CADA "ARCHIVO.CSV" A UNA CARPETA LLAMADA "EXPORT_" EN SECUENCIA.
def dividir_y_exportar_dataframe(df, ruta_carpeta, num_filas=15000):
    num_archivos = len(df) // num_filas + 1
    for i in range(num_archivos):
        carpeta = os.path.join(ruta_carpeta, f'export_{i+1}')
        os.makedirs(carpeta, exist_ok=True)
        archivo_export = os.path.join(carpeta, 'archivo.csv')
        df[i*num_filas:(i+1)*num_filas].to_csv(archivo_export, index=False)

#|||||||||||||||||||||||Modificar la RUTA DE LA CARPETA "DESTINO". Aquí abajo.||||||||||||||||||||||||||||||||||||||
dividir_y_exportar_dataframe(df, 'https://github.com/GuillermoK1/Matthias/blob/main/import/export.csv')
