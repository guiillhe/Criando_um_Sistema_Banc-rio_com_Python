print("""=====================
=== Exercício 001 ===
""")
frase = "Olá mundo!!"
print(frase)
print("=====================")

print("""=====================
=== Exercício 002 ===
""")
nome= input("Qual é o seu nome? ")
print(f"Prazer em conhecê-lo {nome}")


print("""=====================
=== Exercício 003 ===
""")
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
soma = n1+n2
print(f"A soma entre {n1} e {n2} é {soma}")
print("=====================")

print("""=====================
=== Exercício 004 ===
""")
texto = input("Digite algo: ")

print("O tipo primitivo desse valor é ",type(texto))
print("Contem apenas espaços? ", "Sim " if texto.isspace() == True else "Não")#ver
print("É um número? ","Sim " if texto.isnumeric() == True else "Não")
print("É Alfabético? ","Sim " if texto.isalpha() == True else "Não" )
print("É alfanumérico? ", "Sim " if texto.isalnum() == True else "Não")#ver 
print("Está em maiusculas? ", "Sim " if texto.isupper() == True else "Não")
print("Está em minusculas? ", "Sim " if texto.islower() == True else "Não")
print("Está Capitalizada? ", "Sim " if texto.istitle() == True else "Não")
print("=====================")


print("""=====================
=== Exercício 005 ===
""")
texto = int(input("Digite um número: "))
print(f"Analisando o número {texto}, o seu antecessor é {texto-1} e o seu sucessor é {texto+1}")
print("=====================")

print("""=====================
=== Exercício 006 ===
""")
num = int(input("Digite um número: "))
print(f"""
O dobro de {num} é:           {num*2}.
O numero {num} ao quadrado é: {num**2}.
A raiz quadrada de {num} é:   {num**(1/2):.2f}.
""")
print("=====================")

print("""=====================
=== Exercício 007 ===
""")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a Segunda nota: "))
media = (nota1+nota2)/2
print(f"A média entre {nota1} e {nota2} é {media:.1f}")
print("=====================")

print("""=====================
=== Exercício 008 ===
""")
distancia = float(input("digite uma distândia em metros: "))

print(f"""
A Distância equivale a: 
{distancia/1000}Km
{distancia/100}Hm
{distancia/10}dm
{distancia*100}cm
{distancia*1000}mm

""")
print("=====================")

print("""=====================
=== Exercício 09 ===
""")
base = int(input("Digite um número para saber a sua tabuada: "))
print("="*5,f"Tabuada do {base:2}","="*5)
for i in range(11):
    print("="*5,f"{base:2} X {i:2} = {base*i:3}","="*5)
    
print("="*25)

print("""=====================
=== Exercício 010 ===
""")
reais = float(input("Quanto Você tem na carteira? R$"))
dolar = 5.11
print(f"Com esse R${reais}(Reais) você compra aproximadamente ${reais/dolar:.2f}(dolares)")

print("=====================")

print("""=========================
===== Exercício  11 =====
=========================
""")
largura = float(input("Qual é a largura da parede em metros? "))
altura = float(input("Qual é a altura da parede em metros? "))
medida = largura * altura
print(f"""Sua parede com {largura} x {altura} tem:
{medida} metros quadrados 
Vai precisar de {medida/2:.2f} litros de tinta para a pintura""")
print("="*25)

print("""=========================
===== Exercício  12 =====
=========================
""")
preco = float(input("Qual é o preço do produto? R$"))
desconto = preco *0.95

print(f""" O preço do produto é: R${preco:.2f}.
E com um desconto fica: R${desconto:.2f}.""")

print("="*25)

print("""=========================
===== Exercício  13 =====
=========================
""")
salario = float(input("Qual é o salário a ser reajustado? R$"))
porcentagem = float(input("Qual é a porcentagem de aumento? "))
reajuste = porcentagem/100+1
print(f"""O salário de R${salario}, com o valor do reajuste, sobe para  para R${salario*reajuste:.2f} a partir do próximo mes.""" )


print("="*25)

print("""=========================
===== Exercício  14 =====
=========================
""")
temperatura = float(input("Qual é a temperatura atual em C°"))
print(f'A temperatura de {temperatura}C° equivale a {(temperatura*(9/5))+32}')


print("="*25)

print("""=========================
===== Exercício  15 =====
=========================
""")
dias = int(input("Qual é a quantidade de dias foi usado o  carro? "))
kms = int(input("Qual é a quantidade de kms rodados? "))
total = (dias*60) +(kms+0.15)
print(f'''
O valor pelo uso de {dias}dias  e {kms}Kms Rodados é:
R${total:.2f}(Reais)''')


