import pandas as pd

df = pd.read_csv("trabajoFinal/data/raw/data-parte1.csv")

df_variablesRelevantes = df.drop(
    [
        'data_T_RangoEdad',
        'dummies_Tsexo_Mujer',
        'data_T_numero_hijos',
        'cluster',
        'data_NRO_ENT_PROM_U6M',
        'data_pobreza',
        'data_total',
        'data_sumCOD',
        'data_TIPCRE_UM'
    ],
    axis=1
)

df_variablesRelevantes.to_pickle("trabajoFinal/data/interim/df_manteniendo_VariablesRelevantes.pkl")