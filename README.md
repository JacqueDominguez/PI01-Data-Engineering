# Cómo realizar tu primer API con FastAPI y Deta. 

Bienvenido! Si llegaste hasta acá probablemente buscás alguna forma fácil y gratuita de realizar una Application Programming Interface (API) y realizar su deployment para que cualquier persona pueda acceder a las consultas desde cualquier parte del mundo. 
<div>
<img src="https://amalgjose.files.wordpress.com/2021/02/fast_api_ppt.png?w=816&h=9999?resize=1500%2C720&quality=80&ssl=1" width="305px">
<img src="https://res.cloudinary.com/practicaldev/image/fetch/s--HhcPKSOJ--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/zkp5uldyd7wo1k7w8f3r.png?resize=1500%2C720&quality=80&ssl=1" width="380px">


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

## Fuente de datos

Para realizar este trabajo se utlizaron los archivos ubicados en la carpeta Datasets que corresponden a informacion sobre series y peliculas de las plataformas de Amazon, Disney, Hulu y Netflix.
<div>
<img src="https://i0.wp.com/codigoespagueti.com/wp-content/uploads/2020/07/Amazon-Prime-Video-Perfiles-Netflix-1.jpg?resize=1200%2C720&quality=80&ssl=1" width="200px">
<img src="https://tec.com.pe/wp-content/uploads/2021/11/logo-de-disney-plus-scaled-1.jpeg" width="200px">
<img src="https://www.streamingdigitally.com/wp-content/uploads/2022/12/hulu-featured-1-jpg-1200x720.webp" width="200px">
<img src="https://i0.wp.com/frikispan.com/wp-content/uploads/2014/12/netflix-logo.png?resize=1200%2C720" width="200px">

</div>

## Pasos a seguir:

### 1- Extraccion y transformación:

Para ello utilicé Python , más especificamente las librerias pandas y numpy (podras encontrar todo el código dentro del notebook [transformaciones.ipynb](/transformaciones.ipynb)) y por último convertí el dataframe en el archivo [data.csv](/Datasets/data.csv) para utilizar en la elaboración de la API.

### 2- Desarrollo de la API en [FastAPI](https://fastapi.tiangolo.com/):

Para ello utilicé un entorno virtual donde se instaló FastAPI, Pandas y Uvicorn. Luego desarrollé la API con FastApi (podras encontrar todo el código dentro del archivo [main.py](/main.py), en donde en pocas lineas se realiza la configuración , se extra el dataset desde una url (para lograr disponibilizar los datos en la etapa del deploy) y se crean cinco funciones para las consultas: 

+ get_word_count: cantidad de veces que aparece una palabra en el título de peliculas o series, por plataforma.
+ get_score_count: cantidad de películas por plataforma con un puntaje mayor a 'xx' en determinado año.
+ get_second_score: la segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.
+ get_longest: película o serie que más duró según año, plataforma y tipo de duración.
+ get_rating_count: cantidad de series y películas por tipo de rating.

Durante la etapa de desarrollo revisé el funcionamiento integral de la API y sus consultas de manera local desde la terminal con el comando ***uvicorn main:app --reload***  en el localhost http://127.0.0.1:8000/ . Una vez logrado el adecuado funcionamiento de API de manera local realice en archivo de requerimientos con el comando  ***pip freeze > requirements.txt***. 

Aclaracion: Si ha utilizado el comando pip freeze > requirements.txt en powershell Windows, el archivo creado no está codificado en UTF-8. Cambie la codificación o cree un nuevo archivo con la codificación correcta para poder realizar el deploy. No olvide borrar de los requerimientos a uvicorn ya que no es necesario para el deploy.

### 3- Deployment en [Deta](https://www.deta.sh/?ref=fastapi):

Como primer paso hay que realizar una cuenta en Deta, luego crear una carpeta solo con los archivos [main.py](/main.py) y [requirements.txt](/requirements.txt) y desde esa carpeta ejecutar los siguientes comandos en PowerShell (si su sistema operativo no es Windows consulte la [documentación](https://docs.deta.sh/docs/micros/getting_started/?ref=fastapi) ):

+ ***iwr https://get.deta.dev/cli.ps1 -useb | iex*** -- Instalación del CLI.
+ ***deta login*** -- Abre el navegador para que pueda loguearse con su cuenta .
+ ***deta new --python*** -- Acaba de crear una nueva micro. Pruebe en el navegador el "endpoint" que otorga en la pantalla si dice "Hola Mundo" la conexión fue exitosa.
+ ***deta deploy*** -- Realiza el deploy del proyecto
+ ***deta auth disable*** -- Disponibiliza el proyecto para cualquier persona.

</div>

## ¿Te gustaría probar mi API? 

Podés hacer click en los siguientes enlaces para probar cada una de las consultas detalladas anteriormente: 

+ https://07o5qt.deta.dev/get_word_count/(netflix,love)
+ https://07o5qt.deta.dev/get_score_count/(netflix,85,2010)
+ https://07o5qt.deta.dev/get_second_score/(amazon)
+ https://07o5qt.deta.dev/get_longest/(netflix,min,2016)
+ https://07o5qt.deta.dev/get_rating_count/(18%2B)

</div>

## Tecnologías Utilizadas

* [Python](https://www.python.org/)
* [Pandas](https://pandas.pydata.org/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Uvicorn](https://www.uvicorn.org/)
* [Deta](https://www.deta.sh/)

</div>

## Para realizar este proyecto las siguientes fuentes de información fueron de gran ayuda: 

+ https://fastapi.tiangolo.com/tutorial/
+ https://docs.deta.sh/docs/micros/getting_started/?ref=fastapi
+ https://awstip.com/deploying-a-fastapi-service-on-deta-959f86a8982a
+ https://www.youtube.com/watch?v=J0y2tjBz2Ao&t=685s
+ https://www.youtube.com/watch?v=dAQENEPAqsc&t=2219s