print("="*25)

print("""=========================
===== Exercício  16 =====
=========================
""")
numero = float(input("Qual é a quantidade de dias foi usado o  carro? "))
inteiro = int(numero)

print(f"A porção inteira do {numero} é igual a {inteiro}")

print("="*25)

print("""=========================
===== Exercício  17 =====
=========================
""")
co = float(input("Qual é a medida do cateto oposto? "))
ca = float(input("Qual é a medida do cateto adjascente? "))
hip= (((co**2)+(ca**2))**(1/2))
print(f'A hipotenusa medirá {hip:.2f}')

print("="*25)

#Import para o exercício 18
import math
print("""=========================
===== Exercício  18 =====
=========================
""")
angulo = float(input("Qual é o angulo desejado? "))

print(f'O angulo de {angulo} tem um seno de {math.sin(math.radians(angulo)):.2f}')
print(f'O angulo de {angulo} tem um coseno de {math.cos(math.radians(angulo)):.2f}')
print(f'O angulo de {angulo} tem uma tangente de {math.tan(math.radians(angulo)):.2f}')


print("="*25)
#import 
import random
print("""=========================
===== Exercício  19 =====
=========================""")


aluno1 = input("Qual é o primeiro aluno? ")
aluno2 = input("Qual é o segundo aluno? ")
aluno3 = input("Qual é o terceiro aluno? ")
choice = random.randint(1, 3)

if choice == 1:
    print(f"O aluno sorteado foi o {aluno1}")
elif choice == 2:
    print(f"O aluno sorteado foi o {aluno2}")
elif choice == 3:
    print(f"O aluno sorteado foi o {aluno3}")
        



print("="*25)
#import 
import random
print("""=========================
===== Exercício  20 =====
=========================""")


aluno1 = input("Qual é o primeiro aluno? ")
aluno2 = input("Qual é o segundo aluno? ")
aluno3 = input("Qual é o terceiro aluno? ")
aluno4= input("Qual é o terceiro aluno? ")
lista = [aluno1,aluno2,aluno3,aluno4]
random.shuffle(lista)

print(f"""A ordem de apresentação é:
Primeiro: {lista[0]}
Segundo: {lista[1]}
Terceiro: {lista[2]}
Quarto: {lista[3]}
""")




print("="*25)

print("""=========================
===== Exercício  21 =====
=========================""")
#Pulei pra fazer em casa

print("="*25)

print("""=========================
===== Exercício  22 =====
=========================""")


nome = input("Qual seu nome completo? ").strip()

print(f"""Analisando seu nome...
Seu nome em maiusculas: {nome.upper()}
Seu nome em minusculas: {nome.lower()}
Seu nome tem {len(nome)- nome.count(' ')} letras.
Seu primeiro nome é {nome[0:nome.index(" ")]} e tem {len(nome[0:nome.index(' ')])} letras.
""")





print("="*25)

print("""=========================
===== Exercício  23 =====
=========================""")

num = int(input('Digite um número inteiro de 0 a 9999: '))

if num >=0 and num <=9999:
    print(f'Unidade {num//1%10}' )
	print(f'Dezena {num//10%10}' )
	print(f'Centena {num//100%10}' )
	print(f'Milhar {num//1000%10}' )
else:
    print("Digite um número válido")




print("="*25)


print("""=========================
===== Exercício  24 =====
=========================""")

cidade = input('Digite a cidade que você nasceu: ').strip()
cidade = cidade.split()

if cidade[0].upper() == 'SANTO':
    print(True)
else:
    print(False)






print("="*25)


print("""=========================
===== Exercício  25 =====
=========================""")

nome = input('Digite o seu nome: ').strip()
resposta = "Sim" if nome.upper().__contains__("SILVA") else "Não"
print(f'Seu nome contem silva? {resposta}')





print("="*25)

print("""=========================
===== Exercício  26 =====
=========================""")

frase = input('Digite uma frase: ').strip()

print(f'A letra A aparece {frase.upper().count("A")} vezes nessa frase')
primeira = frase.upper().find("A")
print(f'A primeira aparição ocoore na {primeira+1}ª posição' )
ultima = frase.upper().rfind("A")
print(f'A ultima aparição ocorre na {ultima+1}ª posição')


print("="*25)

print("""=========================
===== Exercício  27 =====
=========================""")

nome = input('Digite seu nome completo: ').strip()
nome = nome.split()

print(f'''Olá usuário!!
Prazer em conhecê-lo!
Seu primeiro nome é {nome[0]}
Seu ultimo nome é {nome[-1]}
''')





