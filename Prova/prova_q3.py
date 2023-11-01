def soma(n):
  mult = []
  i = 0
  while (i*3) < n:
    mult.append(i*3)
    i = i+1
  i = 0
  while (i*5) < n:
    if (i*5) in mult:
      i = i+1
    else:
      mult.append(i*5)
      i = i+1
  return sum(mult)

n = int(input("N ="))
print(soma(n))