import pandas as pd
import matplotlib.pyplot as plt

def cargar_datos_desde_csv(nombre_archivo, omitir_primera_fila=True):
    if omitir_primera_fila:
        return pd.read_csv(nombre_archivo, skiprows=1).values.tolist()
    else:
        return pd.read_csv(nombre_archivo).values.tolist()

def graficar_datos(datos):

    df = pd.DataFrame(datos)
    num_columnas = df.shape[1]
    fig, axs = plt.subplots(num_columnas, figsize=(10, 6))
    for i in range(num_columnas):
        axs[i].hist(df[i], bins=20)
        axs[i].set_title(f'Columna {i+1}')
        axs[i].set_xlabel('Valor')
        axs[i].set_ylabel('Frecuencia')
    
    plt.tight_layout() 
    plt.show()

datos = cargar_datos_desde_csv('C:\\Users\\Lenovo\\Desktop\\asd\\heart_failure_clinical_records_dataset.csv')
graficar_datos(datos)
