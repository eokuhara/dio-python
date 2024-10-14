
def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem_2(nome="Everson"):
    print(f"Olá {nome}") 

def exibir_mensagem_3(nome):
    print(f"Olá {nome}")  

def funcao_teste():
    #print()

    exibir_mensagem()
exibir_mensagem_2()
exibir_mensagem_3(nome="Okuhara")
funcao_teste()

def calcular_total(numeros):
    return sum(numeros)
print(calcular_total([10,35,40,55]))

def criar_carro(*, cor, modelo, ano, marca):
    print(cor, modelo, ano, marca)
criar_carro(cor="preto", modelo="Tiida", ano="2011", marca="Nissan")


def somar(a,b):
    return a + b

def subtrair(a,b):
    return a - b

def exibir_resultado(a,b, funcao):
    resultado = funcao(a,b)
    print(f"O resultado é {a} + {b} = {resultado}")

exibir_resultado(10,20,somar)
exibir_resultado(20,10,subtrair)

operacao = somar
print(operacao(22,12))

salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

salario_com_bonus = salario_bonus(500)

print(salario_com_bonus)