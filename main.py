import psycopg2
from flask import Flask, redirect, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import PaawordField, StringField, SubmitField

app = Flask (__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('libros')
def libros():
    # Conectar con la base de datos
    conexion = psycopg2.connect(
        database="biblioteca3a",
        user="postgres",
        password="2580",
        host="localhost",
        port="5432"
    )
    # Crar un cursor para recorrer el contenido de las tablas
    cursor = conexion.cursor()
    # ejecutar consulta en postgres, informacion de libros
    cursor.execute('''SELECT * FROM libros''')
    datos = cursor.fetchall()
    # cerrar conexion a la bd
    cursor.close()
    conexion.close()
    return render_template('libros.html', datos=datos)