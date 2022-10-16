#!/usr/bin/env python
# coding: utf-8

# In[4]:


#pip install requests
import requests
import datetime
import csv
import os
from pathlib import Path
import pandas as pd


# #Organizando la información de Museos:

# In[37]:



#Descargar contenido
URL = "https://docs.google.com/spreadsheets/d/1PS2_yAvNVEuSY0gI8Nky73TQMcx_G1i18lm--jOGfAA"+"/export?format=csv"
respuesta = requests.get(URL)

#Obtener fecha
fecha=respuesta.headers['Date']
fecha2= fecha[5:16]
print(fecha2)

#Transformando la cadena de caracteres a fecha
fechaActual=datetime.datetime.strptime(fecha2, '%d %b %Y')
año = str(fechaActual.year)
mes = str(fechaActual.month)
dia = str(fechaActual.day)

#Creando la ruta de la carpeta
fecha_carpeta1 = año + '-'+ mes
fecha_archivo1 = 'museos-'+ dia+ '-'+ mes + '-' + año
print(fecha_archivo1)

#creación de carpeta
dir1 = os.path.join('Museos', fecha_carpeta1)

#Validación de la existencia de la ruta y creación de carpetas
try:
  os.makedirs(dir1)
except:
  with open(f"{dir1}/{fecha_archivo1}.csv", "wb") as f_out:
    f_out.write(respuesta.content)

print(dir1)

#creacion archivo .csv
with open(f"{dir1}/{fecha_archivo1}.csv", "wb") as f_out:
    f_out.write(respuesta.content)

fecha = dia + '-'+ mes + '-' + año


# In[6]:


#Obtención de directorio actual

#wd = os.getcwd()
#print("working directory is ", wd)


# In[31]:


#Leyendo los archivos descargados y normalizando:

csv_path1 = f"{dir1}/{fecha_archivo1}.csv"
Museosdata = pd.read_csv(csv_path1)

Museosdata.rename(columns={'categoria':'Categoria','provincia':'Provincia','localidad':'Localidad','nombre':'Nombre','direccion':'Domicilio','telefono':'Telefono'}, inplace=True)
col_drop=['Observaciones', 'Latitud', 'Longitud', 'TipoLatitudLongitud', 'Info_adicional', 'fuente', 'jurisdiccion', 'año_inauguracion', 'actualizacion']
Museosdata.drop(columns = col_drop, inplace = True)
#Museosdata.to_csv('Museos.csv')
Museosdata['Fecha'] = fecha
Museosdata.head()


# In[8]:


Museosdata.info()


# #Organizando la información de Salas de cine:

# In[9]:


#Descargar contenido
URL = "https://docs.google.com/spreadsheets/d/1o8QeMOKWm4VeZ9VecgnL8BWaOlX5kdCDkXoAph37sQM"+"/export?format=csv"
respuesta = requests.get(URL)

#Obtener fecha
fecha=respuesta.headers['Date']
fecha2= fecha[5:16]
print(fecha2)

#Transformando la cadena de caracteres a fecha
fechaActual=datetime.datetime.strptime(fecha2, '%d %b %Y')
año = str(fechaActual.year)
mes = str(fechaActual.month)
dia = str(fechaActual.day)

#Creando la ruta de la carpeta
fecha_carpeta2 = año + '-'+ mes
fecha_archivo2 = 'Cines-'+ dia+ '-'+ mes + '-' + año
print(fecha_archivo2)

#creación de carpeta
dir2 = os.path.join('Cines', fecha_carpeta2)
try:
  os.makedirs(dir2)
except:
  with open(f"{dir2}/{fecha_archivo2}.csv", "wb") as f_out:
    f_out.write(respuesta.content)
print(dir2)

#creacion archivo .csv
with open(f"{dir2}/{fecha_archivo2}.csv", "wb") as f_out:
    f_out.write(respuesta.content)


# In[40]:


csv_path2 = f"{dir2}/{fecha_archivo2}.csv"
Cinesdata = pd.read_csv(csv_path2)

#print(Xdata)
Cinesdata.rename(columns={'Dirección':'Domicilio','Categoría':'Categoria'}, inplace=True)
col_drop=['Observaciones', 'Latitud', 'Longitud', 'TipoLatitudLongitud', 'Información adicional', 'Fuente', 'tipo_gestion', 'año_actualizacion']
Cinesdata.drop(columns = col_drop, inplace = True)
#Cinesdata.to_csv('Cines.csv')
Cinesdata.head()

