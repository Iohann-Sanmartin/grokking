

# implementacion de fibonacci con ciclo
# def fibcic(n):
#    fib = [0,1]
#    a = fib[0]
#    b = fib[1]
#    for i in range(n):
#     print(i)
#     f = a+b
#     fib.append(f)
#     a = b
#     b = f
#     print(fib)

#fibcic(5)

# implementacion de fibonacci con recursión
def fiborecu(n):
  fiblist = [0,1]
  print(fiblist)
  
  if n == 0:
    print("n = a cero. STOP")
    return 0
  
  if n == 1:
     print("n = a uno. STOP")
     return 1
  else:
    print ("entra a recursion:", n)
    recu = fiborecu(n-2) + fiborecu (n-1)
    fiblist.append(recu)
    print ("sale de recursion:", n)
    print(recu)
    return recu #este return no entrega un valor. lo que hace es relanzar la recursion.el valor viene de f==0 o f==1
  
  
print(fiborecu(6))

'''El fiborecu funciona porque en la recursion, el ultimo que entra es el primero que se resuelve y sale. 
De esta forma recursion siempre baja por la izquierda (es decir, todos los fiborecu (n-2)),
y va dejando abiertas las recursiones a medida que sube a resolverlas (reuerde: el primero el ultimo que abre,
resulve primero y sale). Luego sigue el de la derecha, que es fiborecu (n-1). 
Asi, si el argumento es 6 ("busque la posicion 6 en fibonacci"), fiborecu hace: f(6) f(4) f(2) (f0) y, cuando llega al caso base 0,
retorna 0. luego comienza a subir y resuelve el f(n-1) de f(2) y retorna 1. FINALMENTE CALCULA recu = 0+1 y recu = 1.



'''