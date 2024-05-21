import pandas as pd

def cargaD(nombre_archivo, omitir_primera_fila=True):
    if omitir_primera_fila:
        return pd.read_csv(nombre_archivo, skiprows=1).values.tolist()
    else:
        return pd.read_csv(nombre_archivo).values.tolist()

def ultimo_cuartil(datos):
    valores = [float(valor) for fila in datos for valor in fila]
    ultimo_cuartil = pd.Series(valores).quantile(0.75)
    print("Último cuartil:", ultimo_cuartil)

def percentil_80(datos):
    valores = [float(valor) for fila in datos for valor in fila]
    percentil_80 = pd.Series(valores).quantile(0.8)
    return percentil_80

# Cargar datos desde el archivo CSV
datos = cargaD('C:\\Users\\Lenovo\\Desktop\\asd\\heart_failure_clinical_records_dataset.csv')
ultimo_cuartil(datos)
percentil_80 = percentil_80(datos)
print("Percentil 80:", percentil_80)
