menu  = """

Olá, seja bem vindo(a)!
Escolha uma opção para começar:
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
lista_depositos = []
lista_saques = []
total_saques = 0
valor_deposito = 0
valor_saque = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d": #processo depósito
        print("Depósito:")
        valor_deposito = float(input("Digite o valor do depósito: R$ ")) #recebe o valor de entrada do usuário
        if valor_deposito < 0:
            print("Valor não pode ser menor do que zero!")
        else:
            lista_depositos.append(valor_deposito) #adiciona o valor de entrada do usuário na variavel extrato
            print("Valor depositado: ","R$ "f"{valor_deposito:.2f}")
            saldo += valor_deposito #soma o valor depositado ao saldo
            print("Total atualizado em conta: ","R$ "f"{saldo:.2f}")

    elif opcao == "s": #processo saque
        print("Saque:")
        valor_saque = float(input("Digite o valor do saque: R$ ")) #recebe o valor de entrada do usuário
        if valor_saque > 500 or valor_saque > saldo:
            print("Operação não permitida por falta de saldo ou saque é maior do que o permitido de R$ 500,00")
        else:    
            lista_saques.append(valor_saque) 
            total_saques = (len(lista_saques)) 
            if total_saques > LIMITE_SAQUES: #controla limite de saques
                print("Valor máximo de saques diários atingido! Volte amanhã.")
            else:
                print("Valor sacado: ","R$ "f"{valor_saque:.2f}")
                saldo -= valor_saque #subtrai o valor depositado do saldo
                print("Total atualizado em conta: ","R$ "f"{saldo:.2f}")        

    elif opcao == "e": #processo extrato
        if saldo <= 0:
            print("Não foram realizadas movimentações.")
        else:
            print("Extrato ==============")
            print("Detalhe Saques =======")
            for item in lista_saques:
                valor = float(item)
                print("R$ ",f"{valor:.2f}")
            print("Total de Saques =====> ","R$ ",sum(lista_saques))
            print("Detalhe Depósitos ===")
            for item in lista_depositos:
                valor = float(item)
                print("R$ ",f"{valor:.2f}")
            print("Total de Depósitos ==> ","R$ ",sum(lista_depositos))
            print("Saldo Total ============> ","R$ ",saldo)

    elif opcao == "q": #processo sair
        print("Sistema finalizado!")
        break

    else:
        print("Operação inválida! Por favor selecione novamente a operação desejada.")
