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
  
  

