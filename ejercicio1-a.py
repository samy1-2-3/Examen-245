import csv

def cargaD(nombre_archivo, omitir_primera_fila=True):
    datos = []
    with open(nombre_archivo, newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        if omitir_primera_fila:
            next(lector_csv)  
        for fila in lector_csv:
            datos.append(fila)
    return datos

def ultimo_cuartil(datos):
    valores = [float(valor) for fila in datos for valor in fila]
    valores_ordenados = sorted(valores)
    cantidad_datos = len(valores_ordenados)
    indice_cuartil = int(cantidad_datos * 0.75)
    ultimo_cuartil = valores_ordenados[indice_cuartil]
    print("Último cuartil:", ultimo_cuartil)

def percentil_80(datos):
    valores = [float(valor) for fila in datos for valor in fila]
    valores_ordenados = sorted(valores)
    cantidad_datos = len(valores_ordenados)
    indice_percentil_80 = int(cantidad_datos * 0.8)
    percentil_80 = valores_ordenados[indice_percentil_80]
    return percentil_80


datos = cargaD('C:\\Users\\Lenovo\\Desktop\\asd\\heart_failure_clinical_records_dataset.csv')
ultimo_cuartil(datos)
percentil_80 = percentil_80(datos)
print("Percentil 80:", percentil_80)
