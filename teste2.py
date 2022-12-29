import textwrap
numConta = 0
contas = {
	numConta:{
	    'cpf': 123,
		"nome": "nome",
		"endereco":{
			'logradouro': 'logradouro',
			'numero': 213,
			'bairro':'bairro',
			'cidade': 'cidade',
			'estado': 'PR',
			'cep': '86375-000',
			},
		'telefone': '(xx)99999-9999',
		}
	}
def menu():
	menu = """
========MENU==========
=[NU] - Novo Cliente =
=[NC] - Nova conta   =
=[D ] - Depositar    =
=[S ] - Sacar        =
=[E ] - Extrato      =
=[Q ] - Sair         =
======================
"""
	saldo = 100
	transacao = 0
	depositos = 0
	saques = 0
	vdep = 0
	vsaq = 0
	extrato = []


	return input(textwrap.dedent(menu))



def main():
    global numConta
    opcao = menu()
    opcao = opcao.upper()
    if opcao == "NU":
       bolCPF= False
       numConta += 1
       
       
       while bolCPF == False:
           cpf = input("Digite o seu CPF (apenas numeros): ")
           for conta in contas:
               if contas[conta]["cpf"] == int(cpf):
                   print("CPF já cadastrado")
               else:
                   bolCPF = True
                   
                
                
            
                    
            
       #Criando o padrão para a conta nova 
       contas.setdefault(
           numConta,{
               'cpf': 123,
               "nome": "nome",
               "endereco":{
                   'logradouro': 'logradouro',
                   'numero': 0,
                   'bairro':'*',
                   'cidade': '*',
                   'estado': '*',
                   'cep': '*',
                   },
                'telefone': '(xx)99999-9999',
            }
		)     
       contas[numConta]["cpf"] =  cpf
       nome = input("Digite seu nome completo: ")
       contas[numConta]["nome"]=  nome
       #capturando o endereço 
       rua = input("Digite O nome da sua Rua/Av/Travessa \nExemplo: Rua, x ou Av, Y ou Travessa Z:  ")
       contas[numConta]["endereco"]['logradouro']= rua
       numero = input("Digite o numero da sua casa :  ")
       contas[numConta]["endereco"]['numero'] = numero
       bairro = input("Digite o seu bairro : ")
       contas[numConta]["endereco"]['bairro'] = bairro
       cidade =  input("Digite o nome da sua cidade : ")
       contas[numConta]["endereco"]['cidade'] = cidade
       estado = input("Digite a sigla do seu estado \nExemplo: PR, SC, SP, etc  : ")
       contas[numConta]["endereco"]['estado'] = estado
       cep = input("Digite seu cep \nEcemplo:86500-000:  ")
       contas[numConta]["endereco"]['cep'] = cep
       telefone = input("Digite o numero do seu telefone : ")
       contas[numConta]["telefone"] = telefone
       
       
       
       
       
       for conta, dados in contas.items():
           print(conta,dados)
		


main()