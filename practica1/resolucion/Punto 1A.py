#!/usr/bin/python

import re

str = 'XI'
match = re.findall(r'^[XIVLCDM]+$', str)

#Si es numero romano se muestra en pantalla
for numero in match:
                print (numero)


