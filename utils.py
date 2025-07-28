def calcular_custo_total(matriz, caminho):
    custo = 0
    for i in range(len(caminho) - 1):
        custo += matriz[caminho[i]][caminho[i + 1]]
    return custo
