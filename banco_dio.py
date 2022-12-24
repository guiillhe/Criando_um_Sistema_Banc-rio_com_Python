#depósitos operações com os valores guardados em  uma variável
#max 3 saques de 500 diario
menu = """
[D] - Depositar
[S] - Sacar
[E] - Extrato 
[Q] - Sair
"""
saldo = 100
transacao = 0
depositos = 0
saques = 0
vdep = 0
vsaq = 0
extrato = []
while True:
  opcao = input(menu)
  opcao = opcao.upper()
  if opcao == "D":
    transacao = int(input("Digite o valor a ser depositado : "))
    if transacao > 0:
      depositos +=1
      vdep += transacao 
      DepName = "Deposito",depositos
      addExtrato = "Deposito {depositos}: R${transacao:.2f}".format(depositos =  depositos, transacao =  transacao)
      extrato.append(addExtrato)
      saldo = saldo + transacao
      print("Seu novo saldo é de : R${saldo:.2f}".format(saldo = saldo))
    elif transacao < 0:
      print("O valor precisa ser um valor inteiro e positivo")


    
  elif opcao == "S":
    if saques <3:
      transacao = int(input("Digite o valor a ser sacado : "))
    if saques == 3:
      print("Limite de saques diários atingidos, volte amanhã")
    elif transacao > 0 and saques <=3 and transacao <501 and saldo>transacao:
      saques +=1
      vsaq += transacao
      SaqName = "Saque ",depositos
      addExtrato = "Saque {saques}: R${transacao:.2f}".format(saques =  saques, transacao =  transacao)
      extrato.append(addExtrato)
      saldo = saldo - transacao
      print("Voce ainda pode faxer mais : ",(3-saques), " saques" )
      print("Seu novo saldo é de : R${saldo:.2f}".format(saldo = saldo))
    elif transacao > 500:
      print("O valor máximo do saque é de R$500,00")
    elif transacao> saldo:
      print("Saldo insuficiente, não foi possível realizar o saque, seu saldo é de : R${saldo:.2f}".format(saldo=saldo))
    
      print("Seu limite de saques diários foi alcançada, volte amanhã")
  elif opcao == "E":
    print("Movimentações:")
    for move in extrato:
      print(move)
    
    print("Suas movimentações de hoje foram: \n{saques} saques no valor de R${vsaq:.2f}. \n{depositos} depósitos no valor de R${vdep:.2f} .\nSeu saldo é de R${saldo:.2f}".format(saldo= saldo, saques= saques, depositos= depositos, vsaq =vsaq, vdep=vdep))
  
  elif opcao == "Q":
    print("Obrigado por ser nosso cliente")
    break
  else:
    print("Opção inválida, por favor digite uma opção válida em caixa alta.")
