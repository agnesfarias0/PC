def eh_narc(n):
  num = list(n)
  soma = 0
  for i in num:
   soma = soma + (int(i))**len(n)
  if (soma)==int(n):
    return print("É um número narcisista.")
  else:
    return print("Não é um número narcisista.")
    
n = input()
eh_narc(n)