n = int(input("Qual o N? "))
numeros = []
print("Digite os valores:")
for i in range(n):
  i = input()
  numeros.append(i)

op = int(input("Qual a op? "))
a = int(input("Qual o A? "))
b = int(input("Qual o B? "))

if op == 0:
  print(str(numeros[a-1]) + " + " + str(numeros[b-1]) + " = " + str(int(numeros[a-1])+int(numeros[b-1])))
elif op == 1:
  print(str(numeros[a-1]) + " * " + str(numeros[b-1]) + " = " + str(int(numeros[a-1])*int(numeros[b-1])))