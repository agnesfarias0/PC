newlist = []

n1 = int(input("n1? "))
n2 = int(input("n2? "))

if (n1 <= 1 or n2 <= 1):
  print("Entre com valores maiores que 1...")
  exit()

lista = [n1,n2]

if (lista[0] > lista[1]):
  lista.sort()

num = lista[0]

while (num < lista[1]): #loop 1 incrementa o n1 até o n2-1
  
  if ((num % 2) != 0): #se for ímpar, entrará no if
    
    div = 3
    
    while (div < num): #loop 2 que incrementa divisor até num-1
      if (num % div == 0): #se for divisível, entrará no if, para e armazena numero
        newlist.append(num)
        break
      div = div + 1 #se não for divisível, só incrementa o divisor e checa novamente no loop 2
            
  num = num+1 #se não for ímpar, incrementa o n1 e checa novamente no loop 1

print("números ímpares não primos [", lista[0], "-", lista[1], "]: ", newlist)