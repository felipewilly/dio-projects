'''
Sistema Bancário, desafio dio.me, nesse desafio irei seguir conforme aulas apresentado para caminhar por todo o percurso já aprendido em python
'''


menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    |==> """.lower()

#Regras de negocio
saldo = 100
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
extrato = []

while True:

    opcao = input(menu)

    if opcao == 'd':
        
        deposito = float(input('Valor [D]eposito: '))

        if  deposito > 0:
            saldo += deposito

    elif opcao == 's':

        print('-='*15)
        print(f'Saldo atual na conta: {saldo}')
        print('-='*15)

        if numero_saques < LIMITE_SAQUES:
            
            numero_saques += 1

            saque = float(input('Valor de saque: '))

            if saque > 500:
                
                print('Valor saque maior que limite permitido R$ 500,00 ')

            else:

                if saldo - saque < 0:

                    print(f'saque indisponivel {saque}  saldo conta: {saldo}')

                else:

                    saldo = saldo - saque
                    extrato.append(saque)
                    
        else:

            print('Limite saque atingido no dia.')
        

    elif opcao == 'e':

        print(extrato)
    
    elif opcao == 'q':
        break

    else:
        print('Opção digitada incorreta tente outra OP ')