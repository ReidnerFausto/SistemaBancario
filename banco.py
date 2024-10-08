menu = """
    
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [0]\tSair
    
    """
    
saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3
    
while True:
    
        opcao = input (menu)
        
        if opcao == '1':
            valor = float(input('Informe o valor do depósito: '))
            
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:2f}/n"
                
            else:
                print("Operação invalida! Por favor verifique o valor informado!")
        
        elif opcao == '2':  
            valor = float(input('Informe o valor do saque: '))
            
            excedeu_saldo = valor > saldo
            
            excedeu_limite = valor > limite
            
            excedeu_saques= numero_saques >= LIMITE_SAQUES
            
            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo o suficiente!")
                
            elif excedeu_limite:
                print("Operação falho! Você excedeu o limite!")
                
            elif excedeu_saques:
                print("Operação falho! Você excedeu o limite de saques!")
                
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R${valor:2f}/n"
                numero_saques += 1
                
            else:
                print("Operação falhou! o valor informado é invalido!")
                
        elif opcao == 3:
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")
            
        elif opcao == "0":
            break
        
        else:
            print("Operação invalida, por favor selecione novamente a opção desejada")