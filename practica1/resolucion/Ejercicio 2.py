import re
import collections
import matplotlib.pyplot as plt
import matplotlib

#Texto a minuscula
with open('rey_lear.txt', 'r+') as f:
    text = f.read()
    f.seek(0)
    f.write(text.lower())
    #f.truncate()

#Eliminación de signos de puntuación y reescritura
string = open('rey_lear.txt').read()
new_str = re.sub('[.,?¿:;]', ' ', string)
open('rey_lear.txt', 'w').write(new_str)


str = open('rey_lear.txt','r').read()
palabras = re.findall (r'\w+',str)

c = collections.Counter(palabras)
print (c) #Imprime todo en formato PALABRA:NUMERO

f = 0
t = 0

print ('##########################')
print ('Impresion de texto')
mc = c.most_common()
print (mc)  #Esto imprime todo el texto en una lista (PALABRA,NUMERO)


print ('##########################')
print ('Impresion de primeras las palabras por separado y contando repeticiones')
for value, count in c.most_common():
    print (value,count) #Imprime todas las palabras una abajo de la otra, con sus ocurrencias
    f = f + count
    t = t + 1

print ('##########################')
print ('Impresion de la cantidad de palabras totales del texto')
print (f) #Imprime la cantidad de palaras totales del texto
print ('##########################')
print ('Impresion de la cantidad de palabras unicas del texto')
print (t) #Imprime la cantidad de palabras unicas
print ('##########################')
print ('Impresion de primeras 5 palabras')
print (mc[:5]) # Imprime las primeras 5
    




#Prohibidas
prohibidas = re.findall(r'\w+', open('prohibidas.txt').read().lower())

#Remover prohibidas
for i in prohibidas:
	del c[i]
mc = c.most_common(5)
print ('##########################')
print ('Impresion de la cantidad de palabras totales del texto sin las prohibidas')
print (mc)

#Creacion de listas para mostrar 
palabras =[]
repeticion = []

for i in mc:
	palabras.append(i[0])
	repeticion.append(i[1])

print (palabras)
print (repeticion)

print (matplotlib.rcParams['backend'])

xs = [i + 0.1 for i, _ in enumerate(palabras)]
plt.bar(xs,repeticion)

plt.ylabel("Cantidad de palabras")
plt.title("Rey Lear")

plt.xticks([i + 0.5 for i, _ in enumerate(palabras)],palabras)

plt.show()


