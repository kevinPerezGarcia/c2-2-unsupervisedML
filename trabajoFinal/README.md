![logo](https://github.com/kevinPerezGarcia/kevinPerezGarcia/blob/main/logo.png)

<h1>{{cookiecutter.project_name}}</h1>

Descripción del Proyecto de Ciencia de Datos

# 👥 Autor

[@Kevin Perez Garcia](https://www.linkedin.com/in/kevinperezgarcia)

# 📜 Licencia

Este proyecto está bajo la [MIT License](./Licencia).

# 🤝 Contribución

¡Las contribuciones, los problemas y las solicitudes de funciones son bienvenidos!

# 📞 Contacto

Para más consultas o colaboraciones, comuníquese a `econ.perez.garcia.k@gmail.com`.

# 📌 Tabla de contenido
- [👥 Autor](#-autor)
- [📜 Licencia](#-licencia)
- [🤝 Contribución](#-contribución)
- [📞 Contacto](#-contacto)
- [📌 Tabla de contenido](#-tabla-de-contenido)
- [Introducción](#introducción)
  - [Planteamiento del problema](#planteamiento-del-problema)
  - [Objetivos](#objetivos)
    - [Objetivo General](#objetivo-general)
    - [Objetivos Específicos](#objetivos-específicos)
  - [Importancia](#importancia)
  - [Actuales soluciones alternativas](#actuales-soluciones-alternativas)
  - [Problemas comparables](#problemas-comparables)
  - [Profesionales requeridos respecto a la problemática](#profesionales-requeridos-respecto-a-la-problemática)
- [📊 Datos](#-datos)
  - [Datos necesarios](#datos-necesarios)
  - [Fuente de los datos](#fuente-de-los-datos)
  - [Consideraciones legales](#consideraciones-legales)
  - [Descripción de la base de datos](#descripción-de-la-base-de-datos)
  - [Descripción de la unidad de análisis](#descripción-de-la-unidad-de-análisis)
  - [Sobre las variables](#sobre-las-variables)
    - [Diccionario de variables](#diccionario-de-variables)
      - [Diccionario de variables facilitado](#diccionario-de-variables-facilitado)
      - [Diccionario de variables después de la limpieza de datos](#diccionario-de-variables-después-de-la-limpieza-de-datos)
      - [Diccionario de variables después de la ingeniería de variables](#diccionario-de-variables-después-de-la-ingeniería-de-variables)
      - [Diccionario de variables usadas en el modelamiento](#diccionario-de-variables-usadas-en-el-modelamiento)
    - [Notas sobre las Variables](#notas-sobre-las-variables)
    - [Relaciones lógicas entre la variable objetivo y cada predictor](#relaciones-lógicas-entre-la-variable-objetivo-y-cada-predictor)
  - [Tamaño de la base de datos](#tamaño-de-la-base-de-datos)
  - [Supuestos](#supuestos)
- [🔍 Metodología](#-metodología)
  - [Enmarcación del problema en el contexto de machine learning](#enmarcación-del-problema-en-el-contexto-de-machine-learning)
  - [Medida de desempeño](#medida-de-desempeño)
- [📈 Resultados](#-resultados)
  - [Resultados del EDA](#resultados-del-eda)
    - [Resultados del Análisis de Perfil](#resultados-del-análisis-de-perfil)
- [📈 Conclusiones](#-conclusiones)
- [Trabajo Futuro](#trabajo-futuro)
- [Anexos](#anexos)
  - [Terminología](#terminología)
- [📚 Referencias](#-referencias)
- [🔄 Registro de cambios](#-registro-de-cambios)

_**Nota.**_ Antes de revisar este reporte, se recomienda leer, en la subsección [Terminología](#terminología) del Anexo, sobre los términos y conceptos que se utilizan a lo largo de este documento.

# Introducción

## Planteamiento del problema

El proyecto actual aborda el problema de [problema específico o dominio de interés]. En el mundo actual, [proporciona una breve descripción de la situación actual y por qué este problema es relevante]. Por ejemplo, en la industria X, el problema Y ha llevado a Z, lo que motiva la necesidad de un enfoque más eficiente/solución.

## Objetivos

### Objetivo General

El principal objetivo de este proyecto es [describe el objetivo específico, como "desarrollar un modelo de clasificación para predecir si un cliente comprará un producto basado en su historial de compras"].

### Objetivos Específicos

El principal objetivo de este proyecto es [describe el objetivo específico, como "desarrollar un modelo de clasificación para predecir si un cliente comprará un producto basado en su historial de compras"].

## Importancia

FYI

- ¿Cómo sería usada tu solución?
- ¿Cómo espera la empresa utilizar y beneficiarse de este modelo?

Esto permitirá [beneficios/resultados esperados, como "una mayor eficiencia en las campañas de marketing o una mejor experiencia del usuario"].

## Actuales soluciones alternativas

FYI

- ¿Cómo es la solución actual? Si las hay.
- Brindará ideas sobre cómo resolver el problema.
- Servirá como referencia de desempeño.

## Problemas comparables

FYI

- ¿Cuáles son los problemas comparables?
- ¿Puedes reutilizar la experiencia o herramientas?

## Profesionales requeridos respecto a la problemática

FYI

- ¿Hay experiencia humana disponible?
- ¿Cómo solucionarías el problema manualmente?

# 📊 Datos

## Datos necesarios

FYI

- Enumere los datos que necesita y cuánto necesita.

## Fuente de los datos

Los datos provienen de una competición introductoria de predicción denominada _Titanic - Machine Learning from Disaster_ (https://www.kaggle.com/competitions/titanic/overview).

## Consideraciones legales

FYI

- Consultar las obligaciones legales y obtener autorización si es necesario.
- Obtener autorizaciones de acceso.
- Asegúrese que la información confidencial se elimine o proteja (por ejemplo, anonimizada).

## Descripción de la base de datos

ENAHO está conformada por varios módulos. Para la presente investigación se hace uso de los siguientes 6 módulos:
- "Características de la Vivienda y el Hogar"
- "Características de los Miembros del Hogar"
- "Educación"
- "Salud"
- "Empleo e Ingresos"
- "Sumarias (Variables Calculadas)"

A partir de estos, se extraerán las variables necesarias para construir aquellas referidas a la investigación, detalladas en la siguiente sección.

La base de datos ha sido dividida en dos grupos:
- Base de datos de entrenamiento (_train.csv_)
- Base de datos de prueba (_test.csv_)

**Nota.** Para los objetivos propuestos, sólo usaremos la base de datos de entrenamiento.

## Descripción de la unidad de análisis

La unidad de análisis es un área o zona de $625~m^2$ dividida en 25 celdas de $5~m^2$ ($5~m$ x $5~m$) cada una, con la siguiente distribución:

| 1 	| 6  	| 11     	| 16 	| 21 	|
|---	|----	|--------	|----	|----	|
| 2 	| 7  	| 12     	| 17 	| 22 	|
| 3 	| 8  	| *13*    | 18 	| 23 	|
| 4 	| 9  	| 14     	| 19 	| 24 	|
| 5 	| 10 	| 15     	| 20 	| 25 	|


 Si el área presentó deslizamiento de tierra, la celda 13 es la ubicación de dicho deslizamiento y las otras celdas representan el resto del área. Si el área no presentó deslizamiento de tierra, ninguna celda es la ubicación de deslizamiento de tierra.

 Cada muestra u observación es independiente de las otras; es decir, no son áreas aledañas.

## Sobre las variables

### Diccionario de variables

#### Diccionario de variables facilitado

Se presenta 11 variables (1 identificador, 1 variable objetivo, 9 predictores)

| Variable | Etiqueta de la Variable | Tipo de Dato Adecuado | Etiquetas Actuales de Valores<br>o Unidad Actual de Medida | Etiquetas Correctas de Valores |
|---|---|---|---|---|
| id | Identificador de la zona | Cadena de caracteres |  |  |
| target | Deslizamiento de tierra | Categórico nominal binario | 1: sí, 0: no | Sí, No |
| elevacion | Elevación digital de la superficie del terreno | Numérico continuo | metro |  |
| tpgeologia | Litología del material superficial | Categórico nominal de siete categorías | 1: Rocas graníticas del Cretácico meteorizadas<br>2: Rocas graníticas del Jurásico meteorizadas<br>3: Toba y lava del Jurásivo meteorizadas<br>4: Toba y lava del Cretácico meteorizadas<br>5: Depósitos cuaternarios<br>6: Relleno<br>7: Arenisca del Jurásico meteorizada, lutita y arcilla | Rocas graníticas del Cretácico meteorizadas<br>Rocas graníticas del Jurásico meteorizadas<br>Toba y lava del Jurásivo meteorizadas<br>Toba y lava del Cretácico meteorizadas<br>Depósitos cuaternarios<br>Relleno<br>Arenisca del Jurásico meteorizada, lutita y arcilla |
| factorlp | Factor de longitud-pendiente que tiene en cuenta los efectos de la topografía en la erosión |  |  |  |
| curvplanta | Curvatura en planta, curvatura perpendicular a la dirección de la pendiente máxima |  |  |  |
| curvperfil | Crvatura de perfil, curvatura paralela a la pendiente, indicando la dirección de máxima inclinación |  |  |  |
| fiodp | Factor de intensificación orográfica de duración del paso: un índice para cuantificar la amplificación de la orografía en la precipitación |  |  |  |
| pendiente | Ángulo de inclinación de la pendiente en grados |  |  |  |
| iht | Índice de humedad topográfica, un índice para cuantificar el control topográfico sobre el proceso hidrológico |  |  |  |

![image.png](attachment:image.png)

#### Diccionario de variables después de la limpieza de datos

![image.png](attachment:image.png)

#### Diccionario de variables después de la ingeniería de variables

![image.png](attachment:image.png)

#### Diccionario de variables usadas en el modelamiento

![image.png](attachment:image.png)

### Notas sobre las Variables

**Respecto a la variables `conglome`, `vivienda`, `hogar`, `codperso`:**

Estas son variables que permiten identificar al hogar y el miembro del hogar.
  
**Respecto a la variable `pobreza`:**

Esta se refiere a la pobreza monetaria que toma el valor de 1 si el ingreso es menor al costo de una canasta básica de consumo de alimentos y no alimentos, que para el año 2022 asciende a S/ 415 mensual por habitante, es decir, para una familia de cuatro integrantes dicho monto asciende a S/ 1 660 mensual. Toma el valor de 0 en caso contrario.

**Respecto a la variable `casado`:**

Esta variable toma el valor de 1 si el miembro del hogar es conviviente o casado; mientras que toma el valor de 0 si el miembro del hogar es soltero, viudo o divorciado.

**Respecto a la variable `educacion`:**

Esta variable mide el grado de instrucción del miembro del hogar.

### Relaciones lógicas entre la variable objetivo y cada predictor

**`deslizamiento` vs `exposicion`**

Para comprender la relación entre el predictor "exposición" y la variable objetivo "target" en el contexto que proporcionas (si hubo deslizamiento o no), necesitamos considerar cómo los factores geológicos y topográficos, como la exposición de la pendiente, pueden influir en la estabilidad del terreno y por tanto en la probabilidad de un deslizamiento.

El predictor "exposición" en este caso representa la exposición de la pendiente en grados, lo cual puede interpretarse como la orientación de la pendiente respecto a los puntos cardinales. La exposición de la pendiente puede afectar varios aspectos que influyen en la estabilidad de la pendiente:

1. **Clima**: La dirección de la pendiente puede determinar la cantidad de insolación que recibe, lo que afecta a su vez la humedad del suelo y la vegetación. Por ejemplo, las pendientes que miran al sur en el hemisferio norte pueden estar más secas debido a una mayor exposición al sol, lo que podría influir en la cohesión del suelo.

2. **Erosión**: Dependiendo de la orientación, algunas pendientes pueden estar más protegidas o expuestas a factores erosivos como el viento y la lluvia. Una pendiente que enfrenta la dirección predominante de las tormentas puede ser más propensa a la erosión.

3. **Temperatura**: Las pendientes con cierta exposición pueden experimentar diferencias significativas en la temperatura, lo que puede afectar la congelación y el deshielo y, por tanto, la estabilidad del terreno.

4. **Vegetación**: La orientación de la pendiente influye en el tipo y la densidad de la vegetación, lo que a su vez afecta la retención de agua y la estabilidad del suelo.

En un análisis de datos para evaluar la relación entre "exposición" y la probabilidad de deslizamiento ("target"), podríamos esperar encontrar que ciertas orientaciones de la pendiente están asociadas con una mayor o menor frecuencia de deslizamientos. Esto podría ser debido a los factores mencionados anteriormente y probablemente a la interacción con otros factores como el tipo de suelo (tpgeologia), la pendiente del terreno, y los índices relacionados con la humedad (iht) y la erosión (factorlp).

Para establecer una relación cuantitativa, se realizaría un análisis estadístico, por ejemplo, usando modelos de regresión logística si "target" es una variable binaria (sí/no de deslizamiento). En este modelo, podríamos estimar cómo el cambio en el grado de exposición afecta la probabilidad logarítmica de que ocurra un deslizamiento, manteniendo constantes otros factores. Si encontramos que el coeficiente de "exposición" es estadísticamente significativo y positivo, esto indicaría que a medida que aumenta la exposición de la pendiente, también lo hace la probabilidad de un deslizamiento, todo lo demás constante. Si el coeficiente es negativo, indicaría que a mayor exposición, menor es la probabilidad de un deslizamiento.

## Tamaño de la base de datos

FYI

- Compruebe cuánto espacio ocupará.
- Cree un espacio de trabajo con suficiente espacio de almacenamiento.
- Comprobar el tamaño y tipo de datos (series temporales, muestrales, geográficos, etc.).

## Supuestos

FYI

- Enumere los supuestos que usted u otros han hecho hasta ahora.
- Verifiqe los supuestos si es posible.

# 🔍 Metodología

## Enmarcación del problema en el contexto de machine learning

FYI

- Supervisado, no supervisado, semisupervisada, autosupervisada, o de refuerzo
- ¿regresión, clasificación, o algo más?
- ¿Debería utilizar técnicas de aprendizaje por lotes o de aprendizaje en línea?
- ¿Qué algoritmos seleccionará?

## Medida de desempeño

FYI

- ¿Cómo se debe medir el desempeño?
- ¿La medida de desempeño está alineado con el objetivo comercial?
- ¿Cuál sería el desempeño mínimo necesario para alcanzar el objetivo del negocio?

# 📈 Resultados

Key findings, visualizations, and insights derived from the project.

## Resultados del EDA

### Resultados del Análisis de Perfil

- El 22.5% de los encuestados peruanos adultos se encuentran en una situación de pobreza monetaria.
- La mayor cantidad de pobres se ubican en la región Sierra, a diferencia de los no pobres que se ubican en la región Costa.
- Distribución bastante equilibrada respecto al área de residencia, la pobreza parece distribuirse de manera equitativa entre las áreas urbanas y rurales, ya que ambas tienen porcentajes similares de personas en situación de pobreza.
- Una proporción significativamente mayor de personas en situación de no pobreza reside en áreas urbanas. Esto podría indicar una concentración de recursos, servicios y oportunidades en las zonas urbanas que facilitan una mejor calidad de vida o condiciones económicas.
- Top 5 de departamentos con la mayor cantidad de personas pobres: Lima, Cajamarca, Loreto, Piura, Puno.
- Importante disparidad en el acceso al agua potable entre los pobres y no pobres: Un 70.53% de las personas que no están en situación de pobreza tienen acceso a agua potable, mientras que solo el 47.68% de las personas en situación de pobreza cuentan con dicho servicio.
- Predominancia del no acceso al agua potable entre los pobres: Un 52.32% de las personas en situación de pobreza no tienen acceso a agua potable, lo que refleja una importante carencia básica en este grupo.

# 📈 Conclusiones

Comment on your findings here and provide a summary. 

Include: 
1. The model you would choose to deploy (if any) 
2. A table of results of the different models you tested
3. Model performance across different subsets (ie, geographies, customer offering, etc.)
  * Should we not deploy for certain subsets/groups?
4. Steps on how to maintain and update the model in production in a way stakeholders can understand

# Trabajo Futuro

# Anexos

## Terminología

**Raleo de uva**: Práctica agrícola en el cultivo de la vid. Consiste en la eliminación selectiva de ciertas bayas o racimos de uva en la planta, con el objetivo de mejorar la calidad y la cantidad de la cosecha final. Esta técnica se realiza durante el crecimiento de la uva, generalmente en las primeras etapas de desarrollo de la fruta.

El propósito principal del raleo es reducir la carga de la planta, es decir, el número de racimos o la cantidad de uvas que la vid debe madurar. Esto permite que los racimos restantes reciban más nutrientes, agua y luz solar, lo que a su vez promueve un desarrollo más completo y una mejor calidad de la fruta. Al eliminar ciertos racimos o bayas, se logra una distribución más uniforme de los recursos disponibles para la planta, lo que resulta en uvas más grandes, sabrosas y con mejor concentración de azúcares y otros compuestos importantes para la calidad del vino.

El raleo de uva se realiza de manera manual o mecánica, dependiendo de la escala de producción y la disponibilidad de recursos. En muchos viñedos de alta calidad, el raleo manual es preferido, ya que permite una selección más precisa y delicada de las uvas a eliminar, asegurando que solo se retiren aquellas que afecten negativamente la calidad final del producto. Sin embargo, en grandes viñedos comerciales, el raleo mecánico puede ser más práctico y rentable, aunque puede ser menos preciso.

**Operario de raleo de uva**: Un operario de raleo de uva es un trabajador agrícola especializado en llevar a cabo la práctica de raleo de uva en los viñedos. Su función principal es realizar la selección y eliminación de racimos o bayas de uva de manera manual, siguiendo las instrucciones específicas del viticultor o encargado del viñedo.

Los operarios de raleo de uva son responsables de identificar y eliminar los racimos o bayas que no tienen el tamaño, la madurez o la calidad adecuada para contribuir a una cosecha de alta calidad. Esto puede implicar retirar racimos excesivamente pequeños, dañados por enfermedades o plagas, inmaduros o sobreexpuestos al sol, así como ajustar la carga de la planta para mejorar la distribución de los recursos disponibles.

Estos trabajadores deben tener habilidades y experiencia en el manejo delicado de las uvas, así como un buen ojo para detectar las características deseables o no deseables en la fruta. Además, es importante que sigan las indicaciones del viticultor o supervisor para garantizar que el raleo se realice de acuerdo con los estándares de calidad y las necesidades específicas de la viña.

En muchos casos, el trabajo de raleo de uva se realiza a mano, lo que requiere paciencia, precisión y resistencia física por parte del operario. Este trabajo es fundamental para asegurar una cosecha de uva de alta calidad, ya que el raleo adecuado contribuye a la salud de las plantas, la uniformidad de la maduración y la concentración de sabores en las uvas restantes, lo que finalmente se refleja en la calidad del vino producido. 

# 📚 Referencias

- Nombre del autor, **Título del artículo o recurso**, enlace o DOI.

# 🔄 Registro de cambios

- **[Fecha]**: Lanzamiento inicial.
- **[Fecha]**: Nueva característica X añadida.