# Entrada de dados
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso: "))

# Processamento de dados


imc = peso / (altura * altura)

print(f"Olá {nome}, sua idade é {idade}, e o seu IMC é {imc:.2f}")
