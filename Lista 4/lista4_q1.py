qnt = int(input("Quantos nomes?"))
nomes = []

for i in range(qnt):
  i = input()
  nomes.append(i)

nomes.reverse()

print("Você digitou:")

for i in range(0,qnt):
  print(nomes[i])