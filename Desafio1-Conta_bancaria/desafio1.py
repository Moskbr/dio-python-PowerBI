menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)     # mostra o menu e espera entrada do usuario

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"        # acrescentado na string extrato
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if valor > saldo:       # se nao tem saldo suficiente
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > limite:    # se excede valor limite diario
            print("Operação falhou! O valor do saque excede o limite.")
        elif numero_saques >= LIMITE_SAQUES:    # se ultrapassa quantidade de saques
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:         # caso contrario, operação válida
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)    # return if __ else __
        print(f"\nSaldo: R$ {saldo:.2f}")       # formatado em duas casas decimais
        print("==========================================")

    elif opcao == "q":      # sair
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")