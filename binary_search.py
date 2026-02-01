letlst= ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
numlst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
item = input("type a number or a letter:") 

def binsearch(lst, item):
  low = 0
  high = len(letlst)-1
  guess = 0
  cnt = 0
  
  while low <= high:
    mid = int((low+high)/2)
    guess = lst[mid]
    if guess == item:
      print(f"FOUN IT! Runtime: BigO = {cnt}")
    if item > guess:
      low = mid + 1
      cnt+= 1
    else:
      high = mid - 1
      cnt+= 1    


while not item.isalpha() or item.isdigit():
    print(f"type ONLY a number or a letter")
    item = input("type a number or a letter:")
if item.isalpha():
    item = item.capitalize()
    print(f"you search for the letter : {item}")
    binsearch(letlst, item)
elif item.isdigit():
    item = int(item)
    print(f"you search for the number : {item}")
    binsearch(numlst, item)
if item not in numlst and item not in letlst:
    print("not found. Try agian")   
  



lista=[1,2,3,4,5,6,7,8,9]
inicio =0
fin =  len(lista)-1 #ojo esto es un indice (ultimo i == 8)


def binrecu(n, lista, inicio, fin):
    if inicio > fin:
        return False
        
    medio = (inicio+fin)//2
    print("valor medio",lista[medio])
    
    if n == lista[medio]:
        print("n es igual a", lista[medio])
        print("encontrado en el indice", medio)
        return lista[medio]
        
    if n < lista[medio]:
        print(f"entra index {medio}. Valor medio {lista[medio]}")
        return binrecu(n,lista,inicio, medio-1)
    else:
         return binrecu(n,lista,medio+1, fin)
    

binrecu (9,lista,inicio,fin)

''' La funcion pide 4 argumentos, de los cuales "medio" es el INDICE del Valor del medio(lista[medio]). 
Si el valor n es menor que valor del medio (lista[medio]), 
corre la primera recursion, que remplaza el final por el valor del INDICE medio-1. 
PERO, si n > valor del medio (lista[medio]), se remplaza inicio por el valor del INDICE medio+1'''

