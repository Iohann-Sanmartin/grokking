

# implementacion de fibonacci con ciclo
def fibcic(n):
   fib = [0,1]
   a = fib[0]
   b = fib[1]
   for i in range(n):
    print(i)
    f = a+b
    fib.append(f)
    a = b
    b = f
    print(fib)

fibcic(5)

# implementacion de fibonacci con recursión
def fibo(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibo(n-2) + fibo(n-1)
    
print(fibo(7))