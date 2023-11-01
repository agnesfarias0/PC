def imprimePartes(lista,sep):
  
  lista_temp = []
  new_list = []
  
  for i in range(len(lista)):
    if lista[i] != sep:
      lista_temp.append(lista[i])
    else:
      if len(lista_temp) > 0:
        new_list.append(lista_temp) # adiciona à new_list somente quando há elementos em lista_temp
      lista_temp = []
  
  if len(lista_temp) > 0: #adiciona o último intervalo caso exista
    new_list.append(lista_temp)
  
  if new_list != []:
    for i in new_list:
      print(*i, end="")
      print()
  else:
    return print("Nenhuma")

lista = []
new_list = []

n = int(input("N? "))
print("Qual a sequência?")

for i in range(n):
  lista.append(int(input()))

sep = int(input("Qual o elemento separador?"))

print("Sequências resultantes:")
imprimePartes(lista,sep)