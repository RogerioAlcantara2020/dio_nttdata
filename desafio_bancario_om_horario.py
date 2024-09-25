from datetime import datetime

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


"""

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        agora = datetime.now().strftime("%d/%m/%Y %H:%M")
        print("Depósito".center(20, "#"))
        valor = input("Coloque o valor que deseja depositar: ")

        try:
            valor_deposito = float(valor)
        except:
            print("Valor inválido!")
            continue

        if float(valor_deposito) > 0:
            saldo += valor_deposito
            extrato += f"{agora} - Depósito de R$ {valor_deposito:.2f}\n"
        else:
            print("Valor inválido para essa operação")

    elif opcao == "s":
        agora = datetime.now().strftime("%d/%m/%Y %H:%M")

        print("Saque".center(20, "#"))
        valor = input("Insira o valor do saque: ")

        try:
            valor_saque = float(valor)
        except:
            print("Valor inválido!")
            continue

        if valor_saque > saldo:
            print("Nâo há saldo suficiente!")
            continue

        if numero_saque >= LIMITE_SAQUES:
            print(f"Você já sacou o limite diário d {LIMITE_SAQUES}!")
            continue


        elif (valor_saque) > 0:
            saldo -= valor_saque
            numero_saque += 1
            extrato += f"{agora} - Saque: R$ {valor_saque :.2f}\n"

    elif opcao == "e":
        if saldo == 0: continue
        extrato_resumo = f"""
        ================ INICIO EXTRATO ================

{extrato}
Saldo atual: R$ {saldo:.2f}

        ================== FIM EXTRATO =================

        """
        print(extrato_resumo)



    elif opcao == "q":
        print("Sessão finalizada com sucesso, até breve!")
        break

    else:
        print("Operação inválida, por favor selecione uma das opções disponíveis. Vamos tentar novamente? :)")
