#crie um scrip para solicitar as 4 notas de um aluno e inserir em uma lista. Exibir a maior nota, a menor nota, a soma, a média, e se o aluno está apovado ou reprovdo

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4  = float(input("Digite a quarta nota: "))

notas = [nota1, nota2, nota3, nota4]

# print(notas)

print("-"*60)

print(f"A maior nota é: {max(notas)}")
print(f"A menor nota é: {min(notas)}")
print(f"A soma das notas é: {sum(notas)}")

media = (sum(notas)) / len(notas)

print(f"A média final é: {media}")

if media>=6:
    print("O aluno está aprovado")
else:
    print("O aluno está reprovado")

print("-"*60)