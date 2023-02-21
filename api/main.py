from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pandas as pd
from html_tags import *

app = FastAPI()

data = pd.read_csv('data.csv')

@app.get("/")
def read_root():
    
    content = html_home
    return HTMLResponse(content)


@app.get("/menu")
async def get_dataframe():
    return ("estos comandos te pueden servir: ", "\n", "hola")


@app.get("/get_max_duration")
def duration_info():
    content = html_duration
    return HTMLResponse(content)
    
@app.get("/get_max_duration/{anio}/{plataforma}/{tipo_duracion}")
def get_max_duration(anio: int, plataforma: str, tipo_duracion:str):
    
    #Restringimos los inputs para el anio
    if type(anio) != int:
        return ("El año tiene que ser un numero entero")
    elif anio < data.release_year.min():
        return ("Disculpa, solo tenemos datos de peliculas desde " + str(data.release_year.min()))
    elif anio > data.release_year.max():
        return ("Disculpa, solo tenemos datos de peliculas hasta " + str(data.release_year.max()))
    
    #Restringimos el tipo de duracion
    tipos = list(data.duration_type.unique())
    if type(tipo_duracion) != str:
        return ("El tipo de duracion tiene que ser una cadena de caracteres")
    elif tipo_duracion not in tipos:
        return ("Disculpa, los tipos de duracion solo pueden ser " + str(tipos[0]) + " o " + str(tipos[1]))
        
    #Estandarizar el input plataforma a los ID:
    if plataforma == "amazon":
        plat = "as"
    elif plataforma == "disney":
        plat = "ds"
    elif plataforma == "hulu":
        plat = "hs"
    elif plataforma == "netflix":
        plat = "ns"
    else:
        return ("Plataforma incorrecta. Las opciones son: amazon, disney, hulu, netflix. Recuerde escribir todo en minúsculas.")

    filtro = (data["show_id"].str.contains(plat)) & (data["release_year"] == anio) & (data["duration_type"] == tipo_duracion)
    output = data[filtro]
    duracion = output.duration_int.max()
    pelicula = output.loc[output.duration_int == duracion]
    
    if tipo_duracion == "min":
        return (f"La pelicula más larga de '{plataforma}' en el año {anio} es: '{pelicula.title.iloc[0]}' del director: '{pelicula.director.iloc[0]}' con una duración de: {pelicula.duration_int.iloc[0]} {tipo_duracion}")
    else:
        return (f"La serie más larga de '{plataforma}' en el año {anio} es: '{pelicula.title.iloc[0]}' del director: '{pelicula.director.iloc[0]}' con una duración de: {pelicula.duration_int.iloc[0]} {tipo_duracion}")

#====================================
@app.get("/get_score_count")
def score_info():
    content = html_score
    return HTMLResponse(content)
@app.get("/get_score_count/{plataforma}/{score}/{anio}")    
def get_score_count(plataforma:str, score:float, anio:int):
    
    #Restringimos los inputs para el anio
    if type(anio) != int:
        return ("El año tiene que ser un numero entero")
    elif anio < data.release_year.min():
        return ("Disculpa, solo tenemos datos de peliculas desde " + str(data.release_year.min()))
    elif anio > data.release_year.max():
        return ("Disculpa, solo tenemos datos de peliculas hasta " + str(data.release_year.max()))
    
    #Restringimos el score
    if score > data.Promedio_Valoraciones.max():
        return (f"Disculpa, pero el score maximo registrado es {data.Promedio_Valoraciones.max()}, recomendamos usar un numero inferior")
    elif score <= 0:
        return ("El score no puede ser un numero negativo")
        
    #Estandarizar el input plataforma a los ID:
    if plataforma == "amazon":
        plat = "as"
    elif plataforma == "disney":
        plat = "ds"
    elif plataforma == "hulu":
        plat = "hs"
    elif plataforma == "netflix":
        plat = "ns"
    else:
        return ("Plataforma incorrecta. Las opciones son: amazon, disney, hulu, netflix. Recuerde escribir todo en minúsculas.")

    filtro = (data["show_id"].str.contains(plat)) & (data["release_year"] == anio) & (data["Promedio_Valoraciones"] > score)
    output = data[filtro]
    return (f"En el año {anio} en {plataforma} hubo '{len(output)}' peliculas con mas de {score} de score")

#====================================
@app.get("/get_count_platform")
def platform_info():
    content = html_platform
    return HTMLResponse(content)
@app.get("/get_count_platform/{plataforma}")
def get_count_platform(plataforma):
    #Estandarizar el input plataforma a los ID:
    if plataforma == "amazon":
        plat = "as"
    elif plataforma == "disney":
        plat = "ds"
    elif plataforma == "hulu":
        plat = "hs"
    elif plataforma == "netflix":
        plat = "ns"
    else:
        return ("Plataforma incorrecta. Las opciones son: amazon, disney, hulu, netflix. Recuerde escribir todo en minúsculas.")

    filtro = data["show_id"].str.contains(plat)
    output = data.loc[filtro] 
    
    return (f"En '{plataforma}' hay {len(output)} registros entre series y peliculas")

#=====================================
@app.get("/get_actor")
def platform_info():
    content = html_actor
    return HTMLResponse(content)
@app.get("/get_actor/{plataforma}/{anio}")
def get_actor(plataforma:str, anio:int):
    
    #Restringimos los inputs para el anio
    if type(anio) != int:
        return ("El año tiene que ser un numero entero")
    elif anio < data.release_year.min():
        return ("Disculpa, solo tenemos datos de peliculas desde " + str(data.release_year.min()))
    elif anio > data.release_year.max():
        return ("Disculpa, solo tenemos datos de peliculas hasta " + str(data.release_year.max()))
    
    #Estandarizar el input plataforma a los ID:
    if plataforma == "amazon":
        plat = "as"
    elif plataforma == "disney":
        plat = "ds"
    elif plataforma == "hulu":
        plat = "hs"
    elif plataforma == "netflix":
        plat = "ns"
    else:
        return ("Plataforma incorrecta. Las opciones son: amazon, disney, hulu, netflix. Recuerde escribir todo en minúsculas.")

    filtro = (data["show_id"].str.contains(plat) & (data["release_year"] == anio))
    output = data[filtro]
    #Los datos cambian de tipo con la exportacion a CSV por lo que tenemos que corregirlo
    output.cast = output.cast.apply(eval)
    
    # convertir la columna 'cast' en una lista plana
    lista_actores = output['cast'].explode().reset_index(drop=True)

    # contar cuántas veces se repite cada nombre de actor
    conteo_actores = lista_actores.value_counts().reset_index()
    conteo_actores = conteo_actores.drop(index=0, axis=0)

    actor_maximo = conteo_actores["index"].iloc[conteo_actores.cast.idxmax()]
    numero = len(output[output['cast'].apply(lambda x: actor_maximo in x)])
    return (f"El actor con más peliculas en {anio} fué '{actor_maximo}' con {numero} peliculas en total")

