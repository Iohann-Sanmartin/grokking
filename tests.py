
def fiborecu(s):
   
    if s == 1:
        #print("base uno. STOP")
        return [0,1]
    
    #print ("entra a recursion:", s)
    lista = fiborecu(s-1)
    #print ("sale de recursion:", s)
    #print("lista:", lista)
    #print(f"sumando {lista[-1]} y {lista[-2]} para hacer append")
    lista.append(lista[-1] + lista[-2]) # est hace que el ultimo valor de la lista se sume al penultimo valor y lo adiciona al final de la lista.
    #print("lista despues del append:", lista)
    return lista #este return  entrega la MISMA lista. El valor viene de f==0 o f==1

print(fiborecu(5))