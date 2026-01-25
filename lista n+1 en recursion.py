
def suma(s):
  if s == 0:
    #print("base 0")
    return [0]
  #print("entra a recursion el ", s)
  lista = suma(s-1)
  #print("sale de recursion el ", s)
  lista.append(s)
  return lista
  # print(list)

print(suma(3))