print("="*25)


import random 
print("""=========================
===== Exercício  28 =====
=========================""")

print("\033[7;33;46m-=-\033[m"*17)
print("Vou pensar em umnumero entre 0 e 5. Tente adivinhar")
print("\033[7;33;46m-=-\033[m"*17)

numero = input("Qual escolha um numero? ")
choice = random.randint(0, 5)
print("Parabéns Você acertou!!!" if numero ==choice else f"Não foi dessa vez o numero era {choice}")





print("="*25)


print("""=========================
===== Exercício  29 =====
=========================""")


print("-=-=-=-=- RADAR-=-=-=-=-")
velocidade = int(input("Qual é a velocidade do carro? "))
velocidademax = 80
multa = ((velocidade-velocidademax)*7)+100
if velocidade <= velocidademax:
    print(f'Tenha um bom dia, Dirija com segurança')
else:
    print(f'''Você excedeu o limite de velocidade de {velocidademax}km/h
Você foi multado em R${multa:.2f}  ''')





print("="*25)

print("""=========================
===== Exercício  30 =====
=========================""")


print("-=-=-=-=- Par ou impar-=-=-=-=-")
numero = int(input("Digite um  número inteiro: "))
resto = numero%2
if resto == 0:
    print(f'O numero {numero} é Par')
else:
    
    print(f'O numero {numero} é Impar')


print("="*25)

print("""=========================
===== Exercício  31 =====
=========================""")


print("-=-=-=-=- Preço da passagem-=-=-=-=-")
numero = int(input("Qual é a distancia da viagem?: "))

if numero <= 200:
    print(f'O preço da passagem é R${numero*0.5}')
else:
    
    print(f'O preço da passagem é R${numero*0.45}')


print("="*25)

import datetime
print("""=========================
===== Exercício  32 =====
=========================""")


print("-=-=-=-=- Ano bissexto -=-=-=-=-")
ano = int(input("Qual é o ano a ser analizado?(digite 0 para o ano atual): "))
if ano == 0:
   ano = datetime.datetime.now().year
    
if ano%4 == 0 and  ano%100 !=0 or ano%400 ==0:
    print(f"O ano {ano} é bissexto ")
else:
    print(f'O ano {ano} não é bissexto')  
    


print("="*25)

print("""=========================
===== Exercício  33 =====
=========================""")


print("-=-=-=-=- maior e menor -=-=-=-=-")
n1 = int(input("Digite o primeiro numero "))
n2 = int(input("Digite o segundo numero "))
n3 = int(input("Digite o terceiro numero "))

lista = [n1,n2,n3]
maior = max(lista)
menor = min(lista)
if maior == menor:
    print("Todos os números são iguais")
else:
    print(f'''O maior valor digitado é: {maior}
O menor valor digitado é: {menor}''')
print("="*25)

print("""=========================
===== Exercício  34 =====
=========================""")


print("-=-=-=-=- Reajuste salarial -=-=-=-=-")
salario = float(input("Qual é o salário do colaborador? "))


if salario <= 1250:
    print(f"O novo salário será de R${salario*1.15:.2f}")
else:
        print(f"O novo salário será de R${salario*1.1:.2f}")
print("="*25)

print("""=========================
===== Exercício  35 =====
=========================""")


print("-=-=-=-=- Triangulos -=-=-=-=-")
l1 = float(input("Qual é o tamanho do primeiro lado? "))
l2 = float(input("Qual é o tamanho do segundo lado? "))
l3 = float(input("Qual é o tamanho do terceiro lado? "))


if (l1+l2)>l3 and (l2+l3)>l1 and (l3+l1) > l2:
    print("As retas acima PODEM formar um triangulo")
else:
    print("As retas acima NÃO PODEM formar um triangulo")
print("="*25)

print("""=========================
===== Exercício  36 =====
=========================""")


print("-=-=-=-=- Empréstimo simples -=-=-=-=-")
valor = float(input("Qual é o valor do imóvel? R$"))
salario = float(input("Qual é o valor do seu salário? R$"))
tempo = int(input("Em quantos anos você quer pagar? "))
parcela = valor/(tempo*12)
limite = salario *0.3

print(f"Para pagar uma casa de R${valor} em {tempo} anos será necessário uma parcela de R${parcela:.2f}")
if parcela>limite:
    print("Desculpe, mas o Empréstimo NEGADO")
    print(f"Seu limite é de R${limite}")
else:
    print("Parabéns, seu limite foi aprovado")
print("="*25)

print("""=========================
===== Exercício  37 =====
=========================""")


