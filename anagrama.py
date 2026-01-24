a = "saunas"
b = "susana"
anagrama = True

def anagramit(a,b):
  if len(a.lower()) == len(b.lower()):
    return True
  for i in a:
    for j in b:
        if i == j:
          print (f"a{a.index(i)} match in b, index {b.index(j)}")
          break
          
    else:
      print(f"stoped in:a{a.index(i)} b{b.index(j)} no es un anagrama")
      anagrama = False
      break
        
  if anagrama:    
    print("si es un anagrama!")
        
         
  else:
    print("no puede ser un anagrama")



  

def anagrec(a,b):
  # 1) se empieza por comparar la similitud en longitud de las palabras:
  if len(a) == 0 and len(b) == 0:
    return True # caso base 1: las variables esten vacias (no hay texto)
  elif len(a) != len(b):
    return False # caso base 2: las variables no tienen el mismo numero de caracteres (no es anagrama)
  
  #2) ahora se comparan al interior de las palabras (los valores de los indices).
  index = -1
  for i in range(len(b)): #se itera comparado a con b, usando i para los indices. 
    if a[0] == b[i]: # si la primera letra coincide:
      print(f"found letter {a[0]} from a in index b{i}")
      index = i #y se modifica el valor en la variable "index"
      break 
  #si no coincide la primera letra, la variable "index" simplemente no cambia:
  if index == -1:
    return False # no coincide ninguna letra
   
  else: #pero si cambiara, luego de la primera letra se ejecuta la recursion hasta el final    
    print(a[1:], b[:i]+b[i+1:])
    return anagrec(a[1:], b[:i]+b[i+1:])
    #b[:i] arranca diciendo "de 0 a 0" sumado a "de 0+1 al final". 
    # Asi, como el primer indice es 0 (porque S estaba en b0) no pasa nada con "b[:i]", 
    # que sería igual a decir "de 0 a 0", 
    # pero luego permite que se ejecute la recursividad solamente en las 
    # letras que van quedando, esten antees o despues de "i"

print(anagrec(a,b))

   
