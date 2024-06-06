import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.decomposition import PCA

# normalizar los datos
def normalizar(datos):
    scaler = StandardScaler()
    datos_normalizados = scaler.fit_transform(datos)
    return datos_normalizados

# escalar características usando MinMaxScaler
def escalar_caracteristicas(datos):
    scaler = MinMaxScaler()
    datos_escalados = scaler.fit_transform(datos)
    return datos_escalados


# imputar valores perdidos
def imputar_valores_perdidos(datos, estrategia='mean'):
    imputer = SimpleImputer(strategy=estrategia)
    datos_imputados = imputer.fit_transform(datos)
    return datos_imputados


# detectar y eliminar duplicados
def eliminar_duplicados(datos):
    datos_sin_duplicados = datos.drop_duplicates()
    return datos_sin_duplicados


# detectar y manejar valores atípicos usando el rango intercuartil (IQR)
def manejar_valores_atipicos(datos, columnas):
    Q1 = datos[columnas].quantile(0.25)
    Q3 = datos[columnas].quantile(0.75)
    IQR = Q3 - Q1
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    datos_sin_atipicos = datos[~((datos[columnas] < limite_inferior) | (datos[columnas] > limite_superior)).any(axis=1)]
    return datos_sin_atipicos


datos = pd.read_csv('heart_failure_clinical_records_dataset.csv')
print(datos)

print("DATOS SIN DUPLICADOS-------------------------- ")
datos_sin_duplicados = eliminar_duplicados(datos)
print(datos_sin_duplicados)

print("DATOS IMPUTADOS ---------------------------")
datos_imputados = imputar_valores_perdidos(datos_sin_duplicados, estrategia='mean')
print(datos_imputados)

print("DATOS NORMALIZADOS-------------------------- ")
datos_normalizados = normalizar(datos_imputados)
print(datos_normalizados)

print("DATOS ESCALADOS-----------------------------")
datos_escalados = escalar_caracteristicas(datos_imputados)
print(datos_escalados)

columnas_numericas = datos.select_dtypes(include=[np.number]).columns
print("DATOS SIN ATIPICOS--------------------------")
datos_sin_atipicos = manejar_valores_atipicos(datos, columnas_numericas)
print(datos_sin_atipicos)