#Apaguei sem querer

print("""=========================
===== Exercício  38 =====
=========================""")


print("-=-=-=-=- Comparando números -=-=-=-=-")
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1>n2:
    print("O primeiro número é maior")
elif n2>n1:
    print("O segundo número é maior")
else:
    print("Os dois números são iguais")

print("="*25)

import datetime
print("""=========================
===== Exercício  39 =====
=========================""")


print("-=-=-=-=- Alistamento militar -=-=-=-=-")
anonascimento = int(input("Digite o ano do seu nascimento: "))
anoatual = datetime.datetime.now().year
idade = anoatual-anonascimento
multa = (idade-18)*200
if idade < 18:
    print(f"""Você ainda não pode se alistar
Voce tem fará {idade} anos em {anoatual}
Faltam {18-idade} anos para voce se alistar 
Volte no ano de {18-idade+anoatual}""")
elif idade == 18:
    print("""Voce está no ano do seu alistamento
Vá até o posto de alistamento mais próximo da sua casa""")
else:
    print(f"""Você passou do ano do seu alistamento
Era pra você ter se alistado em {anoatual-idade+18}
Você pagará uma multa de R${multa:.2f}
""")

print("="*25)

print("""=========================
===== Exercício  40 =====
=========================""")


print("-=-=-=-=- Média escolar -=-=-=-=-")
n1 = float(input("Digite a primeira nota: " ))
n2 = float(input("Digite a segunda nota: " ))
n3 = float(input("Digite a terceira nota: " ))
n4 = float(input("Digite a quarta nota: " ))
media = (n1+n2+n3+n4)/4
if media < 5:
    print(f"Sua média foi de {media:.2f}, você está reprovado")
elif media >=5 and media <7:
    print(f"Sua média foi de {media:.2f}, você está de recuperação")
elif media >=7:
    print(f"Sua média foi de {media:.2f}, Parabéns!!! você está aprovado")
    
print("="*25)

print("""=========================
===== Exercício  41 =====
=========================""")


print("-=-=-=-=- Categorias  -=-=-=-=-")
nascimento  = int(input("Digite o ano de nascimento do atleta: " ))
anoatual = datetime.datetime.now().year
idade = anoatual-nascimento)

if idade < 9:
    print(f"Sua idade é  {idade}, você está na categoria mirim")
elif idade < 15:
    print(f"Sua idade é  {idade}, você está na categoria infantil")

elif idade<20:
    print(f"Sua idade é  {idade}, você está na categoria júnior")
elif idade<26:
    print(f"Sua idade é  {idade}, você está na categoria Sênior")
elif idade > 25:
    print(f"Sua idade é  {idade}, você está na categoria master")
print("="*25)


print("""=========================
===== Exercício  42 =====
=========================""")


print("-=-=-=-=- Triangulos 2.0 -=-=-=-=-")
l1 = float(input("Qual é o tamanho do primeiro lado? "))
l2 = float(input("Qual é o tamanho do segundo lado? "))
l3 = float(input("Qual é o tamanho do terceiro lado? "))
triangulo =(l1+l2)>l3 and (l2+l3)>l1 and (l3+l1) > l2

if triangulo == False :
    print("As retas acima NÃO PODEM formar um triangulo")
elif triangulo == True and l1 == l2 and l2==l3:
    print("As retas acima formam um triangulo equilátero")
elif triangulo == True and l1 == l2 and l2==l3:
    print("As retas acima formam um triangulo retangulo")
elif triangulo == True and l1 != l2 and l2!=l3 and l1!=l3:
    print("As retas acima formam um triangulo Escaleno")
elif triangulo == True and l1 == l2 or l2==l3 or l1==l3:
    print("As retas acima formam um triangulo Isóceles")
print("="*25)

print("""=========================
===== Exercício  43 =====
=========================""")


print("-=-=-=-=- Na medida certa -=-=-=-=-")
peso = float(input("Qual é o seu peso? Kg"))
altura = float(input("Qual é a sua altura em metros?"))
imc = peso/(altura**2)

if imc<18.5:
    print(f'''Seu imc é {imc:.2f}.
Você está abaixo do peso''')
elif imc < 25:
    print(f'''Seu imc é {imc:.2f}.
Parabéns, você está no peso ideal''')
elif imc < 30:
    print(f'''Seu imc é {imc:.2f}.
Cuidado você está com sobrepeso''')
elif imc < 40:
    print(f'''Seu imc é {imc:.2f}.
Cuidado você está obeso''')
else:
    print(f'''Seu imc é {imc:.2f}.
Cuidado você está obesidade mórbida''')
    

