def mdc(n1,n2):
  
  divsn1 = [1]
  divsn2 = [1]
  mdc = 0
  
  for i in range(2,n1): #incrementa de 2 até o número para checar se é divisível
    if (n1%i == 0): #se o numero for divisivel, armazena em divsn1
      divsn1.append(i)
  divsn1.append(n1)
  
  for i in range(2,n2): #incrementa de 2 até o número para checar se é divisível
    if (n2%i == 0): #se o numero for divisivel, armazena em divsn2
      divsn2.append(i)
  divsn2.append(n2)
  
  if max(divsn2) == max(divsn1):
    mdc = max(divsn2)
  else:
    for i in divsn1:
      for j in divsn2:
        if i == j:
          mdc = i
          
  return mdc

while True:
  n1 = int(input("Digite o primeiro número inteiro: "))
  n2 = int(input("Digite o segundo número inteiro: "))
  max_div = mdc(n1,n2)
  print("O Máximo Divisor Comum (MDC) de " + str(n1) + " e " + str(n2) + " é: " + str(max_div))