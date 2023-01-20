#Importar de las librerías necesarias.
from fastapi import FastAPI
import pandas as pd

#Instanciamos la App y le damos un título, una descripción y una versión.
app = FastAPI(title='PI-01 Jacqueline Dominguez',
            description='Bootcamp Henry Data Science',
            version='1.0.1')

@app.get('/') # Primer respuesta de la API 
async def index():
    return {'Proyecto Individual Data Engineer- Bootcamp Henry Data Science'}

@app.get('/about/') # Acerca de la API
async def about():
    return {'Proyecto Individual Data Engineer Bootcamp Henry Data Science realizado por Jacqueline Dominguez cohorte 06'}

    
#Ahora definiremos las consultas a realizar en la API a nuestro csv
    
#1-Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma
#Puede probar con /get_word_count/(netflix,love)

@app.get('/get_word_count/({platform},{keyword})')  
async def get_word_count(platform:str,keyword:str):    
    data = pd.read_csv('https://raw.githubusercontent.com/JacqueDominguez/PI01-Data-Engineering/main/Datasets/data.csv')
    if platform == 'netflix':
        #Filtro de plataforma y de Titulo que contiene la keyword, 
        df=data[(data['id'].str.startswith('n')) & (data['title'].str.contains(str(keyword),case=False))] # case es para que no distinga entre mayúsculas y minúsculas
        rdo=df['id'].count()
        datos = {'Plataforma':[str(platform).capitalize()],'Cantidad':[str(rdo)]}
        return datos
    elif platform == 'disney':
        #Filtro de plataforma y de Titulo que contiene la keyword, 
        df=data[(data['id'].str.startswith('d')) & (data['title'].str.contains(str(keyword),case=False))] # case es para que no distinga entre mayúsculas y minúsculas
        rdo=df['id'].count()
        datos = {'Plataforma':[str(platform).capitalize()],'Cantidad':[str(rdo)]}
        return datos
    elif platform == 'hulu':
        #Filtro de plataforma y de Titulo que contiene la keyword, 
        df=data[(data['id'].str.startswith('d')) & (data['title'].str.contains(str(keyword),case=False))] # case es para que no distinga entre mayúsculas y minúsculas
        rdo=df['id'].count()
        datos = {'Plataforma':[str(platform).capitalize()],'Cantidad':[str(rdo)]}
        return datos
    elif platform == 'amazon':
        #Filtro de plataforma y de Titulo que contiene la keyword, 
        df=data[(data['id'].str.startswith('d')) & (data['title'].str.contains(str(keyword),case=False))] # case es para que no distinga entre mayúsculas y minúsculas
        rdo=df['id'].count()
        datos = {'Plataforma':[str(platform).capitalize()],'Cantidad':[str(rdo)]}
        return datos
    else :
        return {'El valor ingresado no corresponde a una plataforma válida, pruebe con alguno de los siguientes valores' : ['netflix','hulu','disney','amazon'] }    
    
#2-Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año
#Puede probar con /get_score_count/(netflix,85,2010)

@app.get('/get_score_count/({platform},{score},{year})')  
async def get_score_count(platform:str,score:int,year:int):  
    data = pd.read_csv('https://raw.githubusercontent.com/JacqueDominguez/PI01-Data-Engineering/main/Datasets/data.csv')
    if platform == 'netflix':
        #Filtro de peliculas ,plataforma ,puntaje y año
        df=data[(data['type']=='movie') & (data['id'].str.startswith('n')) & (data['score'] > int(score)) & (data['release_year'] == int(year))]
        rdo=df['id'].count()
        datos = {'Plataforma':[str(platform).capitalize()],'Cantidad':[str(rdo)]}
        return datos
    elif platform == 'hulu':
        #Filtro de peliculas ,plataforma ,puntaje y año
        df=data[(data['type']=='movie') & (data['id'].str.startswith('h')) & (data['score'] > int(score)) & (data['release_year'] == int(year))]
        rdo=df['id'].count()
        datos = {'Plataforma':[str(platform).capitalize()],'Cantidad':[str(rdo)]}
        return datos
    elif platform == 'disney':
        #Filtro de peliculas ,plataforma ,puntaje y año
        df=data[(data['type']=='movie') & (data['id'].str.startswith('d')) & (data['score'] > int(score)) & (data['release_year'] == int(year))]
        rdo=df['id'].count()
        datos = {'Plataforma':[str(platform).capitalize()],'Cantidad':[str(rdo)]}
        return datos
    elif platform == 'amazon':
        #Filtro de peliculas ,plataforma ,puntaje y año
        df=data[(data['type']=='movie') & (data['id'].str.startswith('a')) & (data['score'] > int(score)) & (data['release_year'] == int(year))]
        rdo=df['id'].count()
        datos = {'Plataforma':[str(platform).capitalize()],'Cantidad':[str(rdo)]}
        return datos
    else:
        return {'El valor ingresado no corresponde a una plataforma válida, pruebe con alguno de los siguientes valores' : ['netflix','hulu','disney','amazon'] }    
    