print("="*25)

print("""=========================
===== Exercício  44 =====
=========================""")


print("-=-=-=-=- Gerenciador de compras -=-=-=-=-")
valor = float(input("Qual é o valor do produto? "))
pagamento = int(input('''Forma de pagamento:
[1] – à vista dinheiro: 10% de desconto
[2]– à vista no cartão: 5% de desconto
[3]– em até 2x no cartão: preço formal 
[4]– 3x ou mais no cartão: 20% de juros (max 10)
Sua escolha: '''))

match pagamento:
    case 1:
         print(f'''A vista em dinheiro, desconto 10%:
O valor do produto, com o desconto fica em: R${valor*0.9:.2f}''')
    case 2:
        print(f'''A vista no cartão de crédito, desconto 5%: 
O valor do produto, com o desconto fica em: R${valor*0.95:.2f}''')
    case 3:
        print(f'''O valor em duas vezes no cartão fica:
Duas parcelas iguais de R${valor/2:.2f}''')
    case 4:
        parcelas = int(input("Quantas parcelas? "))
        valor = valor*1.2
        if 2 < parcelas < 11:
            print(f'''O valor será  parcelado em {parcelas}vezes:
Com os juros o valor fica R${valor:.2f}.
Dividido em {parcelas} parcelas iguais de {valor/3:.2f}''' )
        else:
            print('''Quantidade de parcelas fora  do permitido pelo sistema
Favor escolher um número entre 3 e 10''')
    case _:
        print("valor inválido")

print("="*25)

import random
print("""=========================
===== Exercício  45 =====
=========================""")
print("-=-=-=-=- Jokenpo -=-=-=-=-")
itens = ('Pedra','Papel','Tesoura')
eu = int(input('''Vamos começar o jogo escolha:
[1] - Pedra
[2] - Papel
[3] - Tesoura 
Sua jogada: '''))-1
pc = random.randint(0,2)

print(f'''A Sua jogada foi {itens[eu]}.
A jogada do computador foi {itens[pc]}.''')
if eu == pc:
    print ("EMPATE")
elif (eu == 0 and pc == 1) or (eu == 1 and pc == 2) or (eu == 2 and pc == 0):
    print (f'{itens[eu]} perde para {itens[pc]} VOCÊ PERDEU!"')
else:
    print (f'{itens[eu]} ganha de {itens[pc]} VOCÊ GANHOU')
    
print("="*25)

import time 
print("""===== Exercício  46 =====
=========================""")
print("-=-=-=-=- Ano novo -=-=-=-=-")
print("Começando a contagem regressiva...")
time.sleep(1)
for i in range(10,0,-1):
    time.sleep(1)
    print(f'{i:2}...')

print("="*25)

print("""===== Exercício  47 =====
=========================""")
print("-=-=-=-=- Números pares -=-=-=-=-")
numeroInicial = int(input("Digite o numero para começar a contagem: "))
numeroFinal = int(input("Digite o numero para terminar a contagem: "))

if numeroInicial %2 ==0:
    pass
else:
    numeroInicial +=1
for n in range(numeroInicial,numeroFinal+1,2):
    print(n)
    

print("="*25)


print("""===== Exercício  48 =====
=========================""")
print("-=-=-=-=- Números pares -=-=-=-=-")
soma = 0
quantidade = 0

for i in range(1,501):
    if i %2 ==0:
        if i %3 ==0:
			quantidade+=1
            soma += i
            
print(f'A soma entre os {quantidade} numeros pares\ndivisiveis por três entre 1 e 500 é {soma}')    


print("="*25)

print("""===== Exercício  49 =====
=========================""")
print("-=-=-=-=- Números pares -=-=-=-=-")

#Já fiz desse jeito no 9 


print("="*25)


print("""===== Exercício  50 =====
=========================""")
print("-=-=-=-=- Somar pares digitados  -=-=-=-=-")
cont =0
soma = 0
for i in range(6):
    numero= int(input(f"Digite o {i+1}º Número "))
    if numero %2 ==0:
        soma += numero
        cont +=1
    
print(f'A soma dos {cont} números pares digitados é iguam a: {soma}')


print("="*25)

print("""===== Exercício  51 =====
=========================""")
print("-=-=-=-=- 10 primeiros termos da P.A.  -=-=-=-=-")
n1=int(input("Digite o numero que vai iniciar a P.A.: "))
ns=int(input("Digite a razão da  P.A.: "))
for i in range(10):
    print(n1)
    n1+=ns


print("="*25)

print("""===== Exercício  52 =====
=========================""")
print("-=-=-=-=- Primo ou não?.  -=-=-=-=-")

