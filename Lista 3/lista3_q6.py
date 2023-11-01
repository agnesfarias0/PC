n1 = int(input("n1? "))
n2 = int(input("n2? "))

primos = []
  
for i in range(2,(n2)+1): #incrementa n1 ate n2
  
  cont = 0
  
  for j in range(2,i): #incrementa de 2 até o número para checar se é divisível
    if (i%j == 0): #se o numero for divisivel incrementa o contador
      # print(str(i) + " é Multiplo de " + str(j) + ", logo não é primo!")
      cont = cont + 1
      
  if (cont==0): #se o contador não for incrementado nenhuma vez, o número é primo
    primos.append(i)

print("Existem " + str(len(primos)) + " números primos entre " + str(n1) + " e " + str(n2))
# print(primos)