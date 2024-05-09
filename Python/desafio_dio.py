""" 
*************************************
    DESAFIO SISTEMA BANCARIO
    AUTOR: CICERO GOMES
*************************************
"""    

menu = """
(1) Depositar
(2) Sacar
(3) Extrato
(0) Sair
=> """

saldo = 0
limite = 500
numero_saques = 0
limite_saques = 3
extrato = ""

while True:
    opcao = input(menu)
    if opcao == "1":
        valor = float(input("Valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

    elif opcao == "2":
        valor = float(input("Valor do saque: "))
        maior_saldo = valor > saldo
        maior_limite = valor > limite
        numeros_saques = numero_saques > limite_saques
        if maior_saldo:
            print("Você não tem saldo o saque.")

        elif maior_limite:
            print("Valor do saque maior que o limite.")

        elif numeros_saques:
            print("Apenas tres saques.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

    elif opcao == "3":
        print("\n*************** EXTRATO ****************")
        print("Sem Operações para exibir." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("******************************************")

    elif opcao == "0":
        break

    else:
        print("Selecione opção do Menu.")