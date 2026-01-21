a = "ramo"
b = "amort"
anagrama = True

if len(a) == len(b):
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

