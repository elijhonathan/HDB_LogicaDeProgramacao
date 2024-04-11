print("=" * 25)
media = float(input("Digite a media do aluno: "))
print("=" * 25)

if(media > 9):
    print("O aluno tem conceito A")

elif((media <= 9) and (media >= 7)):
    print("O aluno tem conceito B")

elif((media < 7) and (media >= 6)):
    print("O aluno tem conceito C")

elif((media < 6) and (media >= 5)):
    print("O aluno tem conceito D")

else:
    print("O aluno tem conceito F")