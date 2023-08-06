LIMITE_DIARIO = 3
limite_diario = 0
saldo = 0
historico_depositos = []
historico_saques = []
usuarios = {}
contas = {}
id = 1

def extrato(saldo, /, *, historico_depositos, historico_saques):
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

def cadastro_cliente(usuarios_funcao = usuarios):
    usuarios_funcao = usuarios_funcao
    while (True):
        cpf = input("Informe o CPF, somente com números: ")
        while (cpf in usuarios_funcao):
            print("CPF já registrado!")
            cpf = input("Informe o CPF, somente com números: ")
        nome = input("Informe o nome: ")
        data_nascimento = input("Informe a data de nascimento em formato dia-mês-ano: ")
        endereco = input("Informe o endereço em formato logradouro,número-bairro-cidade/sigla de estado: ")
        print("Cadastro de cliente criado com sucesso!")
        return cpf,nome,data_nascimento,endereco

def cadastro_conta(usuarios_funcao = usuarios, contas_funcao = contas, id_funcao = id):
    usuarios_funcao = usuarios_funcao
    contas_funcao = contas_funcao
    id_funcao = id_funcao
    while (True):
        cpf = input("Informe o CPF do titular da nova conta, somente com números: ")
        while (cpf not in usuarios_funcao):
            print("CPF não encontrado!")
            cpf = input("Informe o CPF, somente com números: ")
        conta = "0001" + str(id_funcao)
        print(f"Conta {conta} criada com sucesso!")
        id_funcao += 1
        return cpf, conta, id_funcao

while (True):

    print(""" 
    ========= Banco do dev =========
    ******  Digite sua opção ******
    [1] Extrato 
    [2] Saque
    [3] Depósito
    [4] Cadastrar cliente
    [5] Cadastrar conta
    [6] Finalizar
    """)
    operacao = input("Sua opção: ")

    if operacao == "1":
        extrato(saldo, historico_depositos = historico_depositos, historico_saques = historico_saques)
    elif operacao == "2":
        limite_diario, saldo = saque(limite_fixo = LIMITE_DIARIO, limite_diario = limite_diario, saldo = saldo)
    elif operacao == "3":
        saldo = deposito(saldo)
    elif operacao == "4":
        cpf, nome, data_nascimento, endereco = cadastro_cliente()
        usuarios.setdefault(cpf,[nome, data_nascimento, endereco])
    elif operacao == "5":
        cpf, conta, id = cadastro_conta()
        contas.setdefault(cpf,[conta])
    elif operacao == "6":
        print("Finalizado com sucesso!")
        break