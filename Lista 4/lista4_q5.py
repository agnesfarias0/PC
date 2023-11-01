n = int(input("Qual o valor do N? "))
dados = []
print("Digite os dados:")

d1 = float(input()) #input anterior
dados.append(d1)

for i in range(n-1):
  d2 = float(input()) #novo input
  if (d1 < d2): #se o input anterior for menor que o novo input
    dados.append(d2) #armazenar novo input na lista
    d1 = d2 #input anterior passa a ser o valor do input
    continue #continua laço
  else:
    print("Erro! Conjunto tem de estar em ordem crescente")
    exit()

dados2 = dados.copy()

# calculo da mediana
if (n%2 != 0): 
  mediana = dados[int(((n+1)/2)-1)]
else:
  mediana = dados[int((((n/2)+((n/2)+1))/2)-1)]
  
#primeiro quartil
pos1 = round(n*(1/4))
prim_quart = dados[int(pos1-1)]

#terceiro quartil
pos2 = round(n*(3/4))
terc_quart = dados[int(pos2)]

inter = float((terc_quart-prim_quart)-1.5)

#limite inferior
inf = min(dados)
if (inf <= inter):
  lim_inf = inf
else:
  dados2.pop(0)
  lim_inf = dados2[0]

#limite superior
sup = max(dados)
inf = min(dados)
if (sup <= inter):
  lim_sup = sup
else:
  dados2.pop(n-1)
  lim_sup = dados2[n-2]

print("Limite inferior: " + str(int(lim_inf)))
print("1o quartil: " + str(int(prim_quart)))
print("Mediana: " + str(int(mediana)))
print("3o quartil: " + str(int(terc_quart)))
print("Limite superior: " + str(int(lim_sup)))