Cines_tabla = Cinesdata[['Provincia', 'Pantallas', 'Butacas', 'espacio_INCAA']]

Cinesdata.head()
Cines_tabla.head()


# #Bibliotecas Populares

# In[14]:


#Descargar contenido
URL = "https://docs.google.com/spreadsheets/d/1udwn61l_FZsFsEuU8CMVkvU2SpwPW3Krt1OML3cYMYk"+"/export?format=csv"
respuesta = requests.get(URL)

#Obtener fecha
fecha=respuesta.headers['Date']
fecha2= fecha[5:16]
print(fecha2)
fechaActual=datetime.datetime.strptime(fecha2, '%d %b %Y')
año = str(fechaActual.year)
mes = str(fechaActual.month)
dia = str(fechaActual.day)
fecha_carpeta3 = año + '-'+ mes
fecha_archivo3 = 'Bibliotecas-'+ dia+ '-'+ mes + '-' + año
print(fecha_archivo3)

#creación de carpeta
dir3 = os.path.join('Bibliotecas', fecha_carpeta3)

#Validación de la existencia de la ruta y creación de carpetas
try:
  os.makedirs(dir3)
except:
  with open(f"{dir3}/{fecha_archivo3}.csv", "wb") as f_out:
    f_out.write(respuesta.content)
print(dir3)

#creacion archivo .csv
with open(f"{dir3}/{fecha_archivo3}.csv", "wb") as f_out:
    f_out.write(respuesta.content)


# In[15]:


#Leyendo los archivos descargados y normalizando:
csv_path3 = f"{dir3}/{fecha_archivo3}.csv"
Bibliosdata = pd.read_csv(csv_path3)

Bibliosdata.rename(columns={'Cod_tel':'cod_area','Categoría':'Categoria','Teléfono':'Telefono'}, inplace=True)
col_drop=['Observacion', 'Subcategoria', 'Latitud', 'Longitud', 'TipoLatitudLongitud', 'Información adicional', 'Fuente', 'Tipo_gestion', 'Año_actualizacion', 'año_inicio']
Bibliosdata.drop(columns = col_drop, inplace = True)
#Bibliosdata.to_csv('Bibliotecas.csv')
Bibliosdata.head()


# #Conexion con postgresql

# In[16]:


pip install psycopg2


# In[17]:


import pandas as pd
#pip install SQLAlchemy


# In[38]:


#Creando conexión con la base de datos:
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:0000@localhost:5432/Challenge_Analytica')

#concatenando la información normalizada

df = pd.concat([Museosdata, Cinesdata, Bibliosdata])
df['Fecha'] = fecha
#Ingresando la tabla a la base de datos
df.to_sql("datos", con=engine, if_exists = "replace")

#Ingresando la tabla de cines
Cines_tabla['Fecha'] = fecha
Cines_tabla.to_sql("cines", con=engine, if_exists="replace")

result  = pd.read_sql_query("SELECT * FROM datos", engine)
result.Categoria


# In[22]:


#Procesando los datos conjuntos 

result  = pd.read_sql_query('SELECT * FROM Datos', engine)
result.dtypes


# In[28]:


#Conteo de registros por categoría

rg_cat = result.groupby(['Categoria']).agg({'Categoria' : 'count'})
print('los registros por categoría son:\n', rg_cat)


# In[24]:


#Conteo de registros por fuente:

#enlace museos

cant_mus_fuente = Museosdata.axes[0]
print ("El conteo de registros por la fuente de museos es:", cant_mus_fuente.stop)

#enlace bibliotecas

cant_biblio_fuente = Bibliosdata.axes[0]
print ("El conteo de registros por la fuente de bibliotecas es:", cant_biblio_fuente.stop)

#enlace cines

cant_cines_fuente = Cinesdata.axes[0]
print ("El conteo de registros por la fuente de cines es:", cant_cines_fuente.stop)


# In[27]:


#Cantidad de registros por provincia y categoría:

a= result[(result.Categoria=='Espacios de Exhibición Patrimonial')]
a =a.groupby(['Provincia']).agg({'Provincia' : 'count'})

b = result[(result.Categoria=='Bibliotecas Populares')]
b = b.groupby(['Provincia']).agg({'Provincia' : 'count'})



c = result[(result.Categoria=='Salas de cine')]
c = c.groupby(['Provincia']).agg({'Provincia' : 'count'})

print ('El conteo de registros por provincia de los museos es:\n', a)
print('El conteo de registros por provincia de las bibliotecas es:\n', b)
print('El conteo de registros por provincia de los cines es:\n', c)


# In[ ]:




