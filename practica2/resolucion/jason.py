import json


f = open('trump.txt')
print ("###########################################")
print ("Tweet Numero:")
print (1)  #Mostramos el primer tweet, con el que se comparará si los sucesivos tienen nuevas claves
primera = f.readline()
jason = json.loads(primera)
claves = jason.keys()
print (primera)
a=0
b=0
indentar = 0


for line in f:
    try:
    #print(line)
        #print(json.loads(line))
        line2 = json.loads(line)
        b=b+1
        if line2.keys() - claves:   #Mostramos los tweets que tengan una clave nueva
            print ("###########################################")
            print ("Tweet Numero:")
            print (a+2)
            print (line)
            claves = claves | line2.keys()
            a=a+1
        for clave in line2: #Mostramos clave y tipo de datos de todos los tweets
            #print (clave, type(line2[clave]))
            indentar = indentar +1 #esto lo puse porque el print imprime mucho, y al comentar el print me tira error de identar con el except



    except:
        continue
    
f.close()

print ("###########################################")
print ("Cantidad de tweets totales:")
print (b)
print ("###########################################")
print ("Cantidad de tweets con claves nuevas:")
print (a)
