'''From :  https://colab.research.google.com/drive/1XFojqrwvUGeuYQ5USLeMfR943jKcgHqG#scrollTo=794ec039'''
#Ejercicio 1: cuenta atras imprime 5,4,3,2,1

def countd(n):
    if n == 0 :
        return False
    else:
        print(n)
        #print("entra a recursion",n)
        var =  countd(n-1)
        #print("sale de recursion",n)
        return var

def countd2(n):
    if n==0: return
    print(n)
    countd2(n-1)

#countd2(5)

#Ejercicio 2: Ascendente. Imprime de 1 a n

def ascerecu(n):
    if n == 0:return

    var = ascerecu(n-1)
    print(n)

#ascerecu(5)

# Ejercicio 3 — Suma 1..n Devuelve la suma
def sumarecu(n):
    if n == 0:
        return 0
    suma = n + sumarecu(n-1)
    return suma

#print(sumarecu(5))

def s(n):
    return 0 if n==0 else n+s(n-1)

#print(s(5))

#Ejercicio 4 — Llamadas. Imprime llamadas
def llamadasrecu(n):
    if n == 0: 
        return
    else: 
        print(llamadasrecu(n-1))

llamadasrecu(5)

def f(n):
    print(n)
    if n > 0:
        return f(n-1)
    else:
        return None

#f(5)