numero = int(input("Digite um numero inteiro para saber se ele é primo: "))
resultado = 0
contagem = 0

for i in range(1,numero+1):
    resultado = numero%i
    if resultado == 0:
        contagem+=1
if contagem == 2:
    print(f'O numero {numero} é primo.')
else:
    print(f'O numero {numero} NÃO é primo.')
    
print("="*25)

print("""===== Exercício  53 =====
=========================""")
print("-=-=-=-=- Detector palindromos  -=-=-=-=-")

frase = str(input("Digite uma frase para testar se é palindromo: "))
fraseTratada = frase.upper().replace(" ","")
reverso = frase.upper().replace(" ","")[::-1]
print(fraseTratada==reverso)
print("="*25)

from datetime import datetime
print("""===== Exercício  54 =====
=========================""")
print("-=-=-=-=- Maioridades  -=-=-=-=-")
anoAtual = datetime.now()
anoAtual = anoAtual.year
maiores =0
menores =0
for i in range(7):
    nascimento = int(input(f"Digite a {i+1}ª data de nascimento: "))
    print(f'Digite a {i+1}ª data de nascimento:{nascimento}')
    if anoAtual-nascimento >17:
        maiores +=1
    else:
        menores +=1
print(f'Ao todos temos {maiores} maiores e {menores} menores de 18 anos' )

print("="*25)

print("""===== Exercício  55 =====
=========================""")
print("-=-=-=-=- Analisador completo  -=-=-=-=-")

maior =0
menor =0
for i in range(6):
    peso = float(input(f"Digite o {i+1}º peso: "))
   
    if peso > maior:
        maior = peso
    if peso < menor or i==0:
        menor = peso
    
print(f'O maior peso é {maior}Kg e o menor peso é {menor}Kg')


print("="*25)

print("""===== Exercício  56 =====
=========================""")
print("-=-=-=-=- Analisador completo  -=-=-=-=-")

maiorIdade = 0
maisVelho = ""
homens = 0
mulheres = 0
nda =0
mulherAbaixo =0
somaIdade =0
for i in range(4):
    nome = str(input(f"Qual é o {i+1}º nome? "))
    idade = int(input("Qual é a idade? "))
    genero = str(input(f"Qual é o gênero? M= masculino F = Feminino")).strip().upper()
    somaIdade += idade
    if genero == "M":
        homens+=1
    elif genero == "F":
        mulheres +=1
    else:
        nda+=1
        
    if maiorIdade < idade and genero == "M":
        maisVelho = nome
    
    if idade>20 and genero == "f":
        mulherAbaixo +=1

print(f"Ao todo são {homens} homens, {mulheres} mulheres {nda} não binários.\nO homem mais velho é {maisVelho} e temos {mulherAbaixo} mulher(es) com menos de 20 anos")
    
        
        
    
print("="*25)

print("""===== Exercício  57 =====
=========================""")
print("-=-=-=-=- Analisador de genero -=-=-=-=-")
flag = False
while flag == False:
    gen = input("Qual é o seu genero? ")
    if gen in "mMFf":
        print("Welcome")
        flag = True
    else:
        print("Valor inválido, o valor deve se M para masculino e F para feminino")
    

print("="*25)

import random 
print("""===== Exercício  58 =====
=========================""")
print("-=-=-=-=- Em qual número estou pensando? -=-=-=-=-")
pc = random.randint(0,10)
tentativas = 1
print(pc)

while True:
    eu = int(input("Qual é o a sua escolha? "))
    if eu == pc:
        print(f'Parabéns você acertou em {tentativas} tentativas')
        break
    elif eu > pc:
        print(f"O valor que eu pensei é menor que {eu}")
        tentativas +=1
    elif eu < pc:
        print(f"O valor que eu pensei é maior que {eu}")
        tentativas +=1
        
        
    

print("="*25)


print("""===== Exercício  59 =====
=========================""")
print("-=-=-=-=- Calculadora simples -=-=-=-=-")


while True:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    operacao = int(input('''Qual operação você deseja fazer?
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Sua escolha: '''))
    if operacao == 1:
        print(f'A soma dos numeros {n1:.2f} e {n2:.2f} é: {n1+n2:.2f}')
    elif operacao == 2:
        print(f' o produto da multiplicação entre {n1:.2f} e {n2:.2f} é : {n1*n2:.2f}')
    elif operacao == 3:
        if n1>n2:
            print(f"O número {n1:.2f} é maior!!!")
        elif n1<n2:
            print(f"O numero {n2:.2f} é maior!!!")
        else:
            print("Os números são iguais")
    elif operacao == 4:
        pass
    elif operacao == 5:
        break
    else:
        print("Opção inválida, tente outra vez!")

        
    

