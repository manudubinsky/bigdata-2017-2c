import json
import collections
import re
import matplotlib.pyplot as plt
import random


f = open('trump.txt')
f2 = open ('wc.txt','a') #este archivo comienza vacio

lineas = []


for line in f:
    try:
        line2 = json.loads(line)
        tweet=line2["text"] #agarramos el texto de los tweets
        #print (tweet) #Imprime los tweets
        f2.write(tweet) #llevamos el texto a un txt
        
    except:
       continue

f.close()
f2.close()

str = open('wc.txt','r').read()
palabras = re.findall (r'\w+',str) #agarramos todas las palabras del los twets guardados en wc.txt

c = collections.Counter(palabras)
#print (c)

mc = c.most_common(20) #agarramos las primeras 20 palabras

#acomodamos el tamaño de las palabras
def text_size(total):
    return 8 + total /20000*20

#Mostramos el WC
for value,count in mc:
    plt.text(random.randint(0, 100),random.randint(0, 100), value,ha='center',va='center',size=text_size(count))
plt.xlabel("Palabras")
plt.ylabel("Cantidad de repeticiones")
plt.axis([0,100,0,100])
plt.xticks([])
plt.yticks([])
plt.show()




