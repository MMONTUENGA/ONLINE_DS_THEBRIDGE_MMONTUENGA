# EDA: Infrografía del viajero

## Descripción.


En los últimos años, el sector del alquiler vacacional en España ha experimentado una evolución notablemente positiva, marcada por un crecimiento sostenido y una diversificación en su oferta. Esta transformación no solo refleja un cambio en las preferencias de los consumidores, sino que también evidencia la adaptabilidad y la innovación dentro del sector turístico.

Ante la gran variedad y cantidad de datos que se generan en este tipo de negocio, realizar un análisis en profundidad es fundamental. Comprender patrones y tendencias de comportamiento no solo es esencial para conocer el mercado actual, sino que permite la creación de acciones comerciales más efectivas y adaptadas a os diferentes tipos de viajeros.

En el presente EDA (Análisis Exploratorio de Datos), se estudia el caso particular de FeelFree, una empresa con varios años de trayectoria, especializada en la gestión de apartamentos en dos regiones clave de España: San Sebastián y Baqueira.



## Objetivos

1.	Encontrar segmentos clave alto impacto en los ingresos.
La metodología incluirá un análisis detallado de los datos de reservas, segmentando por variables como origen, género, temporada, y otras características de los huéspedes. 

2.	Encontrar segmentos clave por crecimiento interanual
Aquí, el enfoque estará en identificar aquellos segmentos que han mostrado un crecimiento interanual sustancial. S

3.	Detectar fortalezas en el posicionamiento del canal de venta propio
Este objetivo implica analizar el rendimiento del canal de ventas propio de la empresa (la web) comparado con otros canales (como agencias de viajes online o plataformas de reservas). El análisis se enfocará en identificar segmentos de mercado o países donde el canal propio tiene una ventaja competitiva en términos de reservas. 

4.	Mejorar el conocimiento demográfico y geográfico de los viajeros
El último objetivo busca establecer una segmentación clara tanto geográfica como demográfica para afinar acciones de comunicación y marketing.
  
## Herramientas y Recursos Utilizados

* Python: lenguaje de programación base para todo el desarrollo del EDA.
* Pandas: fundamental para el manejo de datos. Utilizo esta biblioteca para cargar, manipular y analizar los datos en formato DataFrame. Es especialmente útil para la limpieza de datos, como la eliminación de duplicados, el manejo de valores nulos, y la transformación de formatos de datos. Funciones como read_excel, drop_duplicates, y fillna son algunas de las que empleo para estas tareas.
* NumPy: NumPy es una biblioteca que me permite realizar operaciones matemáticas y estadísticas avanzadas. La utilizo para manipulaciones numéricas como cálculos estadísticos, operaciones con matrices y generación de números aleatorios. Funciones como mean, median, y std de NumPy me ayudan en el análisis estadístico de los datos.
* Matplotlib y Seaborn: para la visualización de datos. Estas bibliotecas me permiten crear gráficos y diagramas que facilitan la interpretación y presentación de los datos. Utilizo Matplotlib para personalizar gráficos detalladamente y Seaborn para generar visualizaciones más complejas de manera sencilla, como histogramas, diagramas de caja, y mapas de calor.
* Funciones Personalizadas: además de estas bibliotecas, utilizo funciones personalizadas. Estas funciones me permiten automatizar tareas repetitivas y específicas de mi proyecto, como transformaciones de datos particulares o cálculos estadísticos específicos.
* Datetime: manejar datos de fecha y hora, empleo la biblioteca datetime. Es útil para convertir y manipular columnas de fecha y hora, lo que es crucial en muchos conjuntos de datos, especialmente para identificar tendencias a lo largo del tiempo.
* Gender Guesser: biblioteca de Python que se utiliza para predecir el género de una persona basado en su primer nombre. Esta herramienta se basa en un conjunto de reglas y datos que asocian nombres específicos con un género particular.


## Resultado

El análisis realizado revela varios datos interesantes con respecto al impacto de diferentes nacionalidades en el revenue, destacándose Estados Unidos como la nacionalidad con mayor impacto. Esto se debe principalmente a que los viajeros estadounidenses presentan un ADR (Revenue por Habitación Disponible) superior al de otras nacionalidades. Además, se ha observado que los estadounidenses tienden a tener una estancia media más prolongada en comparación con viajeros de otras nacionalidades.

Otro aspecto destacado del análisis es el crecimiento observado en el segmento de familias. Este aumento se hace evidente al comparar las reservas de este grupo en 2019 con las de 2023. Este dato es particularmente relevante para destinos vacacionales como Sebastián.

En resumen, los datos analizados indican un crecimiento significativo en dos frentes principales: por un lado, el grupo de viajeros de origen norteamericano muestra un aumento en la ciudad, y por otro, se observa un crecimiento en el segmento de familias en ambos destinos analizados.

## Contribuidores
Este proyecto ha sido elaborado por:

  <li>Miguel Montuenga Díaz