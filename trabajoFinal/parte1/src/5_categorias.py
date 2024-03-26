import pandas as pd

df = pd.read_pickle("trabajoFinal/data/interim/df_renombrada.pkl")

# Creamos un DataFrame vacío para almacenar los resultados
df_categoriasUnicas = pd.DataFrame(columns=['Variable renombrada', 'Categorías'])

# Iteramos sobre las columnas del DataFrame original
for columna in df.columns:
    # Calculamos el número de valores únicos en cada columna
    num_valores_unicos = df[columna].nunique()
    
    # Verificamos si el número de valores únicos es menor o igual a 15
    if num_valores_unicos <= 15:
        # Obtenemos los valores únicos
        categorias = list(df[columna].unique())
        
        # Añadimos los datos al nuevo DataFrame usando loc
        df_categoriasUnicas.loc[len(df_categoriasUnicas)] = [columna, categorias]

# Exportar DataFrame a Excel
archivo_excel = "trabajoFinal/references/diccionarioVariables.xlsx"
nombre_hoja = "categorías"
with pd.ExcelWriter(archivo_excel, mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
    df_categoriasUnicas.to_excel(writer, sheet_name=nombre_hoja, index=False)
    # Asegúrate de que la hoja esté activa antes de escribir en ella
    worksheet = writer.sheets[nombre_hoja]
