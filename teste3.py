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
