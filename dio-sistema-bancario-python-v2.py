LIMITE_DIARIO = 3
limite_diario = 0
saldo = 0
historico_depositos = []
historico_saques = []

def extrato(saldo, /, *, historico_depositos,historico_saques):
    print(f"""
    ========= BANCO DO DEV =========
    *********    EXTRATO   *********
    --------------------------------
    Saldo disponível R$ {saldo: 6.2f}
    --------------------------------
    Histórico de depósitos:""")
    for key in historico_depositos:
        print(f"""
    Depósito: R$ {key:.2f}""")
    print("""
    Histórico de saques:""")
    for key in historico_saques:
        print(f"""
    Saque: R$ -{key:.2f}
    """)

def saque(limite_fixo, limite_diario, saldo):
    LIMITE_DIARIO = limite_fixo
    limite_diario = limite_diario
    while (True):
        saque = int(input("Informe o valor que deseja sacar: "))
        if limite_diario >= LIMITE_DIARIO:
            print ("Você excedeu o limite diário de 3 saques!")
            return limite_diario, saldo
        elif saque > 500:
            print ("O valor de cada saque não pode exceder R$ 500,00")
            return limite_diario, saldo
        elif saque > saldo:
            print("Saldo insuficiente!")
            return limite_diario, saldo
        elif saque == 0:
            print ("o saque não pode ser R$ 0,00")
            return limite_diario, saldo
        else:
            saldo = saldo - saque
            historico_saques.append(saque)
            limite_diario = limite_diario + 1
            return limite_diario, saldo

def deposito(saldo):
    deposito = int(input("Informe o valor que deseja depositar: "))
    while deposito <= 0:
        deposito = int(input("Informe um valor positivo: "))
    saldo = deposito + saldo
    historico_depositos.append(deposito)
    return saldo

while (True):

    print(""" 
    ========= Banco do dev =========
    ******  Digite sua opção ******
    [1] Extrato 
    [2] Saque
    [3] Depósito
    [4] Finalizar
    """)
    operacao = input("Sua opção: ")

    if operacao == "1":
        extrato(saldo, historico_depositos = historico_depositos, historico_saques = historico_saques)
    elif operacao == "2":
        limite_diario, saldo = saque(limite_fixo = LIMITE_DIARIO, limite_diario = limite_diario, saldo = saldo)
    elif operacao == "3":
        saldo = deposito(saldo)
    elif operacao == "4":
        print("Finalizado com sucesso!")
        break