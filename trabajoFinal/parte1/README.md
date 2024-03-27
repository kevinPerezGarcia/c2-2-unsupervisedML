![logo](https://github.com/kevinPerezGarcia/kevinPerezGarcia/blob/main/logo.png)

<h1>SEGMENTACIÓN DE OPERARIOS DE RALEO DE UVA - REGIONES PIURA E ICA</h1>

Descripción del Proyecto de Ciencia de Datos

# 👥 Autor

[@Kevin Perez Garcia](https://www.linkedin.com/in/kevinperezgarcia)

🤝 ¡Las observaciones, las recomendaciones y las contribuciones son bienvenidas!

📞 Para más consultas o colaboraciones, comuníquese a `econ.perez.garcia.k@gmail.com`.

# 🏢 Cliente

**Nota.** Para mantener en el anonimato y también no brindar información sobre el cliente del proyecto, denominaremos a la empresa cliente como *Exportadora de Uvas del Valle* y la información brindada sobre esta es referida a su actividad pero ficticia. 

### Nombre de la Empresa: Exportadora de Uvas del Valle

### Descripción:
Exportadora de Uvas del Valle es una empresa líder en la producción y exportación de uvas de mesa de alta calidad. Con más de dos décadas de experiencia en el sector, la empresa se ha destacado por su compromiso con la excelencia en el cultivo, empaque y distribución de uvas frescas a nivel nacional e internacional.

### Misión:
Nuestra misión es proporcionar a nuestros clientes productos de la más alta calidad, cultivados de manera sostenible y con prácticas agrícolas responsables. Nos esforzamos por mantener relaciones sólidas y a largo plazo con nuestros clientes y socios comerciales, ofreciendo un servicio excepcional y un producto que supere sus expectativas.

### Visión:
Ser reconocidos como el proveedor líder de uvas de mesa premium en el mercado internacional, manteniendo altos estándares de calidad, innovación y sostenibilidad en todas nuestras operaciones.

---
_**Nota.**_ Antes de leer este reporte, se recomienda revisar la sección [Anexos](#anexos). En esta sección encontrará información que le permitirá familiarizarse con el "negocio".

---

# 📌 Tabla de contenido
- [👥 Autor](#-autor)
- [🏢 Cliente](#-cliente)
    - [Nombre de la Empresa: Exportadora de Uvas del Valle](#nombre-de-la-empresa-exportadora-de-uvas-del-valle)
    - [Descripción:](#descripción)
    - [Misión:](#misión)
    - [Visión:](#visión)
- [📌 Tabla de contenido](#-tabla-de-contenido)
- [Introducción](#introducción)
  - [Planteamiento del Problema](#planteamiento-del-problema)
  - [Objetivos](#objetivos)
  - [Importancia](#importancia)
  - [Actuales Soluciones](#actuales-soluciones)
  - [Profesionales Requeridos Respecto a la Problemática](#profesionales-requeridos-respecto-a-la-problemática)
- [📊 Datos](#-datos)
  - [Datos necesarios](#datos-necesarios)
    - [Datos Cuantitativos](#datos-cuantitativos)
    - [Datos Cualitativos](#datos-cualitativos)
  - [Fuente de los datos](#fuente-de-los-datos)
  - [Organización de la base de datos](#organización-de-la-base-de-datos)
  - [Diccionario de variables facilitado](#diccionario-de-variables-facilitado)
  - [Descripción de los datos](#descripción-de-los-datos)
  - [Descripción de la unidad de análisis](#descripción-de-la-unidad-de-análisis)
- [🔍 Metodología](#-metodología)
- [📈 Resultados](#-resultados)
- [📈 Conclusiones](#-conclusiones)
- [Trabajo Futuro](#trabajo-futuro)
- [Anexos](#anexos)
  - [Planta de vid](#planta-de-vid)
  - [Ciclo de cultivo de la vid](#ciclo-de-cultivo-de-la-vid)
  - [Terminología](#terminología)

# Introducción

## Planteamiento del Problema
La empresa "Exportadora de Uvas del Valle" enfrenta desafíos en la optimización de sus operaciones de cultivo y cosecha de uva, específicamente durante el proceso de raleo, que es crucial para garantizar la calidad del fruto. A pesar de contar con un equipo diverso de operarios, existe una variabilidad significativa en la eficiencia y efectividad de su trabajo. Esta variabilidad afecta directamente la productividad general y la calidad de las uvas cosechadas. Sin un entendimiento claro de los diferentes tipos de operarios, la empresa no puede implementar estrategias efectivas de gestión del personal ni optimizar sus procesos.

## Objetivos

- **Principal:** Identificar y categorizar los diferentes tipos de operarios de raleo en la empresa según sus habilidades, rendimiento y otros factores relevantes.

## Importancia
Comprender los distintos perfiles de operarios y su impacto en el proceso de raleo permitirá a "Frutas Estelares S.A." optimizar la asignación de tareas, mejorar la productividad y asegurar un estándar de calidad uniforme en la cosecha. Esto no solo mejorará la eficiencia operativa sino que también reforzará la competitividad de la empresa en el mercado global de uvas de mesa.

## Actuales Soluciones
Actualmente, la gestión de operarios se realiza principalmente a través de evaluaciones cualitativas y la experiencia de los supervisores. Aunque este enfoque ha sido parcialmente efectivo, carece de la precisión y objetividad que los métodos analíticos basados en datos pueden proporcionar.

## Profesionales Requeridos Respecto a la Problemática
Para abordar este desafío, se requieren profesionales con experiencia en:
* Científicos de datos, para diseñar y ejecutar el análisis de segmentación de operarios.
* Especialistas en recursos humanos, para interpretar los resultados del análisis y desarrollar estrategias de gestión del personal.
* Ingenieros agrónomos, para aportar conocimientos especializados sobre el proceso de raleo y sus requisitos.
* Gerentes de operaciones, para implementar cambios en los procesos y supervisar la ejecución de nuevas estrategias.

# 📊 Datos

## Datos necesarios

Para llevar a cabo una segmentación efectiva de operarios de raleo, es fundamental recopilar y analizar datos que no solo capturen el rendimiento cuantitativo de los trabajadores, sino también factores cualitativos que puedan influir en su productividad y calidad de trabajo.

### Datos Cuantitativos
1. **Rendimiento de Raleo (kg/hora):** Medición directa de la cantidad de uva raleada por hora por cada operario. Este es el indicador más directo de productividad.
2. **Calidad del Raleo:** Evaluación basada en los estándares de calidad de la uva post-raleo, posiblemente cuantificada a través de mediciones específicas o índices de calidad.
3. **Asistencia:** Días trabajados, ausencias (justificadas e injustificadas), y puntualidad. Estos indicadores pueden revelar la fiabilidad y el compromiso del operario.
4. **Eficiencia en el uso de recursos:** Evaluación de cómo el operario utiliza los recursos disponibles (por ejemplo, herramientas de raleo) para maximizar la productividad minimizando el desperdicio.

### Datos Cualitativos
1. **Experiencia y Capacitación:** Antecedentes de trabajo del operario, años de experiencia en raleo, y formación recibida. La experiencia y la capacitación pueden influir significativamente en la eficiencia y la calidad del trabajo.
2. **Condiciones de Trabajo:** Consideraciones sobre el ambiente de trabajo, como el clima, el tipo de terreno, y otras condiciones que podrían afectar el rendimiento.
3. **Feedback de Supervisores:** Opiniones y evaluaciones cualitativas de los supervisores sobre el desempeño, actitud, y habilidades del operario.
4. **Satisfacción Laboral y Motivación:** Información sobre el nivel de satisfacción y motivación de los operarios, que puede afectar directamente su rendimiento y calidad de trabajo.

## Fuente de los datos

Los [datos](/trabajoFinal/data/raw/) son proporcionados por la empresa.

## Organización de la base de datos

La base de datos:
- Está capturada en un solo archivo [data-parte1.csv](/trabajoFinal/data/raw/data-parte1.csv).
- Contiene 22907 registros y 49 variables.

## Diccionario de variables facilitado

| Variable original                   | Variable renombrada          | Etiqueta de la variable                                                                                                   |
|-------------------------------------|------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| data_Persona                        | id_operario                  | Identificador del operario                                                                                                |
| data_Tcamp                          | campania                     | Campaña de cultivo                                                                                                        |
| sede_cod                            | region                       | Región de cultivo                                                                                                         |
| data_productividad_per              | rendimiento                  | Número de jabas recogidas en campo en toda la campaña/horas laboradas en   toda la campaña                                |
| data_veces                          | campania_numero              | Número de campañas en las que ha participado                                                                              |
| data_n_fundo                        | fundo                        | Número de fundos trabajados (cada fundo contiene varios lotes)                                                            |
| data_n_lote                         | lote                         | Número de lote (hectarea de tierra delimitada) trabajado                                                                  |
| data_dias_empresa                   | trabajo_dias                 | Días trabajados en la empresa durante la campaña y en la labor especifica                                                 |
| data_sumHRSLB                       | trabajo_horas                | Total de horas laboradas en la campaña                                                                                    |
| data_sum_hora_extra                 | trabajo_horas_extra          | Suma de horas extra en la campaña                                                                                         |
| data_asistente_dias_empresa         | trabajo_dias_asistente       | Número de días trabajados por el operario al mando de un asistente   (existe la posibilidad que no haya tenido asistente) |
| data_sum_aux_bono_total             | bono_auxiliar                | Bono auxiliar, en soles, por su productividad                                                                             |
| data_bono_produc                    | bono                         | Bono, en soles, por productividad                                                                                         |
| data_otros_bono                     | bono_otros                   | Otros bonos                                                                                                               |
| data_GRADO2                         | estudio                      | Nivel de  estudios del operario                                                                                           |
| data_Testado_civil                  | estado_civil                 | Estado civil del operario                                                                                                 |
| data_Tsexo                          | sexo                         | Sexo del operario                                                                                                         |
| data_Tedad                          | edad                         | Edad del operario                                                                                                         |
| data_numero_hijos                   | hijos                        | Número de hijos dependientes                                                                                              |
| data_n_variedad                     | variedades_uva               | Cantidad de variedades de uva trabajadas durante la campaña                                                               |
| data_DEUDA_PROM_U6M                 | deuda                        | Deuda promedio en el sistema financiero en los seis últimos meses                                                         |
| data_PEOR_CALIF_U6M                 | calificacion_financiera      | Peor Calificación en el sistema financiero en los seis últimos meses                                                      |
| data_MODA_CALIF_U6M                 | calificacion_financiera_moda | Moda de la peor calificación sistema financiero en los seis últimos meses                                                 |
| data_DIAS_ATRASO_PROM_U6M           | dias_atraso_deudas           | Promedio de días de atraso en el sistema financieron en los seis últimos   meses                                          |
| data_BANCARIZADO                    | bancarizado                  | Bancarizado o no                                                                                                          |
| data_distancia                      | distancia_hogar_fundo        | Distancia del hogar al fundo                                                                                              |
| data_import_unico                   | ingresos                     | Ingresos totales obtenidos en la campaña                                                                                  |
| data_numero_asistentes              | asistentes                   | Número de asistentes con los que ha trabajado                                                                             |
| data_asistente_mediana_Tedad        | edad_mediana                 | Mediana de la edad de los asistentes con los que ha trabajado el operario                                                 |
| data_asistente_mediana_numero_hijos | hijos_mediana                | Mediana del número de hijos de los asistentes con el que ha trabajado el   operario                                       |
| data_sum_variedad_total_AL          | jabas_al                     | Total de jabas recogidas de la variedad ALLISON                                                                           |
| data_sum_variedad_total_CC          | jabas_cc                     | Total de jabas recogidas de la variedad COTTON CANDY                                                                      |
| data_sum_variedad_total_CP          | jabas_cp                     | Total de jabas recogidas de la variedad CRIMSON SEEDLESS (ficticio)                                                       |
| data_sum_variedad_total_JS          | jabas_js                     | Total de jabas recogidas de la variedad JACK'S SALUTE                                                                     |
| data_sum_variedad_total_MG          | jabas_mg                     | Total de jabas recogidas de la variedad MAGENTA                                                                           |
| data_sum_variedad_total_RG          | jabas_rg                     | Total de jabas recogidas de la variedad RED GLOBE                                                                         |
| data_sum_variedad_total_SG          | jabas_sg                     | Total de jabas recogidas de la variedad SUGRAONE                                                                          |
| data_sum_variedad_total_TC          | jabas_tc                     | Total de jabas recogidas de la variedad THOMPSON SEEDLESS (ficticio)                                                      |
| data_sum_variedad_total_TM          | jabas_tm                     | Total de jabas recogidas de la variedad TIMPSON                                                                           |
| data_sum_variedad_total_VN          | jabas_vn                     | Total de jabas recogidas de la variedad VIOGNIER (ficticio)                                                               |
| data_T_RangoEdad                    | rango_edad                   | Rango de edad                                                                                                             |
| dummies_Tsexo_Mujer                 | mujer                        | Dummy mujer de la variable "sexo"                                                                                         |
| data_T_numero_hijos                 | hijo                         | Dummy hijo de la variable "hijos"                                                                                         |
| cluster                             | cluster                      | Resultado de la segmentación                                                                                              |
| data_NRO_ENT_PROM_U6M               |                              |                                                                                                                           |
| data_pobreza                        |                              |                                                                                                                           |
| data_total                          |                              |                                                                                                                           |
| data_sumCOD                         |                              |                                                                                                                           |
| data_TIPCRE_UM                      |                              |                                                                                                                           |

*Nota.* La base de datos original contiene las variables con sus nombres originales. El renombramiento se realiza en el preprocesamiento para una mayor legibilidad del código.

## Descripción de los datos

La base de datos presenta 49 variables:
- 1 variable de identificación: `id_operario`
- 1 variable temporal: `campania`
- 1 variable espacial: `region`
- 37 variables explicativas
- 3 variables derivadas (i.e. creadas a partir de otras): `rango_edad`, `mujer`, `hijo`
- 1 variable resultante (i.e. como resultado de algún algoritmo): `cluster`
- 5 variables sin descripción: `data_NRO_ENT_PROM_U6M`, `data_pobreza`, `data_total`, `data_sumCOD`, `data_TIPCRE_UM`

En la importación de la base de datos no se considerarán las variables:
- derivadas, porque se obtendrán según beneficien o no al algoritmo;
- resultante, porque es proceso de un algoritmo de segmentación previo;
- sin descripción, porque se desconocen su significado.

Así, sólo se cuenta con 40 variables a procesar.

## Descripción de la unidad de análisis



# 🔍 Metodología

# 📈 Resultados

# 📈 Conclusiones

# Trabajo Futuro

# Anexos

## Planta de vid

![Planta de uva](/trabajoFinal/img/plantaUva.jpg)

## Ciclo de cultivo de la vid

| Etapa                  | Fecha y Periodo                          | En qué consiste                                                                                                                                                                                 |
|------------------------|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Preparación del suelo  | Otoño/Principios de invierno             | Labranza y enmiendas para preparar el suelo antes de la temporada de lluvias.                                                                                                                   |
| Plantación             | Primavera                                | Colocación de las vides después de que hayan pasado las heladas y el suelo se haya calentado.                                                                                                   |
| Crecimiento vegetativo | Primavera - Verano                       | Rápido crecimiento de hojas, tallos y zarcillos, proporcionando la estructura básica para el desarrollo de la fruta.                                                                            |
| Floración y cuajado    | Mediados de primavera                    | Transformación de las flores en pequeños racimos de uvas, esencial para la producción de fruta.                                                                                                 |
| Desarrollo de la fruta | Primavera - Verano - Principios de otoño | Desarrollo y maduración de las uvas, aumentando de tamaño y contenido de azúcar.                                                                                                                |
| **Raleo de uva**       | **Verano**                               | **Eliminación selectiva de algunas uvas inmaduras de los racimos para mejorar la calidad y el tamaño de las uvas restantes, permitiendo que estas últimas reciban más nutrientes y luz solar.** |
| Veraison               | Finales de verano - Principios de otoño  | Cambio de color de las uvas y comienzo de la maduración final.                                                                                                                                  |
| Maduración y cosecha   | Otoño                                    | Maduración final de las uvas y cosecha, que varía según la variedad y el clima local.                                                                                                           |
| Post-cosecha           | Otoño - Invierno                         | Actividades como poda, riego y fertilización para preparar las vides para el próximo ciclo de crecimiento.                                                                                      |

## Terminología

**Vid**:<br>
La vid, conocida científicamente como Vitis vinifera, es una planta trepadora de la familia de las Vitaceae. Es la especie de vid más comúnmente cultivada para la producción de uvas destinadas a la elaboración de vino, así como para consumo directo de uvas de mesa, jugos, pasas y otros productos derivados.

Características de la vid:

1. **Trepadora**: La vid es una planta trepadora que se enrosca alrededor de soportes, como pérgolas, alambradas o enrejados, para crecer verticalmente.

2. **Hojas palmadas**: Las hojas de la vid son grandes y palmadas, con lóbulos distintivos y bordes dentados.

3. **Frutos en racimos**: Las uvas, los frutos de la vid, crecen en racimos colgantes que pueden variar en tamaño, forma y color según la variedad.

4. **Ciclo de vida perenne**: La vid es una planta perenne, lo que significa que puede vivir y producir frutos durante varios años si se cuida adecuadamente.

5. **Variedades diversas**: Existen numerosas variedades de vid, cada una con sus propias características de sabor, color, tamaño de fruto y adaptación al clima y al suelo.

6. **Importancia económica y cultural**: La vid tiene una gran importancia económica y cultural en muchas regiones del mundo debido a la producción de uvas para la elaboración de vino, así como por su consumo directo y sus múltiples usos en la gastronomía y la agricultura.

La vid es una planta muy adaptable que puede crecer en una amplia gama de climas y suelos, aunque prefiere climas cálidos y soleados con suelos bien drenados. Su cultivo requiere cuidados específicos, incluyendo poda, riego, control de plagas y enfermedades, y cosecha en el momento adecuado para garantizar la calidad de los frutos.

**Uva**:<br>
La uva es el fruto de la vid, una planta trepadora de la familia de las Vitaceae. Es una fruta ampliamente cultivada y consumida en todo el mundo, tanto fresca como procesada en productos como vinos, jugos, pasas y mermeladas.

Las uvas varían en color, tamaño, sabor y textura dependiendo de la variedad de vid de la que provienen. Pueden ser verdes (uvas blancas), rojas (uvas tintas) o moradas, y su sabor puede ser dulce, ácido o una combinación de ambos. Algunas variedades de uva tienen semillas, mientras que otras son sin semillas.

La uva es una fruta rica en nutrientes, incluyendo vitaminas (como la vitamina C y algunas del complejo B), minerales (como potasio y manganeso), antioxidantes y fibra dietética. Se considera una opción saludable como parte de una dieta equilibrada.

Además de su valor nutricional, las uvas también tienen un importante papel cultural y económico. La viticultura, que es el cultivo de la vid, es una industria significativa en muchas regiones del mundo, especialmente en áreas con climas adecuados para su crecimiento. Los vinos elaborados a partir de uvas son apreciados por su diversidad de sabores y características únicas, y tienen un lugar destacado en la gastronomía y la cultura de muchas sociedades.

**Raleo de uva**:<br> Práctica agrícola en el cultivo de la vid. Consiste en la eliminación selectiva de ciertas bayas o racimos de uva en la planta, con el objetivo de mejorar la calidad y la cantidad de la cosecha final. Esta técnica se realiza durante el crecimiento de la uva, generalmente en las primeras etapas de desarrollo de la fruta.

El propósito principal del raleo es reducir la carga de la planta, es decir, el número de racimos o la cantidad de uvas que la vid debe madurar. Esto permite que los racimos restantes reciban más nutrientes, agua y luz solar, lo que a su vez promueve un desarrollo más completo y una mejor calidad de la fruta. Al eliminar ciertos racimos o bayas, se logra una distribución más uniforme de los recursos disponibles para la planta, lo que resulta en uvas más grandes, sabrosas y con mejor concentración de azúcares y otros compuestos importantes para la calidad del vino.

El raleo de uva se realiza de manera manual o mecánica, dependiendo de la escala de producción y la disponibilidad de recursos. En muchos viñedos de alta calidad, el raleo manual es preferido, ya que permite una selección más precisa y delicada de las uvas a eliminar, asegurando que solo se retiren aquellas que afecten negativamente la calidad final del producto. Sin embargo, en grandes viñedos comerciales, el raleo mecánico puede ser más práctico y rentable, aunque puede ser menos preciso.

**Operario de raleo de uva**:<br> Un operario de raleo de uva es un trabajador agrícola especializado en llevar a cabo la práctica de raleo de uva en los viñedos. Su función principal es realizar la selección y eliminación de racimos o bayas de uva de manera manual, siguiendo las instrucciones específicas del viticultor o encargado del viñedo.

Los operarios de raleo de uva son responsables de identificar y eliminar los racimos o bayas que no tienen el tamaño, la madurez o la calidad adecuada para contribuir a una cosecha de alta calidad. Esto puede implicar retirar racimos excesivamente pequeños, dañados por enfermedades o plagas, inmaduros o sobreexpuestos al sol, así como ajustar la carga de la planta para mejorar la distribución de los recursos disponibles.

Estos trabajadores deben tener habilidades y experiencia en el manejo delicado de las uvas, así como un buen ojo para detectar las características deseables o no deseables en la fruta. Además, es importante que sigan las indicaciones del viticultor o supervisor para garantizar que el raleo se realice de acuerdo con los estándares de calidad y las necesidades específicas de la viña.

En muchos casos, el trabajo de raleo de uva se realiza a mano, lo que requiere paciencia, precisión y resistencia física por parte del operario. Este trabajo es fundamental para asegurar una cosecha de uva de alta calidad, ya que el raleo adecuado contribuye a la salud de las plantas, la uniformidad de la maduración y la concentración de sabores en las uvas restantes, lo que finalmente se refleja en la calidad del vino producido. 