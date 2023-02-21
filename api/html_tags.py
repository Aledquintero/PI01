html_home = '''<html>
<head>
	<title>Menú</title>
    <style>
        button {
            margin-bottom: 15px;
        }
    </style>    
	<style>
		.label-bold {
			font-weight: bold;
		}
	</style>
    <style>
		.label-custom {
			font-size: 12px;
			opacity: 0.7;
		}
	</style>
 
	<style>
		body {
			font-family: Arial, serif;
		}
	</style>

<body>
	<h1>Menú</h1>
    <label for="get_max_duration" class="label-bold">get_max_duration</label><br>
	<button onclick="location.href='https://proyectoale-5-e9984292.deta.app/get_max_duration'">click aqui</button>
    <label for="boton2" class="label-custom">Obten la pelicula con mayor duracion filtrado por 'Año', 'Plataforma' y 'Tipo de duracion'</label><br>
    
    <label for="boton2" class="label-bold">get_score_count</label><br>
	<button onclick="location.href='https://proyectoale-5-e9984292.deta.app/get_score_count'">click aqui</button>
    <label for="boton2" class="label-custom">Obten la cantidad de peliculas que sobrepasen un 'score' arbitrario filtrado por 'Año' y 'Plataforma'</label><br>
    
    <label for="boton2" class="label-bold">get_count_platform</label><br>
	<button onclick="location.href='https://proyectoale-5-e9984292.deta.app/get_count_platform'">click aqui</button>
    <label for="boton2" class="label-custom">Obten el numero de peliculas y series que se hicieron en una 'Plataforma' arbitraria</label><br>
 
    <label for="boton2" class="label-bold">get_actor</label><br>
	<button onclick="location.href='https://proyectoale-5-e9984292.deta.app/get_actor'">click aqui</button>
    <label for="boton2" class="label-custom">Obten el actor con más apariciones filtrado por 'Año'</label><br>
</body>
</html>'''

html_duration = '''<html>
<head>
	<title>get_max_duration</title>
    
    <style>
		.label-custom {
			font-size: 14px;
			opacity: 0.7;
		}
	</style>
	<style>
		body {
			font-family: Arial, serif;
		}
	</style>
 	<style>
		.color-block {
			background-color: #808080;
			padding: 20px;
			color: white;
			font-size: 18px;
			font-family: Arial, sans-serif;
		}
	</style>

<body>
    <h1>get_max_duration</h1>
    <div class = color-block>
        <label for="get_max_duration">Esta funcion recibe los parametros 'Año', 'Plataforma' y 'Tipo de duracion' para devolver la pelicula con mayor duración segun los filtros ingresados</label><br>
        <label for="boton2" class="label-custom">Esto se debe hacer en la barra de navegacion bajo la sintaxis /get_max_duration/{año}/{plataforma}/{tipo_duracion}</label><br>
    </div><br>
    <button onclick="location.href='https://proyectoale-5-e9984292.deta.app'">back</button>
</body>
</html>'''

html_score = '''<html>
<head>
	<title>get_score_count</title>
    
    <style>
		.label-custom {
			font-size: 14px;
			opacity: 0.7;
		}
	</style>
	<style>
		body {
			font-family: Arial, serif;
		}
	</style>
 	<style>
		.color-block {
			background-color: #808080;
			padding: 20px;
			color: white;
			font-size: 18px;
			font-family: Arial, sans-serif;
		}
	</style>

<body>
    <h1>get_score_count</h1>
    <div class = color-block>
        <label for="get_max_duration">Esta funcion recibe los parametros 'Plataforma', 'Score' y 'Año' para devolver la cantidad de peliculas que sobrepasaron ese score segun los filtros ingresados</label><br>
        <label for="boton2" class="label-custom">Esto se debe hacer en la barra de navegacion bajo la sintaxis /get_score_count/{plataforma}/{score}/{anio}</label><br>
    </div><br>
    <button onclick="location.href='https://proyectoale-5-e9984292.deta.app'">back</button>
</body>
</html>'''

html_platform = '''<html>
<head>
	<title>get_count_platform</title>
    
    <style>
		.label-custom {
			font-size: 14px;
			opacity: 0.7;
		}
	</style>
	<style>
		body {
			font-family: Arial, serif;
		}
	</style>
 	<style>
		.color-block {
			background-color: #808080;
			padding: 20px;
			color: white;
			font-size: 18px;
			font-family: Arial, sans-serif;
		}
	</style>

<body>
    <h1>get_count_platform</h1>
    <div class = color-block>
        <label for="get_max_duration">Esta funcion recibe el parametro 'Plataforma' para devolver la cantidad de peliculas que hay en esa plataforma</label><br>
        <label for="boton2" class="label-custom">Esto se debe hacer en la barra de navegacion bajo la sintaxis /get_count_platform/{plataforma}</label><br>
    </div><br>
	<button onclick="location.href='https://proyectoale-5-e9984292.deta.app'">back</button>
</body>
</html>'''

html_actor = '''<html>
<head>
	<title>get_actor</title>
    
    <style>
		.label-custom {
			font-size: 14px;
			opacity: 0.7;
		}
	</style>
	<style>
		body {
			font-family: Arial, serif;
		}
	</style>
 	<style>
		.color-block {
			background-color: #808080;
			padding: 20px;
			color: white;
			font-size: 18px;
			font-family: Arial, sans-serif;
		}
	</style>

<body>
    <h1>get_actor</h1>
    <div class = color-block>
        <label for="get_max_duration">Esta funcion recibe el parametro 'Plataforma' y 'Año' para devolver el actor que hizo mas apariciones en esa plataforma en ese año</label><br>
        <label for="boton2" class="label-custom">Esto se debe hacer en la barra de navegacion bajo la sintaxis /get_actor/{plataforma}/{año}</label><br>
    </div><br>
    <button onclick="location.href='https://proyectoale-5-e9984292.deta.app'">back</button>
</body>
</html>'''

#==========================================

