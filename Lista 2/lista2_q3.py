dias = int(input("Digite um número: "))

semanas = int(dias/7)
resto = int(dias%7)

if (dias == 0):
  print(str(dias) + " dias equivale à nenhum dia.")

elif (dias >= 1):
  
  if (semanas == 0):
    print(str(dias) + " dias equivale à " + str(dias) + " dias!")
  
  elif (semanas == 1 and resto == 0):
    print(str(dias) + " dias equivalem à " + str(semanas) + " semana!")
    
  elif (semanas > 1 and resto == 0):
    print(str(dias) + " dias equivalem à " + str(semanas) + " semanas!")
  
  elif (semanas == 1 and resto == 1):
    print(str(dias) + " dias equivalem à " + str(semanas) + " semana e " + str(resto) + " dia!")

  elif (semanas == 1 and resto > 1):
    print(str(dias) + " dias equivalem à " + str(semanas) + " semana e " + str(resto) + " dias!")

  elif (semanas > 1 and resto == 1):
    print(str(dias) + " dias equivalem à " + str(semanas) + " semanas e " + str(resto) + " dia!")

  elif (semanas > 1 and resto > 1):
    print(str(dias) + " dias equivalem à " + str(semanas) + " semanas e " + str(resto) + " dias!")