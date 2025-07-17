import numpy as np


# matriz_distancias: matriz com distâncias entre todos os pontos.
# nome_pontos: lista com os nomes de cada ponto (usada para exibição).
# indice_garagem: posição da Garagem na matriz.
# indice_lixao: posição do Lixão na matriz.
def rota_vizinho_mais_proximo(matriz_distancias, nome_pontos, indice_garagem, indice_lixao):
    total_pontos = len(matriz_distancias) # Conta quantos pontos há no total (linhas da matriz)
    visitados = [False] * total_pontos # Cria uma lista de controle para marcar os pontos já visitados
    caminho = [] # Lista que guardará a sequência da rota percorrida

    ponto_atual = indice_garagem # Começamos a rota pela Garagem
    visitados[ponto_atual] = True # Marcamos a Garagem como visitada
    caminho.append(ponto_atual) # Adicionamos a Garagem ao caminho

    custo_total = 0  # Inicializamos o custo total da rota com zero

    for _ in range(total_pontos - 2):  # Excluímos garagem e lixão do laço principal
        menor_distancia = float('inf') # Inicializamos com uma distância muito grande (infinita)
        proximo_ponto = -1 # Variável para armazenar o próximo ponto mais próximo

        for i in range(total_pontos): # Percorremos todos os pontos possíveis
            if not visitados[i] and i != indice_lixao:  # Consideramos apenas os que ainda não foram visitados e que não sejam o Lixão
                distancia = matriz_distancias[ponto_atual][i] # Pegamos a distância do ponto atual para esse ponto i
                if distancia < menor_distancia: # Se essa distância for menor que a menor encontrada até agora
                    menor_distancia = distancia # Atualizamos a menor distância
                    proximo_ponto = i # E salvamos esse ponto como o mais próximo

        if proximo_ponto == -1: # Caso true não há nenhum ponto restante além do lixão
            break   # Se não encontrou nenhum próximo ponto válido, encerra o laço

        visitados[proximo_ponto] = True # Marca o ponto escolhido como visitado
        caminho.append(proximo_ponto) # Adiciona ele à rota
        custo_total += menor_distancia  # Soma a distância ao custo total
        ponto_atual = proximo_ponto # Atualiza o ponto atual para continuar a busca a partir dele

    # Após visitar todos os pontos (exceto o lixão), adicionamos o lixão como destino final
    caminho.append(indice_lixao)
    custo_total += matriz_distancias[ponto_atual][indice_lixao] # Somamos o custo final para chegar até o lixão

    # Exibir resultado
    print("Rota sugerida (Vizinho Mais Próximo):", [nome_pontos[i] for i in caminho])

    return caminho, custo_total # Retorna a sequência da rota e o custo total