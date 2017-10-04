import time

def f():
    n = 1.0
    valor = 0.0
    actual = 0.0
    anterior = 1.0
    while actual != anterior:
        anterior = valor
        valor =(1+1/n)**n
        yield valor
        n += 1
        actual = valor

def f2():
    den=1.0
    suma=2.0
    i=2.0
    actual = 0.0
    anterior= 1.0
    while actual != anterior:
        anterior = suma
        den=den*i
        i+=1
        suma=suma + 1/den
        yield suma
        actual= suma
        
nums = f2()
valor2=0
for i in nums:
    valor2=i
print (valor2)

