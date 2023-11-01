texto = input("texto? ")
i1 = int(input("i1? "))
i2 = int(input("i2? "))
aux = 0

if (i1 > i2):
  aux = i1
  i1 = i2
  i2 = aux

if (i1 > len(texto) or i2 > len(texto)):
  print("os valores devem ser menores do que o tamanho do texto, nesse caso " + len(texto))

else:

  print("Partes")
  print("Parte 1: " + texto[0:int(i1)])
  print("Parte 2: " + texto[0:int(i2)])
  print("Parte 3: " + texto[int(i1):int(i2)])
  print("Parte 4: " + texto[int(i1):])
  print("Parte 5: " + texto[int(i2):])