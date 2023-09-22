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

def sacar(user):

    print('-='*15)
    print(f'Saldo atual na conta: R$ { user["saldo"]}')
    print('-='*15)

    if user['numero_saques'] < user['limite_saque']:

        user['numero_saques'] += 1

        saque = float(input('Valor de saque: '))

        if saque > 500:

            print('Valor saque maior que limite permitido R$ 500,00 ')

        else:

            if user['saldo'] - saque < 0:

                print(user['numero_saques'])

                print(f'saque indisponivel R${saque}  saldo conta: R${user["saldo"]}')

            else:

                user['saldo'] = user['saldo'] - saque


    else:

        print('Limite saque atingido no dia.')

def extrato():
    ...

def main(user):

    while True:

        opcao = menu()

        if opcao == 'd':

            deposito(user=user)

        elif opcao == 's':
             
             sacar(user=user)

        elif opcao == 'e':

            print(extrato)

        elif opcao == 'q':
            break

        else:
            print('Opção digitada incorreta tente outra OP ')

if __name__ == "__main__":

    cliente = {
        'saldo' : 0,
        'limite' : 500,
        'limite_saque': 3,
        'numero_saques': 0,
        'extrato':[] } 
    
    main(user=cliente)