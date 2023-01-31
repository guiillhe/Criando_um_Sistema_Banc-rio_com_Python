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

