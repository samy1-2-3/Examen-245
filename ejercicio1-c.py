import pandas as pd
import numpy as np
from scipy import stats

def leer(name, primera_fila=True):
    if primera_fila:
        return pd.read_csv(name, skiprows=1).values.tolist()
    else:
        return pd.read_csv(name).values.tolist()

def incisos(datos):
    df = pd.DataFrame(datos)
    
    # media
    media = np.mean(df)
    
    # mediana
    mediana = np.median(df)
    
    # moda
    moda = stats.mode(df)[0][0]
    
    # media geométrica
    geometrica = stats.gmean(df)
    
    return media, mediana, moda, geometrica

datos = leer('C:\\Users\\Lenovo\\Desktop\\asd\\heart_failure_clinical_records_dataset.csv')

media, mediana, moda, geometrica = incisos(datos)

print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)
print("Media Geométrica:", geometrica)
