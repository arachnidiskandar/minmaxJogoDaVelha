import sys
#recebe o argumento x_o_x_o__
#tabuleiro = sys.argv[1]
'''
minimax(estado, profundidade)
 SE estado é terminal OU profundidade = 0 ENTÃO
 RETORNE o valor da heurística do estado
 SENÃO SE o estado representa a jogada de algum adversário ENTÃO
 valor ← +∞
 PARA CADA filho DE estado
 valor ← min(valor, minimax(filho, profundidade-1))
 FIM PARA
 RETORNE valor
 SENÃO
 valor ← -∞
 PARA CADA filho DE estado
 valor ← max(valor, minimax(filho, profundidade-1))
 FIM PARA
 RETORNE valor
 FIM SE
FIM
'''