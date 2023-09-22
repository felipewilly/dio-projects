'''
Sistema Bancário, desafio dio.me, nesse desafio irei seguir conforme aulas apresentado para caminhar por todo o percurso já aprendido em python
'''

def menu():

    esc = input("""
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair

        |==> """).lower()

    return esc

def deposito(user):
    
        deposito = float(input('Valor [D]eposito: '))
        
        if  deposito > 0:
            user['saldo'] += deposito

def sacar():
    ...

def extrato():
    ...


def main(user):

    limite_saque = 3

    while True:

        opcao = menu()

        if opcao == 'd':

            deposito(user=user)


        elif opcao == 's':

            print('-='*15)
            print(f'Saldo atual na conta: R${ user["saldo"] }')
            print('-='*15)

            if user['numero_saques'] < limite_saque:

                numero_saques += 1

                saque = float(input('Valor de saque: '))

                if saque > 500:

                    print('Valor saque maior que limite permitido R$ 500,00 ')

                else:

                    if saldo - saque < 0:

                        print(f'saque indisponivel R${saque}  saldo conta: R${saldo}')

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


if __name__ == "__main__":

    cliente = {
        'saldo' : 100,
        'limite' : 500,
        'numero_saques': 0,
        'extrato':[] } 
    
    main(user=cliente)