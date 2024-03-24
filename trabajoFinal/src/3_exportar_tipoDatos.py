import pandas as pd
from datetime import datetime

df_renombrada = pd.read_pickle("trabajoFinal/data/interim/df_renombrada.pkl")

# Crear DataFrame con los tipos de datos
df_tiposDatos = df_renombrada.dtypes.reset_index()
df_tiposDatos.columns = ["Variable original", "Tipo de dato original"]

# Obtener la hora actual
hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Exportar DataFrame a Excel
archivo_excel = "trabajoFinal/references/diccionarioVariables.xlsx"
nombre_hoja = "tipoDatos"
with pd.ExcelWriter(archivo_excel, mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
    df_tiposDatos.to_excel(writer, sheet_name=nombre_hoja, index=False)
    # Asegúrate de que la hoja esté activa antes de escribir en ella
    worksheet = writer.sheets[nombre_hoja]
    # Escribir la hora en una celda específica (por ejemplo, en la fila siguiente a los datos)
    ultima_fila = len(df_tiposDatos) + 3  # Suponiendo que quieres dejar una fila de espacio
    worksheet.cell(row=ultima_fila, column=1, value="Hora de ejecución:")
    worksheet.cell(row=ultima_fila, column=2, value=hora_actual)

# Nota: El modo 'a' (append) en ExcelWriter podría no funcionar como se espera con if_sheet_exists='replace',
# ya que este intentará reemplazar la hoja existente. Si encuentras problemas, considera el uso de otra estrategia,
# como leer y modificar el archivo Excel directamente con openpyxl antes de usar pandas para exportar el DataFrame.