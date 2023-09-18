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
saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        ...
    
    elif opcao == 's':
        ...

    elif opcao == 'e':
        ...
    
    elif opcao == 'q':
        break

    else:
        print('Opção digitada incorreta tente outra OP ')