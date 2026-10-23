# Nombre completo: Karla Aparicio
# Grupo: 951
# Fecha de realización: 21/10/2026
# Descripción general: Ejercicios de preprocesamiento de datos con pandas
#   (valores nulos y renglones duplicados).

import numpy as np
import pandas as pd



# Ejercicio 1

def porcentaje_nulos(df):
    return df.isnull().sum() / len(df)



# Ejercicio 2

def contar_duplicados(df):
    return int(df.duplicated().sum())



# Ejercicio 3


def eliminar_columnas_nulas(df, maximo):
    if not (0 <= maximo <= 1):
        raise ValueError("El porcentaje máximo debe estar entre 0 y 1.")
    porcentajes = df.isnull().sum() / len(df)
    columnas = porcentajes[porcentajes >= maximo].index.tolist()
    df.drop(columns=columnas, inplace=True)   # modifica el DataFrame original
    return columnas



# Ejercicio 4


def rellenar_nulos(df, columnas, metodo):
    if metodo not in ("mean", "bfill", "ffill"):
        raise ValueError("El método debe ser 'mean', 'bfill' o 'ffill'.")
    for col in columnas:
        if col not in df.columns:
            raise KeyError(f"La columna '{col}' no existe en el DataFrame.")
        if metodo == "mean":
            if not pd.api.types.is_numeric_dtype(df[col]):
                raise TypeError(f"La columna '{col}' no es numérica; no se puede usar 'mean'.")
            df[col] = df[col].fillna(df[col].mean())
        elif metodo == "bfill":
            df[col] = df[col].bfill()
        else:
            df[col] = df[col].ffill()
    return df



# Ejercicio 5

def eliminar_duplicados(df):
    antes = len(df)
    df.drop_duplicates(inplace=True)          # modifica el DataFrame original
    return antes - len(df)



if __name__ == "__main__":
    datos = pd.DataFrame({
        "edad":  [20, 21, np.nan, 21, 22, 20],
        "nota":  [8.0, np.nan, 9.0, np.nan, 7.5, 8.0],
        "grupo": ["A", "B", "A", "B", "A", "A"],
        "vacia": [np.nan] * 6,
    })

    print("Ejercicio 1 - Porcentaje de nulos por columna:")
    print(porcentaje_nulos(datos), "\n")

    print("Ejercicio 2 - Renglones duplicados:", contar_duplicados(datos), "\n")

    prueba = datos.copy()
    print("Ejercicio 3 - Columnas eliminadas (máximo 0.5):",
          eliminar_columnas_nulas(prueba, 0.5))
    print(prueba, "\n")

    try:
        eliminar_columnas_nulas(prueba, 1.5)
    except ValueError as e:
        print("Ejercicio 3 - Validación del máximo:", e, "\n")

    print("Ejercicio 4 - Nulos rellenados con 'mean':")
    print(rellenar_nulos(prueba, ["edad", "nota"], "mean"), "\n")

    try:
        rellenar_nulos(prueba, ["edad"], "median")
    except ValueError as e:
        print("Ejercicio 4 - Método inválido:", e, "\n")

    print("Ejercicio 5 - Renglones eliminados:", eliminar_duplicados(prueba))
    print(prueba)
