#operadores-logicos
#and para ser verdadeiro tudo tem que ser verdadeiro
#ou para ser verdadeiro um tem que ser verdadeiro

print(True and True)
print(True and False)
print(False and False)

print(True or True)
print(True or False)
print(False or False)



saldo = 1000
saque = 200
limite = 100
conta_especial = True



#print(saldo)

saldo >= saque and saque <= limite or conta_especial and saldo >= saque

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

print("teste")
print(saldo <= saque)
