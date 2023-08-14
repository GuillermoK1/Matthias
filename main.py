import os

files = []

archivo_import = os.getcwd() + '/import'

for file in os.listdir(archivo_import):
    print(file)
    if file.endswith('.csv'):
        files.append(file)


while True:
    if len(files) == 0:
        print('no hay files')
        break

    for file in files:
        print('ahora hago algo con', file)

