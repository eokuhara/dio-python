# texto = input("Escreva um texto: ")
# VOGAIS = "AEIOU"

# for letra_pesquisada in texto:
#     if letra_pesquisada.upper() in VOGAIS:
#         print(letra_pesquisada, end="")
# else:    
#     print()
#     print("Executa no final do laço")

# for numero in range(0,11):
#     print(numero, end=" ")

# for numero in range(0,101,10):
#     print(numero, end=" ")

# opcao = 1

# while opcao != 0:
#     opcao = int(input("[1]Sacar \n[2]Extrato \n[0]Sair \n: = digite opcao "))

#     if opcao == 1:
#         print("Sacando...")
#     elif opcao == 2:
#         print("Exibindo Extrato...")

# else:
#     print("Obrigado por usar o nosso sistema!")       
# 
while True:
    numero = int(input("Digite um numero: ")) 

    if numero == 10:
        break
    print(numero)

print("bye...")