print("="*25)

print("""===== Exercício  60 =====
=========================""")
print("-=-=-=-=- Calculadora Fatorial -=-=-=-=-")

n = int(input("Qual é o número que você deseja fatorar? "))
resultado = 1

print(f'Calculando o fatorial de {n}! ', end='')
while n>0:
    resultado *= n
    print(f'{n}',end='')
    print('x'if n>1 else ' = ', end='')
    n-=1
    
    
print(f"{resultado}")
    

print("="*25)

print("""===== Exercício  61 =====
=========================""")
print("-=-=-=-=- 10 primeiros termos da P.A.  -=-=-=-=-")
n1=int(input("Digite o numero que vai iniciar a P.A.: "))
ns=int(input("Digite a razão da  P.A.: "))
termos = 1
while termos < 11:
    print(f'{n1}',end="")
    print('=> 'if termos < 10 else " FIM", end="")
    n1+=ns
    termos+=1


print('\n',"="*25)

print("""===== Exercício  62 =====
=========================""")
print("-=-=-=-=- 10 primeiros termos da P.A.  -=-=-=-=-")
n1=int(input("Digite o numero que vai iniciar a P.A.: "))
ns=int(input("Digite a razão da  P.A.: "))

escolha ="o"

while escolha[0] != "N":
    termos = 1
    while termos < 11:
        print(f'{n1}',end="")
        print('=> 'if termos < 10 else " FIM", end="")
        n1+=ns
        termos+=1
    escolha = input("\nDeseja continuar? ").upper()
print("Fim da PA")
    


print('\n',"="*25)

print("""===== Exercício  62 =====
=========================""")
print("-=-=-=-=-  termos da P.A.  -=-=-=-=-")
n1=int(input("Digite o numero que vai iniciar a P.A.: "))
ns=int(input("Digite a razão da  P.A.: "))
escolha ="o"
cont =1
total=0
mais =10


while escolha[0] != "N":
    total+=mais
    
    while total >= cont:
        print(f'{n1}',end="")
        print('=> 'if total > cont else " Pausa", end="")
        n1+=ns
        cont+=1
        
    escolha = input("\nDeseja continuar? ").upper()
    if escolha[0] !="N":
        mais = int(input('Deseja ver mais quantos termos? '))
print(f"Fim da PA com {total} termos")



print('\n',"="*25)

print("""===== Exercício  63 =====
=========================""")
print("-=-=-=-=-  termos da P.A.  -=-=-=-=-")
n=int(input("Digite o numero que vai iniciar a P.A.: "))
termo = 0
termoa = 0
termob = 1
print(f"Os {n} primeiros termos da sequencia de Fibonacci são:")
while termo < n:
    if termo ==0:
        print("0", end="")
    elif termo == 1:
        print("1",end="")
    else:
        atual = termoa+termob
        print(atual, end="")
        termoa = termob
        termob = atual
    print("=>"if termo<(n-1) else " FIM", end="")
    termo+=1
    






print('\n',"="*25)print("""===== Exercício  64 =====
=========================""")
print("-=-=-=-=-  termos fibonacci.  -=-=-=-=-")
n=int(input("Quantos termos você quer ver?: "))
termo = 0
termoa = 0
termob = 1
print(f"Os {n} primeiros termos da sequencia de Fibonacci são:")
while termo < n:
    if termo ==0:
        print("0", end="")
    elif termo == 1:
        print("1",end="")
    else:
        atual = termoa+termob
        print(atual, end="")
        termoa = termob
        termob = atual
    print("=>"if termo<(n-1) else " FIM", end="")
    termo+=1 






print('\n',"="*25)

print("""===== Exercício  64 =====
=========================""")
print("-=-=-=-=-  tratando vários valores  -=-=-=-=-")
soma = contador = 0
while True:
    n=int(input("Digite um número: "))
    if n == 999:
        break
    soma +=n
    contador+=1
print(f'Foram digitados {contador} valores resultando em uma soma de {soma}')

print('\n',"="*25)

print("""===== Exercício  65 =====
=========================""")
print("-=-=-=-=-  tratando vários valores  -=-=-=-=-")
soma = maior = menor =contador = 0
while True:
    n=int(input("Digite um número:"))
    if contador ==0:
        maior = menor = n
    else:
        if maior<n:
            maior=n
        elif maior>n:
            pass
        if menor<n:
            pass
        elif menor>n:
            menor = n
    soma +=n
    contador+=1
    continuar = str(input("Você quer continuar? [S/N]")).upper().strip()
    if continuar[0] =="N":
        break

