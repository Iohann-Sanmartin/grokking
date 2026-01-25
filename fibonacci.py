

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


def fiborecu(s):
    s=s-1
    if s == 0:
        print("base uno. STOP")
        return [0]
    if s == 1:
        print("base uno. STOP")
        return [0,1] # aca uno SIEMPRE debe poner lo que necesita como punto de partida del calculo
    
    print ("entra a recursion:", s)
    lista = fiborecu(s-1)
    print ("sale de recursion:", s)
    print("lista:", lista)
    print(f"sumando {lista[-1]} y {lista[-2]} para hacer append")
    lista.append(lista[-1] + lista[-2]) # est hace que el ultimo valor de la lista se sume al penultimo valor y lo adiciona al final de la lista.
    print("lista despues del append:", lista)
    return lista #este return  entrega la MISMA lista. El valor viene de f==0 o f==1

print(fiborecu(2))

'''El fiborecu funciona porque en la recursion, el ultimo que entra es el primero que se resuelve y sale. 
De esta forma recursion siempre baja por la izquierda (es decir, todos los fiborecu (n-2)),
y va dejando abiertas las recursiones a medida que sube a resolverlas (reuerde: el primero el ultimo que abre,
resulve primero y sale). Luego sigue el de la derecha, que es fiborecu (n-1). 
Asi, si el argumento es 6 ("busque la posicion 6 en fibonacci"), fiborecu hace: f(6) f(4) f(2) (f0) y, cuando llega al caso base 0,
retorna 0. luego comienza a subir y resuelve el f(n-1) de f(2) y retorna 1. FINALMENTE CALCULA recu = 0+1 y recu = 1.



'''