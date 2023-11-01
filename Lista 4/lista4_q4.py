n = int(input("Quantidade de jogadores? "))
print("Digite os dados para cada jogador:")
jogs = []
s_total = 0
b_total = 0
a_total = 0
s1_total = 0
b1_total = 0
a1_total = 0

for i in range(n): #inclui no vetor jogs os dados dos jogadores, n vezes
  jogs.append(input().split())

for i in range(n): #faz o somatorio totais e de sucesso e armazena em cada variavel
  s_total = s_total + int(jogs[i][1])
  b_total = b_total + int(jogs[i][2])
  a_total = a_total + int(jogs[i][3])
  s1_total = s1_total + int(jogs[i][4])
  b1_total = b1_total + int(jogs[i][5])
  a1_total = a1_total + int(jogs[i][6])

est_saq = float((s1_total/s_total)*100)
est_bloq = float((b1_total/b_total)*100)
est_atk = float((a1_total/a_total)*100)

print("As estatísticas do jogo são as seguintes: ")
print("Pontos de Saque: " + str(round(est_saq,2)) + " %")
print("Pontos de Bloqueio: " + str(round(est_bloq,2)) + " %")
print("Pontos de Ataque: " + str(round(est_atk,2)) + " %")