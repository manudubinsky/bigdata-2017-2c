filename="properati-AR-2017-08-01-properties-sell-six_months.csv"
#from nombreArchivo import *
import collections
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.pyplot as plt2
import math
import re


dic={}

class DataFrame():    

    def __init__(self, filename): # abre el archivo csv, lee la primera fila y arma un diccionario que mapea cada nombre de columna a la posiciÃ³n que de la columna
        file= open(filename, encoding="utf8")
        primera=file.readline()
        print(primera)
        separar=primera.split(",")
        num=0
        global dic
        for valor in separar:
            dic[valor]=num
            num=num+1
        #print(dic)
        
    def cols(self):
        for clave in dic: 
            return clave
        
    def map(self, f):
        file= open(filename, encoding="utf8")
        for l in file:
            fila=l.split(",")
            f(self, fila)
            
            
    def getColValue(self, fila, colName):
        columna=dic[colName]
        return fila[columna]
         

df=DataFrame(filename)
total=0
cantidad=0

def f(self,fila):
    return fila

def fa(self,fila): #funciona bien
    a=self.getColValue(fila,"place_name")
    b=self.getColValue(fila,"rooms")
    c=self.getColValue(fila,"price_aprox_usd")
    global total
    global cantidad
    if a=="Quilmes":
        if b=="2" and c!='""':
            #print (c)
            total=total+float(c)
            cantidad=cantidad+1
    #print(a)

c = []
rooms = []
"""
def fb(self,fila): #funciona bien
    b=self.getColValue(fila,"rooms")
    global rooms
    if b:
        print (b) #pongo este print para ver que el programa corra
        rooms.append(b)
        global c
        c = collections.Counter(rooms)
"""  

lugar =[]
col = []

""" 
def fc(self, fila): #funciona bien
    a=self.getColValue(fila,"place_name")
    b=self.getColValue(fila,"rooms")
    global lugar
    if b=="2":
        lugar.append(a)
        global col
        col = collections.Counter(lugar)
"""  



def fd(self, fila): 
    a = self.getColValue(fila,'lat') #Latitud de las propiedades en String
    b = self.getColValue(fila,'lon') #Longitud de las propiedades en String
    congresoLat=-34.609864 #Latitud del Congreso
    congresoLon=-58.392692 #Longitud del Congreso
    if a!='""' and b!='""': #Discrimina los vacios
        a2=re.findall(r'[-][\d]+.[\d]+', a) #Quita los caracteres especiales
        for each in a2:
            a3=float(each) #Castea a float
            c=pow(a3-congresoLat,2) #Realiza las cuentas para calcular la distancia 
            d = pow(float(b)-58,2)
            print (math.sqrt(c+d))

lon=[]
lat=[]
def fe (self, fila):
    #Defino y modelo la variable para latitud
    a = self.getColValue(fila,'lat') #Latitud de las propiedades en String
    congresoLat=-34.609864 #Latitud del congreso
    global lat #Lista para usar en el Scatter
    if a!='""':
        a2=re.findall(r'[-][\d]+.[\d]+', a) #Quita caracteres especiales
        for each in a2:
            a3=float(each) #Castea a float
            a4=a3-congresoLat #Hace la diferencia
            if a4<0.1: #Si la diferencia es menor a 0.1, se agrega a la lista del Scatter
                lat.append(a4)
        
    #Defino y modelo la variable para longitud
    b = self.getColValue(fila,'lon') #Longitud de las propiedades en String
    congresoLon=-58.392692 #Longitud del congreso
    global lon #Lista para usar en el Scatter
    if b!='""':
        b2=re.findall(r'[-][\d]+.[\d]+', b) #Quita caracteres especiales
        for each in b2:
            b3=float(each) #Castea a float
            b4=b3+congresoLon #Hace la diferencia
            if b4<0.1: #Si la diferencia es menor a 0.1, se agrega a la lista del Scatter
                lon.append(b4)
                print (lon)
    #Scatter Plot
    plt.scatter(lat, lon) 
    for lat_count, lon_count in zip(lat, lon): #MALDITO ERROR
        xy=(lat_count, lon_count)
    plt.show()


df.__init__(filename)
df.cols()
df.map(fe)

#print (total/cantidad) # A -- Promedio de valor de deptos
#print (cantidad)

#print (c) # B -- Muestra la cantidad de repeticiones por cada ambiente
"""
#Histograma Punto B
ambientes = []
repeticion = []
mc = c.most_common(20)
for i in mc:
        ambientes.append(i[0])
        repeticion.append(i[1])
        
print (matplotlib.rcParams['backend'])
xs = [i + 0.1 for i, _ in enumerate(ambientes)]
plt.bar(xs,repeticion)

plt.ylabel("Numero de publicaciones")
plt.title("Cantidad de ambientes")

plt.xticks([i for i, _ in enumerate(ambientes)],ambientes)
plt.show()
"""
#print (col)
"""
#Histograma Punto C
dosambientes = []
repeticion2amb = []
mc2 = col.most_common(10)
for h in mc2:
    dosambientes.append(h[0])
    repeticion2amb.append(h[1])
xs2 = [i + 0.1 for i, _ in enumerate(dosambientes)]
plt2.bar(xs2,repeticion2amb)

plt2.ylabel("Numero de publicaciones 2 ambientes")
plt2.title("Barrios")

plt2.xticks([i for i, _ in enumerate(dosambientes)],dosambientes)
plt2.show()"""

#print (dic)
        
