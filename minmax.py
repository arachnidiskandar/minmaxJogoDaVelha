import sys
#recebe o argumento x_o_x_o__
#tabuleiro = sys.argv[1]
import textwrap

#def minimax(estado, depth):


estado = "xo_xo__o_"


def checarVitoria(estado):
    if '_' in estado: #verifica se n está cheio
        tabuleiro = textwrap.wrap(estado, 3)    #separa a string em 3 vetores
        for linha in range(3):
            if (tabuleiro[linha][0] == tabuleiro[linha][1] and \
                tabuleiro[linha][2] == tabuleiro[linha][2]):#checa vitória em linhas
                return 1
        if tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][2] or \
            tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][0]:#checa vitória nas diagonais
            return 1
    else:#empate
        return 0

def achaJogadasPossíveis(tabuleiro):#pegas as jogadas váliadas
    movimentos_validos = []
    for i, j in enumerate(tabuleiro):
        if j == '_':
            movimentos_validos.append(i)
    return movimentos_validos

def checarVez(estado):
    if estado is "_________":
        return 'vezDoX'
    elif estado.count('x') > estado.count('o'):
        return 'vezDoO'
    else:
        return 'vezDoX'

def compMov(estado):
    jogadasPossiveis = achaJogadasPossíveis(estado)
    jogada = 0
    for letra in ['o', 'x']: #Checar se tem alguma jogada vencedora
        for i in jogadasPossiveis:
            copiaEstado = list(estado)
            copiaEstado[i] = letra
            novoEstado = ''.join(copiaEstado)
            if checarVitoria(novoEstado):
                jogada = i
                return jogada

print(compMov(estado))


