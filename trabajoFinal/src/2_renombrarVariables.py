import pandas as pd

df_variablesRelevantes = pd.read_pickle('trabajoFinal/data/interim/df_manteniendo_variablesRelevantes.pkl')

df_renombramiento = pd.read_excel("trabajoFinal/references/diccionarioVariables.xlsx",
                                  sheet_name='diccionarioVariables',
                                  usecols=['Variable original', 'Variable renombrada'],
                                  index_col='Variable original',
                                  nrows=40)

dict_renombramiento = df_renombramiento['Variable renombrada'].to_dict()

df_renombrada = df_variablesRelevantes.rename(columns=dict_renombramiento)

df_renombrada.to_pickle("trabajoFinal/data/interim/df_renombrada.pkl")