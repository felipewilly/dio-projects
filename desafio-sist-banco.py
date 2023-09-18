'''
Sistema Bancario, dasfio dio.me, nesse desafio irei segueir conforme aulas apresentado para caminhar por todo o percurso ja aprendido em python
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
        print('Opção digitada incorreta tente as OP ')