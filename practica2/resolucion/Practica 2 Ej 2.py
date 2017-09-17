import json
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3
import matplotlib
import collections
import sys
import re
import numpy as np
import matplotlib.pyplot as plt4


f = open('trump.txt')
a = 0
b = 0
c = 0
d = 0
e = 0
h = 0
i = 0
j = 0
k = 0
l = 0
usuarios = []
seguidores = []
amigos = []

#datos del histograma
rangos = [] 
total = [] #followers
total2 = [] #amigos

#datos ej2, punto c
eastern = 0 #folowers
pacific = 0
central = 0
mountain = 0
#histograma
horarios = []
totalf = []

z = {}

for line in f:
    try:
        line2 = json.loads(line)
        name=line2["user"]["name"]
        #print (name) #Imprime lista con todos los nombres
        usuarios.append(name)
        followers = line2["user"]["followers_count"]
        #print (followers) #Imprime lista de followers (PUNTO A)
        seguidores.append(followers) #Miramos los followers y llenamos las variables 
        if followers > 0 and followers < 100:
            a = a +1
        if followers > 100 and followers < 1000:
            b = b +1
        if followers > 1000 and followers < 10000:
            c = c +1
        if followers > 10000 and followers < 100000:
            d = d +1
        if followers > 1000000:
            e = e +1
        friends = line2["user"]["friends_count"]
        #print (friends) #Imprime lista de amigos (PUNTO A)
        amigos.append(friends) #Miramos amigos y llenamos las variables
        if friends > 0 and friends < 100:
            h = h +1
        if friends > 100 and friends < 1000:
            i = i +1
        if friends > 1000 and friends < 10000:
            j = j +1
        if friends > 10000 and friends < 100000:
            k = k +1
        if friends > 1000000:
            l = l +1
        dif=line2["user"]["followers_count"]-line2["user"]["friends_count"]
        #print (dif) #Imprime diferencia entre followers y amigos (PUNTO B)
        if dif > 5000: #Criterio
            z[name] = dif
        #PUNTO C  miramos la cantidad de usuarios con mas de 10000 seguidores
        time=line2["user"]["time_zone"] #Todos los valores con la key TIME_ZONE se almacenan en la variable time
        if time=="Pacific Time (US & Canada)": #Compara los valores de la lista si son igual a Pacific Time (US & Canada)
            if followers > 10000:
                pacific = pacific +1
        if time=="Eastern Time (US & Canada)": #Compara los valores de la lista si son igual a Eastern Time (US & Canada)
            if followers > 10000:
                eastern = eastern +1
        if time=="Central Time (US & Canada)": #Compara los valores de la lista si son igual a Central Time (US & Canada)
            if followers > 10000:
                central = central +1
        if time=="Mountain Time (US & Canada)": #Compara los valores de la lista si son igual a Atlantic Time (US & Canada)
            if followers > 10000:
                mountain = mountain +1
 
    except:
       continue

#print (usuarios)
#print (seguidores)

print ("###########################")
print ("Vemos los usuarios que deberian ser instituciones")
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
print (str(z).translate(non_bmp_map)) #Mostramos todos los usuarios que deberian ser instituciones



#Lista con la info para el primer histograma
total.append(a)
total.append(b)
total.append(c)
total.append(d)
total.append(e)

#Lista con la info para el segundo histograma
total2.append(h)
total2.append(i)
total2.append(j)
total2.append(k)
total2.append(l)

#Lista con los rangos
rangos.append("0-100")
rangos.append("101-1000")
rangos.append("1001-10000")
rangos.append("10001-100000")
rangos.append("+100001")

#Lista con la info para un tercer histograma
totalf.append(pacific)
totalf.append(eastern)
totalf.append(central)
totalf.append(mountain)

#Lista con los horarios
horarios.append("Pacific")
horarios.append("Eastern")
horarios.append("Central")
horarios.append("Mountain")




#print (total)
#print (a)
print (matplotlib.rcParams['backend'])


#Histograma de followers
xs = [i + 0.1 for i, _ in enumerate(rangos)]
plt.bar(xs,total)

plt.ylabel("Personas")
plt.title("Rangos de Seguidores")

plt.xticks([i  for i, _ in enumerate(rangos)],rangos)
#plt.xticks([i + 0.5 for i, _ in enumerate(rangos)],rangos)

plt.show()

#Histograma de Amigos
xs2 = [n + 0.1 for n, _ in enumerate(rangos)]
plt2.bar(xs2,total2)

plt2.ylabel("Personas")
plt2.title("Rangos de Amigos")

plt2.xticks([n  for n, _ in enumerate(rangos)],rangos)

plt2.show()

#Histograma con los followers de cada uso horarios
xs3 = [m + 0.1 for m, _ in enumerate(horarios)]
plt3.bar(xs3,totalf)

plt3.ylabel("Personas con mas de 10000 Seguidores")
plt3.title("Uso horarios")

plt3.xticks([m  for m, _ in enumerate(horarios)],horarios)

plt3.show()

#Seguidores por uso horarios
print (totalf)
muestreo = [[pacific,eastern,central,mountain]]
#grid = muestreo.random.rand(1,4)
plt4.imshow(muestreo, interpolation='none', cmap='gray')
plt4.show()

    
f.close()
