termos = int(input("número de termos: "))

i = 0

fib = [1,1]

if termos == 0:
  print("série de Fibonacci: []")
elif termos == 1:
  print("série de Fibonacci: [1]")
else:
  for i in range(termos-2):
    soma = fib[i]+fib[i+1]
    fib.append(soma)
  print("série de Fibonacci: ", fib)