#!/usr/bin/python

import re

str = 'purple ,alice@goo;gle.com, b..lah monkey b;,ob@abc.com blah dishwasher'

print ('Se muestra el string completo')
print (str)
print ('Se remueven los signos de puntuación')
print (re.sub(r'([,.;]+)', r'', str))

