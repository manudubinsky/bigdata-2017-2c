##importa conector y crea coneccion a BD
import psycopg2, psycopg2.extras
conn = psycopg2.connect(database = 'world',user='postgres',password='',host='localhost')
filename = "top-1m.csv"

##diccionario
diccionario = {}
excel = {}

## crear cursor para obtener datos y ejectuar consulta
cur = conn.cursor()
cur.execute("SELECT code2,code FROM country")
for row in cur:
    #print (row) muestra bien
    diccionario [row[0]] = row[1]
#rows = cur.fetchall()
#print (rows)
for keys,values in diccionario.items():
    #print (keys)
    #print (values)
    print ("%s -> %s " %(keys,values))
    
file = open (filename, encoding="utf8")
##fila = file.readline()
for l in file:
    k = l.split(",")
    excel [k[0]] = k[1]



##for k,v in excel.items():
  ## print ("%s -> %s " %(k,v)) 

#separar dominio Y GUARDAR VARIABLES PARA INSERT

for j,o in excel.items():
    sitio_id = j
    sitio_code = None
    a = o.split(".")
    sitio_entidad = a[0]
    sitio_tipo = a[1].rstrip()
    ##print (a)
    ##print ("Primer dominio  " + a[1])
    long = len(a)
    if (long == 3):
        ##print ("Segundo dominio  " + a[2])
        sitio_pais = a[2].rstrip().upper()
        if sitio_pais in diccionario:
            sitio_code = diccionario [sitio_pais]
            ##print ("############################")
            ##print (sitio_code)
    cur.execute("INSERT INTO sitios VALUES (%s,%s,%s,%s) ", ( sitio_id, sitio_entidad, sitio_tipo, sitio_code));
    conn.commit()






    