#3- La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos
# Puede probar con /get_second_score/(amazon)

@app.get('/get_second_score/({platform})')  
async def get_second_score(platform:str):
    data = pd.read_csv('https://raw.githubusercontent.com/JacqueDominguez/PI01-Data-Engineering/main/Datasets/data.csv')
    if platform == 'amazon':
        df=data[(data['type']=='movie') & (data['id'].str.startswith('a'))] #Filtro de peliculas y plataforma
        orden=df.sort_values(by=['score', 'title'],ascending=[False, True])#Ordenar por Score (Desc) y Title(Asc)
        rdo= {'Titulo':[str(orden.iloc[1,3])],'Puntaje':[str(orden.iloc[1,13])]}
        return rdo
    elif platform == 'disney':
        df=data[(data['type']=='movie') & (data['id'].str.startswith('d'))] #Filtro de peliculas y plataforma
        orden=df.sort_values(by=['score', 'title'],ascending=[False, True])#Ordenar por Score (Desc) y Title(Asc)
        rdo= {'Titulo':[str(orden.iloc[1,3])],'Puntaje':[str(orden.iloc[1,13])]}
        return rdo
    elif platform == 'hulu':
        df=data[(data['type']=='movie') & (data['id'].str.startswith('h'))] #Filtro de peliculas y plataforma
        orden=df.sort_values(by=['score', 'title'],ascending=[False, True])#Ordenar por Score (Desc) y Title(Asc)
        rdo= {'Titulo':[str(orden.iloc[1,3])],'Puntaje':[str(orden.iloc[1,13])]}
        return rdo
    elif platform == 'netflix':
        df=data[(data['type']=='movie') & (data['id'].str.startswith('n'))] #Filtro de peliculas y plataforma
        orden=df.sort_values(by=['score', 'title'],ascending=[False, True])#Ordenar por Score (Desc) y Title(Asc)
        rdo= {'Titulo':[str(orden.iloc[1,3])],'Puntaje':[str(orden.iloc[1,13])]}
        return rdo
    else:
        return {'El valor ingresado no corresponde a una plataforma válida, pruebe con alguno de los siguientes valores' : ['netflix','hulu','disney','amazon'] }    
    
#4- Película que más duró según año, plataforma y tipo de duración
# Puede probar con /get_longest/(netflix,min,2016)

