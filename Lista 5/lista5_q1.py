def encripta(texto):
  
  int1 = ["a","b","c","d","e"]
  int2 = ["f","g","h","i","j"]
  int3 = ["k","l","m","n","o"]
  int4 = ["p","q","r","s","t","u","v","w","x","y","z"]
  
  list(texto) #separa o texto em uma lista
  vetor = []
  
  for i in texto: 
    vetor.append(i) #armazena cada caractere do texto em um espaço do vetor
  
  for i in range(len(vetor)):
    if vetor[i] in int1:
      vetor[i] = "1"
    elif vetor[i] in int2:
      vetor[i] = "2"
    elif vetor[i] in int3:
      vetor[i] = "3"
    elif vetor[i] in int4:
      vetor[i] = "4"
    else:
      vetor[i] = "5"

  return vetor

texto = input("Digite o texto: ").lower()
vetor = encripta(texto)

print("Encriptado: ", *vetor, sep="")