def principal():
  
  v_saldo = 1000
  
  while True:
    opcao = exibeOpcoes()
    if opcao == 4:
      print("Obrigada por usar os serviços do Caixa Eletrônico")
      break
    else:
      v_saldo = processaOpcoes(opcao,v_saldo)

def exibeOpcoes():
  print("")
  print("Qual operacao voce deseja realizar?")
  print("1 - SAQUE")
  print("2 - DEPOSITO")
  print("3 - SALDO")
  print("4 - SAIR")
  opcao = int(input("Escolha: "))
  return opcao

def processaOpcoes(opcao,v_saldo):
  if opcao == 1:
    return saque(v_saldo)
  elif opcao == 2:
    return deposito(v_saldo)
  elif opcao == 3:
    return saldo(v_saldo)

#---OPCAO 1: SAQUE---#  
def saque(v_saldo):
  v_saque = float(input("Qual o valor do saque? "))
  if v_saque <= v_saldo:
    v_saldo = v_saldo - v_saque
    print("Saque autorizado.")
    saldo(v_saldo)
  else:
    print("Saldo insuficiente.")
  return v_saldo
  
#---OPCAO 2: DEPOSITO---#
def deposito(v_saldo):
  v_deposito = float(input("Qual o valor a ser depositado? "))
  if v_deposito > 0:
    v_saldo = v_saldo + v_deposito
    print("Depósito realizado.")
    saldo(v_saldo)
  else:
    print("Valor inválido.")
  return v_saldo
  
#---OPCAO 3: SALDO---#
def saldo(v_saldo):
  print("Seu saldo atual é de " + str(v_saldo))
  return v_saldo

principal()