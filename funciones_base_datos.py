import pandas as pd
import numpy as np
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
import funciones_estadistica as estadistica
import pymysql
from sqlalchemy import create_engine, text
import ast

import time
import mysql.connector

#CREACIÓN BASE DE DATOS

# Conectar a MySQL usando pymysql

def conexion(df, anfitrion, usuario, contraseña, basedatos, archivo):
    connection = mysql.connector.connect(
        host= anfitrion,
        user= usuario,
        password= contraseña
    )
    # Crear un cursor
    cursor = connection.cursor()
    # Crear una base de datos
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {basedatos}")
    print("Base de Datos creada exitosamente.")
    time.sleep(3)
    #transformamos el df a csv
    df.to_csv(archivo, index=False)
    # Cargar el archivo CSV
    df = pd.read_csv(archivo)
    engine = create_engine(f'mysql+pymysql://{usuario}:{contraseña}@{anfitrion}/{basedatos}')
    return engine, connection



