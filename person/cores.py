

class Cores:
    PRETO = '\033[0:30m'
    VERMELHO = '\033[0;31m'
    VERDE = '\033[0;32m'
    AMARELO = '\033[0;33m'
    AZUL = '\033[0;34m'
    ROXO = '\033[0;35m'
    CIANO = '\033[0;36m'
    BRANCO = '\033[0;37m'
    RESET = '\033[0m'


if __name__ == "__main__":

    print(Cores.VERMELHO + "Este é um texto vermelho!" + Cores.RESET)