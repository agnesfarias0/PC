n = int(input("Digite um número inteiro positivo: "))
print("Sequência de Collatz para " + str(n) + ": ")

print(str(int(n)) + " -> ", end="")
while n != 1:
  if (n%2 == 0):
    n = (n/2)
  else:
    n = (n*3)+1
  if n != 1:
    print(str(int(n)) + " -> ", end="")
  else:
    print(str(int(n)))