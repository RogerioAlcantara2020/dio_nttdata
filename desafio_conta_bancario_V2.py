from datetime import datetime

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"
usuarios = []
contas = []


def exibir_menu():
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [lc] Listar Contas
    [nu] Novo Usuário
    [q] Sair
 """
    return input(menu).lower()


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        agora = datetime.now().strftime("%d/%m/%Y %H:%M")
        extrato += f"{agora} - Depósito: R${valor:.2f}\n"
        print(" Depósito realizado com sucesso! ".center(80, "="))
    else:
        print("Não foi possível realizar o depósito. Valor não é válido!")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saque):
    if valor > saldo:
        print("Você não tem saldo suficiente")

    elif valor > limite:
        print("Valor do saque é maior do que o limite")

    elif numero_saques >= limite_saque:
        print("Números de saques diários")

    elif valor > 0:
        saldo -= valor
        agora = datetime.now().strftime("%d/%m/%Y %H:%M")
        numero_saques += 1
        extrato += f"{agora} - Saque: R${valor:.2f}\n"
        print(f"{numero_saques} Saque realizado com sucesso! ".center(80, "="))
    else:
        print("Não foi possível realizar o saque. Valor não é válido!")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def filtrar_usuarios(cpf, usuarios):
    usuario_filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None


def criar_usuario(usuarios):
    cpf = input("Informe o cpf, somente números: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("Este CPF já está sendo usado!")
        return

    nome = input("Informe o nome completo:")
    data_nascimento = input("Informe a data de nascimento (01/05/2000): ")
    endereco = input("Informe o endereço (logradouro, numero - bairro - cidade/Estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereco})
    print(" Cliente criado com sucesso! ".center(80, "="))


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Insira o CPF, somente os números: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print(" Conta criada com sucesso! ")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Não conseguimos criar uma conta.")


def listar_contas(contas):
    for conta in contas:
        ln = f"""
        Agência: {conta["agencia"]}\n
        C/C: {conta["numero_conta"]}\n
        Titular: {conta["usuario"]["nome"]}
"""
        print(ln)


while True:
    opcao = exibir_menu()

    if opcao == "d":
        valor = input("Informe o valor para depósito: ")

        try:
            valor = float(valor)
        except:
            print("Valor inválido!")
            continue

        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = input("Informe o valor para saque: ")

        try:
            valor = float(valor)
        except:
            print("Valor inválido!")
            continue

        saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite,
                                              numero_saques=numero_saques,
                                              limite_saque=LIMITE_SAQUES)

    elif opcao == "nu":
        criar_usuario(usuarios)

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