@app.get('/get_longest/({platform},{typeduration},{year})')  
async def get_longest(platform:str,typeduration:str,year:int): 
    data = pd.read_csv('https://raw.githubusercontent.com/JacqueDominguez/PI01-Data-Engineering/main/Datasets/data.csv')
    if platform == 'netflix':
        df=data[data['id'].str.startswith('n')] #Filtro de plataforma
        if typeduration=='min':
            peli=df[(df['type']=='movie') & (df['release_year']== int(year)) ] #Filtro de peliculas y año
            orden=peli.sort_values(by='duration_int',ascending=False)#Ordenar por Tiempo de duración
            rdo = {'Title':[str(orden.iloc[0,3])],'Duration':[str(orden.iloc[0,14])],'Duration_Type':[str(orden.iloc[0,15])]}
            return rdo
        elif typeduration=='season':
            serie=df[(df['type']=='tv show') & (df['release_year']== int(year)) ] #Filtro de serie y año
            orden=serie.sort_values(by='duration_int',ascending=False)#Ordenar por Tiempo de duración
            rdo = {'Title':[str(orden.iloc[0,3])],'Duration':[str(orden.iloc[0,14])],'Duration_Type':[str(orden.iloc[0,15])]}
            return rdo
        else:
            return {'Ingrese en el parametro typeduration alguno de los siguientes valores' : ['min','season'] }
    elif platform == 'hulu':
        df=data[data['id'].str.startswith('h')] #Filtro de plataforma
        if typeduration=='min':
            peli=df[(df['type']=='movie') & (df['release_year']== int(year)) ] #Filtro de peliculas y año
            orden=peli.sort_values(by='duration_int',ascending=False)#Ordenar por Tiempo de duración
            rdo = {'Title':[str(orden.iloc[0,3])],'Duration':[str(orden.iloc[0,14])],'Duration_Type':[str(orden.iloc[0,15])]}
            return rdo
        elif typeduration=='season':
            serie=df[(df['type']=='tv show') & (df['release_year']== int(year)) ] #Filtro de serie y año
            orden=serie.sort_values(by='duration_int',ascending=False)#Ordenar por Tiempo de duración
            rdo = {'Title':[str(orden.iloc[0,3])],'Duration':[str(orden.iloc[0,14])],'Duration_Type':[str(orden.iloc[0,15])]}
            return rdo
        else:
            return {'Ingrese en el parametro typeduration alguno de los siguientes valores' : ['min','season'] }
    elif platform == 'disney':
        df=data[data['id'].str.startswith('d')] #Filtro de plataforma
        if typeduration=='min':
            peli=df[(df['type']=='movie') & (df['release_year']== int(year)) ] #Filtro de peliculas y año
            orden=peli.sort_values(by='duration_int',ascending=False)#Ordenar por Tiempo de duración
            rdo = {'Title':[str(orden.iloc[0,3])],'Duration':[str(orden.iloc[0,14])],'Duration_Type':[str(orden.iloc[0,15])]}
            return rdo
        elif typeduration=='season':
            serie=df[(df['type']=='tv show') & (df['release_year']== int(year)) ] #Filtro de serie y año
            orden=serie.sort_values(by='duration_int',ascending=False)#Ordenar por Tiempo de duración
            rdo = {'Title':[str(orden.iloc[0,3])],'Duration':[str(orden.iloc[0,14])],'Duration_Type':[str(orden.iloc[0,15])]}
            return rdo
        else:
            return {'Ingrese en el parametro typeduration alguno de los siguientes valores' : ['min','season'] }
    elif platform == 'amazon':
        df=data[data['id'].str.startswith('a')] #Filtro de plataforma
        if typeduration=='min':
            peli=df[(df['type']=='movie') & (df['release_year']== int(year)) ] #Filtro de peliculas y año
            orden=peli.sort_values(by='duration_int',ascending=False)#Ordenar por Tiempo de duración
            rdo = {'Title':[str(orden.iloc[0,3])],'Duration':[str(orden.iloc[0,14])],'Duration_Type':[str(orden.iloc[0,15])]}
            return rdo
        elif typeduration=='season':
            serie=df[(df['type']=='tv show') & (df['release_year']== int(year)) ] #Filtro de serie y año
            orden=serie.sort_values(by='duration_int',ascending=False)#Ordenar por Tiempo de duración
            rdo = {'Title':[str(orden.iloc[0,3])],'Duration':[str(orden.iloc[0,14])],'Duration_Type':[str(orden.iloc[0,15])]}
            return rdo
        else:
            return {'Ingrese en el parametro typeduration alguno de los siguientes valores' : ['min','season'] }
    else:
        return {'Ingrese en el parametro plataforma alguno de los siguientes valores' : ['netflix','hulu','disney','amazon'] }


    
#5-Cantidad de series y películas por rating
# Puede probar con /get_rating_count/(18%2B)

@app.get('/get_rating_count/({rating})')  
async def get_rating_count(rating:str):
    data = pd.read_csv('https://raw.githubusercontent.com/JacqueDominguez/PI01-Data-Engineering/main/Datasets/data.csv')
    filtrado=data[data['rating'] == rating] #Filtro por el rating solicitado
    rdo=filtrado['id'].count()
    datos = {'Rating': rating ,'Cantidad': str(rdo)}
    return datos




