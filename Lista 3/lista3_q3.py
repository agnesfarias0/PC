n = int(input("n? "))
i = 1

for i in range(n):
  
  prod = i*(i+1)*(i+2)
  i = i+1

  if (prod == n):
    break

if (i == n):
  print("não é triangular")
else:
  print("é triangular")