media = soma/contador
print(f'Foram digitados {contador} valores resultando em uma soma de {soma}\nO maior numero digitado foi: {maior}\nO menor número digitado foi: {menor}\nE a média entre eles foi de {media:.2f}')

print('\n',"="*25)


print("""===== Exercício  66 =====
=========================""")
#Já tinha feito assim  no 64 antes por já conhecer o break
print("-=-=-=-=-  tratando vários valores  -=-=-=-=-")
soma = contador = 0
while True:
    n=int(input("Digite um número: "))
    if n == 999:
        break
    soma +=n
    contador+=1
print(f'Foram digitados {contador} valores resultando em uma soma de {soma}')

print('\n',"="*25)

print("""=====================
=== Exercício 67 ===
""")
print("-=-=-=-=-  Tabuada 3.0 -=-=-=-=-")
while True:
    base = int(input("Digite um número para saber a sua tabuada: "))
    if base < 0:
        print("Favor digitar um número positivo!!!")
    else:
        print("="*5,f"Tabuada do {base:2}","="*5)
        for i in range(11):
            print("="*5,f"{base:2} X {i:2} = {base*i:3}","="*5)
        continuar = input("Deseja ver mais uma tabuada? ").upper().strip()
        if continuar[0] =="N":
            break
        elif base>=0:
            print('Então, por favor, ', end='')
print("="*25)

import random
print("""=====================
=== Exercício 68 ===
""")
print("-=-=-=-=-  Vamos Jogar par ou impar  -=-=-=-=-")
contador = 0
while True:
    player = int(input("Escolha seu número: "))
    pc = random.randint(1,2)
    escolha = int(input('''Você quer par ou impar?
[1] - par 
[2] - Impar
Sua escolha: '''))
    res = "Deu par" if (pc+player)%2 ==0 else "Deu impar"
    if (pc+player)%2 ==0 and escolha ==1 or (pc+player)%2 !=0 and escolha ==2:
        contador +=1
        print(f"Você escolheu {player} e eu {pc}.\n{res} você ganhou ")
    else:
        print(f"Você escolheu {player} e eu {pc}.\n{res} você perdeu ")
        break
print(f"Você ganhou {contador} vezes")
    
print("="*25)

print("""===== Exercício  69 =====
=========================""")
print("-=-=-=-=- Analisador completo  -=-=-=-=-")

maiorIdade = 0
maisVelho = ""
homens = 0
mulheres = 0
nda =0
mulherAbaixo =0
somaIdade =0
continuar="Sim"
while True:
    nome = input(f"Qual é o {i+1}º nome? ")
    idade = int(input("Qual é a idade? "))
    genero = input(f"Qual é o gênero? M= masculino F = Feminino").strip().upper()
    somaIdade += idade
    if genero == "M":
        homens+=1
    elif genero == "F":
        mulheres +=1
    else:
        nda+=1
        
    if maiorIdade < idade and genero == "M":
        maisVelho = nome
    
    if idade>20 and genero == "f":
        mulherAbaixo +=1
    continuar = genero = input(f"Deseja continuar? ").strip().upper()
    if continuar[0] =="N":
        break

print(f"Ao todo são {homens} homens, {mulheres} mulheres {nda} não binários.\nO homem mais velho é {maisVelho} e temos {mulherAbaixo} mulher(es) com menos de 20 anos")
'''
A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.
'''
    
    
print("="*25)

print("""===== Exercício  70 =====
=========================""")
print("-=-=-=-=- Analisador de compras-=-=-=-=-")

contador =0
proBarato = ''
pro1000 = 0
valorTotal = 0
valorProBarato = 0
while True:
    continuar = 'x'
    item = input('Digite o nome do item: ')
    valor= float(input('Digite o valor do item: R$'))
    if contador == 0:
        proBarato = item
        valorProBarato = valor
    elif valorProBarato>valor:
        proBarato = item
        valorProBarato = valor
    if valor>1000:
        pro1000+=1
    contador +=1
    valorTotal += valor
    while continuar[0] not in "SN":
        continuar = input('Deseja continuar? [S/N]').upper().strip()
    if continuar[0]=='N':
        break
     
print(f'Compra com {contador} produtos no valor de R${valorTotal:.2f} ')
print(f'Temos {pro1000} que custou mais de R$1000.00')
print(f'O produto mais barato custou foi  o produto {proBarato} e custou R${valorProBarato:.2f}' )
print("="*25)
