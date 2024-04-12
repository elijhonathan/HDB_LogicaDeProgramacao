contador = 1
soma = 0


while(contador <= 5):
    idade = int(input(f"Digite a {contador}° idade: "))
    soma = soma + idade
    contador = contador + 1

print(f"A media de idade foi {soma / (contador -1)}")
