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

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do deposito:"))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito R$: {valor:.2f}\n"

        else:
            print("Depósito não realizado! Valor informado incorreto.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saque não realizado! Saldo insuficiente.")
        
        elif excedeu_limite:
            print("Saque não realizado! Valor acime do limite máximo permitido.")
        
        elif excedeu_saques:
            print("Saque não realizado! Número máximo de saques excedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque R$: {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Saque não realizado! Valor informado não é válido.")
    

    elif opcao == "e":
        print("\n===========EXTRATO===========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo R$: {saldo:.2f}")
        print("=============================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")