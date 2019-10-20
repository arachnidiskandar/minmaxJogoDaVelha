import sys
#recebe o argumento x_o_x_o__
#tabuleiro = sys.argv[1]
import textwrap

def minimax(estado, depth):


estado = "ooxo_oxoo"

#Validar estado terminal
def validarEstado(estado):
    if '_' in estado:
        tabuleiro = textwrap.wrap(estado, 3)
        for linha in range(3):
            if (tabuleiro[linha][0] == tabuleiro[linha][1] and \
                tabuleiro[linha][2] == tabuleiro[linha][2]):
                return 1
        if tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][2] or \
            tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][0]:
            return 1
    else:
        return 0

def achaJogadasPossíveis(tabuleiro):
    movimentos_validos = []
    for i, j in enumerate(tabuleiro):
        if j == '_':
            movimentos_validos.append(j)
    return movimentos_validos


