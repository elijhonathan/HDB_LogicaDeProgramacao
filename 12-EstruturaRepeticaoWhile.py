numero = int(input("Digite um numero para calcular sua tabuada: "))

contador = 1

while(contador <= 10):
    print(f"{numero} x {contador} = {numero * contador}")
    contador = contador + 1