MAIOR_IDADE = 18
IDADE_ESPECIAL = 16

idade = int(input("Informe a sua idade: "))

# if idade >= MAIOR_IDADE:
#     print("Maior de idade, pode tirar CNH")

# if idade < MAIOR_IDADE:
#     print("Menor de idade, não pode tirar CNH")

# if idade >= MAIOR_IDADE:
#     print("Maior de idade, pode tirar CNH")
# else:
#     print("Menor de idade, não pode tirar CNH")

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas somente teóricas para posteriormente tirar CNH")
else: 
    print("Menor de idade, não pode tirar CNH")
