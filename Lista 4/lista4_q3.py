alun_par = []
alun_impar = []
alunos = []
i = 0

qnt = int(input("Quantos alunos? "))

print("Digite os nomes dos alunos:")

for i in range(qnt): #laço para armazenas posições impares em alun_impar e pares em alun_par
  if ((i+1)%2 == 0):
    alun_par.append(input())
  else:
    alun_impar.append(input())

alun_par.reverse() #coloca os itens de alun_par ao contrario

if (qnt%2 != 0): #se a qnt de alunos for impar
  alunos.append(alun_impar[0])
  for i in range(int((qnt-1)/2)): 
    alunos.append(alun_par[i])
    alunos.append(alun_impar[i+1])
else: #se a qnt de alunos for par
  for i in range(int(qnt/2)):
    alunos.append(alun_impar[i])
    alunos.append(alun_par[i])
print("")
print("Nova lista:")
for i in alunos:
  print(i)