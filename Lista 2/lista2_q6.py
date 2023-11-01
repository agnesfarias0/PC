n1 = int(input("Digite o Primeiro número: "))
n2 = int(input("Digite o Segundo número: "))
op = input("Digite a operação a realizar [+,-,* ou /]: ")

print("")

print("Saída:")

if (op == "+"):
  print("A soma de " + str(n1) + " + " + str(n2) + " é: " + str(n1+n2))
elif (op == "-"):
  print("A subtração de " + str(n1) + " - " + str(n2) + " é: " + str(n1-n2))
elif (op == "*"):
  print("O produto de " + str(n1) + " * " + str(n2) + " é: " + str(n1*n2))
elif (op == "/"):
  print("O quociente de " + str(n1) + "/" + str(n2) + " é: " + str(n1/n2))
else:
  print("Operação inválida!")