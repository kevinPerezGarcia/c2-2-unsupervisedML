import pandas as pd

df = pd.read_pickle("trabajoFinal/data/interim/df_renombrada.pkl")

# Creamos un DataFrame vacío para almacenar los resultados
df_valoresUnicos = pd.DataFrame(columns=['Variable renombrada', 'Número de valores únicos'])

# Iteramos sobre las columnas del DataFrame original
for columna in df.columns:
    # Calculamos el número de valores únicos en cada columna
    num_valores_unicos = df[columna].nunique()
    
    # Añadimos los datos al nuevo DataFrame usando loc
    df_valoresUnicos.loc[len(df_valoresUnicos)] = [columna, num_valores_unicos]

# Exportar DataFrame a Excel
archivo_excel = "trabajoFinal/references/diccionarioVariables.xlsx"
nombre_hoja = "valoresUnicos"
with pd.ExcelWriter(archivo_excel, mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
    df_valoresUnicos.to_excel(writer, sheet_name=nombre_hoja, index=False)
    # Asegúrate de que la hoja esté activa antes de escribir en ella
    worksheet = writer.sheets[nombre_hoja]
