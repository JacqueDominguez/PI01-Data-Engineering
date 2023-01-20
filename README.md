# PI01-Data-Engineering. 

Bienvenido! Si llegaste hasta acá probablemente buscás alguna forma fácil y gratuita de realizar una Application Programming Interface (API) y realizar su deployment para que cualquier persona pueda acceder a la consulta desde cualquier parte del mundo. 

</div>

## Pero..¿Que es una API?

Application Programming Interface es una interfaz que permite que dos aplicaciones se comuniquen entre sí, independientemente de la infraestructura subyacente. Son herramientas muy versátiles y fundamentales para la creación de, por ejemplo, pipelines, ya que permiten mover y brindar acceso simple a los datos que se quieran disponibilizar a través de los diferentes endpoints, o puntos de salida de la API.
Para este proyecto utilicé FastAPI, un web framework moderno y de alto rendimiento para construir APIs de manera muy sencilla con Python.

</div>

## Objectivos del proyecto

+ Realizar la ingesta de datos desde diversos datasets.
+ Efectuar el  **Análisis exploratorio de datos** (EDA) a los datasets.
+ Hacer  las **transformaciones** necesarias y unificar el dataset.
+ Realizar  las **consultas** al dataset.
+ Llevar a cabo el **desarrollo de la API** a través de FastApi.
+ Ejecutar el **deployment** de la API en Deta.

</div>

## Fuente de los datos
Para realizar este trabajo se utlizaron los archivos ubicados en la carpeta Datasets que corresponden a informacion sobre series y peliculas de las plataformas de Amazon, Disney, Hulu y Netflix.
<div>
<img src="https://i0.wp.com/codigoespagueti.com/wp-content/uploads/2020/07/Amazon-Prime-Video-Perfiles-Netflix-1.jpg?resize=1200%2C720&quality=80&ssl=1" width="200px">
<img src="https://tec.com.pe/wp-content/uploads/2021/11/logo-de-disney-plus-scaled-1.jpeg" width="200px">
<img src="https://www.streamingdigitally.com/wp-content/uploads/2022/12/hulu-featured-1-jpg-1200x720.webp" width="200px">
<img src="https://i0.wp.com/frikispan.com/wp-content/uploads/2014/12/netflix-logo.png?resize=1200%2C720" width="200px">

</div>

## Pasos a seguir:

### 1- Extraccion y transformación:

Para ello utilicé Python , más especificamente las librerias pandas y numpy (podras encontrar todo el código dentro del notebook llamado **Transformaciones**) y por último convertí el dataframe en el archivo [data.csv](/data.csv) para utilizar en la elaboración de la API.

### 2- Desarrollo de la API:

Para ello utilicé un entorno virtual donde se instaló FastAPI, Pandas y Uvicorn. Luego desarrollé la API con FastApi (podras encontrar todo el código dentro del archivo [main.py](/main.py), en donde en pocas lineas se realiza la configuración , se extra el dataset desde una url (para lograr disponibilizar los datos en la etapa del deploy) y se crean cinco funciones para las consultas: 

+ get_word_count: cantidad de veces que aparece una palabra en el título de peliculas o series, por plataforma.
+ get_score_count: cantidad de películas por plataforma con un puntaje mayor a 'xx' en determinado año.
+ get_second_score: la segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.
+ get_longest: película o serie que más duró según año, plataforma y tipo de duración.
+ get_rating_count: cantidad de series y películas por tipo de rating.

Durante la etapa de desarrollo revisé el funcionamiento integral de la API y sus consultas de manera local desde la terminal con el comando ***uvicorn main:app --reload***  en el localhost http://127.0.0.1:8000/ . Una vez logrado el adecuado funcionamiento de API de manera local realice en archivo de requerimientos con el comando  ***pip freeze > requirements.txt***

### 3- Deployment:
Q sé yo



## Tecnologías Utilizadas
* [Pandas](https://pandas.pydata.org/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Uvicorn](https://www.uvicorn.org/)
* [Deta](https://www.deta.sh/)

## Video en YouTube
Acá el video en YouTube explicando mi proyecto prevemente: (Haga click en la imagen)

[<img src=https://www.cinco8.com/wp-content/uploads/2020/08/404.png width = "200px">]()
