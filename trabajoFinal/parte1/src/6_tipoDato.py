import pandas as pd

df = pd.read_pickle("trabajoFinal/data/interim/df_renombrada.pkl")

df_tipoDatos = pd.read_excel("trabajoFinal/references/diccionarioVariables.xlsx",
                             sheet_name="diccionarioVariables",
                             usecols=['Variable renombrada', "Tipo de dato adecuado"],
                             index_col='Variable renombrada',
                             nrows=40)

dict_tipoDatos = df_tipoDatos['Tipo de dato adecuado'].to_dict()

for columna, tipo_dato in dict_tipoDatos.items():
    df[columna] = df[columna].astype(tipo_dato)
    
df.to_pickle("trabajoFinal/data/interim/df_tipoDato.pkl")