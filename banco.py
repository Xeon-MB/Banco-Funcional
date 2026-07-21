import json

def ver_saldo(conta_logada):
    print(f"O saldo de {conta_logada['nome']} é {conta_logada['saldo']}")

def deposito(conta_logada):
    valor = int(input("Quanto será depositado? "))
    if valor > 0:
        conta_logada['saldo'] = conta_logada['saldo'] + valor
        print("Deposito Realizado!")
        conta_logada['extrato'].append(f"Depósito de {valor} realizado (+{valor})")
        
    else:
        print("Deposito negativo")

def saque(conta_logada):
    valor = int(input("Quanto será sacado? "))
    if conta_logada['saldo'] >= valor and valor > 0:
        conta_logada['saldo'] = conta_logada['saldo'] - valor
        print("Saque Realizado")
        conta_logada['extrato'].append(f"Saque de {valor} realizado(-{valor})")
        json.dump(contas)
    else:
        print("Saldo insuficiente ou saque negativo")

def addconta():
        nome = input("Qual o nome da pessoa? ").strip()
        usuario = input("Qual o usuario da pessoa? ")
        senha = input("Qual a senha da pessoa? ")
        saldo = 1000
        usuario_existe = False
        nome_vazio = False 
        senha_vazia = False      
        if len(nome) == 0:
            nome_vazio = True
        if len(senha) == 0:
            senha_vazia = True
                        
        for conta in contas:
            if usuario == conta['usuario']:
                usuario_existe = True
                break
        if usuario_existe or nome_vazio or senha_vazia:
            print("Este usuario já existe ou o nome/senha está vazio!")
        else:
                conta = {
            "nome": nome,
            "usuario": usuario,
            "senha": senha,
            "saldo": saldo,
            "extrato": []
            }
                contas.append(conta)
                salvar_contas(contas)
                
        
                print("conta Criada!")

def login():
    loguser = input("Qual o Usuario? ")
    logsenha = input("Qual a senha? ")
    conta_logada = None
    for conta in contas:
        if logsenha == conta['senha'] and loguser == conta['usuario']:
         conta_logada = conta
         break
    if conta_logada:
        print("Login realizado")
        return conta_logada
    else:
        print("Login incorreto")

def transferencia(conta_logada):
    destinatario = input("Para quem você quer tranferir? ")
    valor = float(input("Quanto você quer tranferir? "))
    conta_destino = None
    for conta in contas:
            if destinatario == conta['usuario']:
                conta_destino = conta
                break
    if conta_destino == None:
        print("Usuario não existe")
        return


    if conta_logada['saldo'] < valor or valor <= 0:
        print("Saldo insuficiente ou valor menor ou igual que 0!!")
        return

        
    if conta_destino == conta_logada:
        print("Mesma conta")
    else:
        if conta_destino:
            conta_logada['saldo'] = conta_logada['saldo'] - valor
            conta_destino['saldo'] = conta_destino['saldo'] + valor
            print("Transferência realizada")
            conta_logada['extrato'].append(f"Tranferencia para {conta_destino['nome']} de {valor} realizada(-{valor})")
            
        else:
            print("Este usuario não existe")

def ver_contas(dados):
        if len(contas) == 0:
            print("Nenhuma conta cadastrada!")
            return
    
        for conta in contas:
            print("--------------------------------")
            print(f"Nome: {conta['nome']}")
            print(f"Usuario: {conta['usuario']}")
            print(f"Saldo: {conta['saldo']}")
            print("--------------------------------")
            print(dados)

def ver_extrato(conta_logada):
    if len(conta_logada['extrato']) == 0:
        print("Você não fez nenhuma movimentação")
        return
    
    for extrato in conta_logada['extrato']:
        print(extrato)



def menu2(conta_logada, dados):
    op1 = 0
    while op1 != 7:

        print("1 - Ver saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Tranferência")
        print("5 - Ver contas")
        print("6 - Ver extrato")
        print("7 - Logout")
        op1 = int(input(""))

        match op1:
            case 1:
                ver_saldo(conta_logada)
            case 2:
                deposito(conta_logada)
            case 3:
                saque(conta_logada)
            case 4:
                transferencia(conta_logada)
            case 5:
                ver_contas(dados)
            case 6:
                ver_extrato(conta_logada)
            case 7:
                print("Logout Realizado")

def salvar_contas(contas):
    with open('dados.json', 'w', encoding='utf-8') as arquivo:
        dados = json.dump(contas, arquivo, indent=4, ensure_ascii=False)

def carregar_contas(dados):
    json.load(dados)
    print(dados)







op = 0
contas = []
dados = None


while op != 3:
    with open('dados.json', 'r', encoding='utf-8') as arquivo:
        contas = json.load(arquivo)
    print("Banco")

    print("1 - Criar conta")
    print("2 - Fazer Login")
    print("3 - Sair")
    op = int(input(""))


    match op:
        case 1:
            addconta()
        case 2:

            conta_logada = login()
            if conta_logada:
                menu2(conta_logada, dados)
        case 3:
            print("Programa encerrado")
        