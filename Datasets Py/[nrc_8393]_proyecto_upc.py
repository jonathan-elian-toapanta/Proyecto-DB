# -*- coding: utf-8 -*-
"""[NRC_8393]_PROYECTO_ToapantaMartinez_JonathanElian_UPC.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fPOIhW4UFpmXN4XFyhniCkQv0u03DSbW
"""

'''Primero importamos todas las librerias 
que vamos a utilizar'''

!pip install faker
import pandas as pd
import uuid
import random
from faker import Faker
import datetime

num_users=5000

# Generar 6 atributos de la entidad Coordenandas

features = [
    "IdUPC",
    "Primer_Nombre",
    "Apellido",
    "Tipo_UPC",
    "IdCiu",
    "Id_Coor"
]# Se crea un df para estos atributos
df = pd.DataFrame(columns=features)

"""# Id UPC"""

'''Mediante la libreria uuid se implementa un ID de la UPC, 
el cual va a ser único para cada dato obtenido'''

df['IdUPC'] = [uuid.uuid4().hex for i in range(num_users)]
print(df['IdUPC'].nunique()==num_users)

"""# Nombre Completo
    
"""

'''Mediante la libreria faker se creo un nombres falsos 
para cada agente que reside en la UPC nombre_completo'''
faker = Faker()

def Primer_Nom():
    return faker.first_name()

df['Primer_Nombre'] = [Primer_Nom() for i in range(num_users)]

'''Mediante la libreria faker se creo los apellidos falsos 
para cada agente que reside en la UPC esto compone al tributo nombre_completo'''
faker = Faker()

def Apellid():
    return faker.last_name()

df['Apellido'] = [Apellid() for i in range(num_users)]

"""# Tipo de UPC
 
"""

#Se asgino un estatus mediante un dato categorico demostrarndo si la provincia esta vigente o no existe
#Con ayuda de random.choices de establecio el estatus
tipo = ["Barrial", "Movil"]
df['Tipo_UPC'] = random.choices(
    tipo, 
    weights=(85,15), 
    k=num_users
)

"""# Id Ciudad

"""

'''Mediante la libreria uuid se implementa un ID a las ciudades, 
el cual va a ser único para cada dato obtenido'''

df['IdCiu'] = [uuid.uuid4().hex for i in range(num_users)]
print(df['IdCiu'].nunique()==num_users)

"""# Id Coordenanda"""

'''Mediante la libreria uuid se implementa un ID a Coordenadas, 
el cual va a ser unico para cada dato'''

df['Id_Coor'] = [uuid.uuid4().hex for i in range(num_users)]
print(df['Id_Coor'].nunique()==num_users)

"""# Resultados"""

#Creacion del dataset
df.to_csv('dataset_UPC.csv')

#Visualizacion del dataset
pd.read_csv('dataset_UPC.csv', index_col=0)