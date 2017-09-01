#!/usr/bin/python

import re


str= 'pepe,papa,333333/carlos,apellido,454444'

tuples = re.findall(r'([\w]+),([\w]+)', str)
#Guardamos solo nombre y apellido
print ('Nombres y apellidos')
print (tuples)
print ('Apellidos y nombres')
for tuple in tuples:
        #Mostramos apellido y nombre
        print (tuple[1], tuple[0])

