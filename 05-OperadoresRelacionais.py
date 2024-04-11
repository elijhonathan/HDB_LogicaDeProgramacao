num = int(input("Digite um numero: "))
comparacao = int(input("Digite um numero para comparação: "))

resultado = 2 * num + 3

print("O resultado é maior que o numero da comparação: ", resultado > comparacao)
print("O resultado é menor que o numero da comparação: ", resultado < comparacao)
print("O resultado é igual que o numero da comparação: ", resultado == comparacao)
print("O resultado é maior e igual que o numero da comparação: ", resultado >= comparacao)
print("O resultado é menor e igual que o numero da comparação: ", resultado <= comparacao)
print(f"Numero para comparação:{comparacao}")
print(f"Resultado:{resultado}")