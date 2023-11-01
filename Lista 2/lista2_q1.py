n1 = int(input("n1? "))
n2 = int(input("n2? "))
n3 = int(input("n3? "))

lista = [n1, n2, n3]

if (lista[0] == lista[1] and lista[1] == lista[2]): #se todos são iguais
  print("todos são iguais a " + str(lista[0]))
  
else:
  
  maior = max(lista)
  menor = min(lista)
  lista.remove(maior)
  lista.remove(menor)
  
  if (lista[0] == menor): #se há 2 números iguais menores que o terceiro termo
    print("maior: " + str(maior))
    print("menores: " + str(menor))
    print("não há elementos do meio")
    
  elif (lista[0] == maior): #se há 2 números iguais maiores que o terceiro termo
    print("maiores: " + str(maior))
    print("menor: " + str(menor))
    print("não há elementos do meio")
    
  else: #se há 3 números diferentes
    print("maior: " + str(maior))
    print("menor: " + str(menor))
    print("meio: " + str(lista[0]))