# back-test
Funciones basicas para el back end
## Requerimientos

```
pip install fastapi
pip install "uvicorn[standard]"
pip install jinja2
pip install pandas
```

## Entorno virtual

```
python -m venv env
.\env\Scripts\activate 
pip install -r requirements.txt
```

## Prueba

Para correr ejecute el comando:

```
python process_files.py
```

## Inventario de cosas

### Lista

- [x] Se obtienen los dataframes para la aplicación a partir de archivos CSV.
- [x] Se pueden modificar las preguntas y la puntuacion del dataframe de la encuesta (```modificarPregunta()```) - Ver observacion 1.
- [x] Se pueden agregar preguntas y la puntuacion al dataframe de la encuesta (```agregarPregunta()```) - Ver observacion 1.


### Observaciones
1. Fue necesario modificar el archivo cvs de las preguntas para agregar las columnas asociadas a la puntuacion.