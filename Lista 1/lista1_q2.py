logA = 2
logB = 2

while (logA != 0 and logA != 1):
  logA = int(input('Valor lógico de A eh: '))
  if (logA != 0 and logA != 1):
    print("Valor inválido! Entre com 1 ou 0...")

while (logB != 0 and logB != 1):
  logB = int(input('Valor lógico de B eh: '))
  if (logA != 0 and logA != 1):
    print("Valor inválido! Entre com 1 ou 0...")

print("A AND B eh: " + str(bool(logA and logB)))
print("A OR B eh: " + str(bool(logA or logB)))
