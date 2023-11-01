valores = []

def ehPrimo(i):
  divs = [1]
  cont = 0
  
  for j in range(2,int(i)): #incrementa de 2 até o número para checar se é divisível
    if (int(i)%j == 0): #se o numero for divisivel incrementa o contador
      cont = cont + 1
      divs.append(j)
  divs.append(int(i))
  
  if (cont==0): #se o contador não for incrementado nenhuma vez, o número é primo
    return print(str(int(i)) + " é primo")
  else: #se o contador foi incrementado pelo menos uma vez, não é primo
    return print(str(int(i)) + " não é primo, os divisores são: " + str(divs))

n = int(input("Qual o valor de N? "))
print("Digite os valores:")

for i in range(n):
  valores.append(input())
  
print("A classificação é:")

for i in range(len(valores)):
  ehPrimo(valores[i])