n1 = int(input("Digite n1: "))
n2 = int(input("Digite n2: "))

if n1>n2:
  aux = n1
  n1 = n2
  n2 = aux

for i in range(n1,n2+1): 
  
  print("=-=-=-= Tabuada de " + str(n1) + " =-=-=-=")
  
  for j in range(10):
    print(str(n1) + " x " + str(j+1) + " = " + str(n1*(j+1)))
  
  n1 = n1 + 1