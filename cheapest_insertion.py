# matriz_distancias: matriz com distâncias entre todos os pontos.
# nome_pontos: lista com os nomes dos pontos (apenas para exibição).
# indice_garagem: índice do ponto de partida.
# indice_lixao: índice do ponto final.

def rota_aresta_mais_baratas(matriz_distancias, nome_pontos, indice_garagem, indice_lixao):
    total_pontos = len(matriz_distancias) # Número total de pontos na matriz
    visitados = [False] * total_pontos # Lista que indica se cada ponto já foi adicionado à rota

    # Começamos com uma rota inicial: da garagem direto para o lixão
    rota = [indice_garagem, indice_lixao]  
    visitados[indice_garagem] = True # Marca a garagem como visitada
    visitados[indice_lixao] = True # Marca o lixão como visitado

    # Enquanto ainda houver pontos não visitados
    while not all(visitados): 
        menor_custo_insercao = float('inf') # Inicializa o menor custo de inserção com infinito
        melhor_ponto = None # Armazena o ponto candidato à melhor inserção
        melhor_posicao = None # Posição ideal na rota para inserir esse ponto

        for ponto in range(total_pontos): # Testa todos os pontos ainda não inseridos na rota
            if visitados[ponto]:
                continue # Pula pontos já visitados

            # Tenta inserir o ponto entre cada par consecutivo da rota atual
            for i in range(len(rota) - 1):
                a = rota[i]
                b = rota[i + 1]
                custo_sem_ponto = matriz_distancias[a][b] # Custo atual entre a e b
                custo_com_ponto = matriz_distancias[a][ponto] + matriz_distancias[ponto][b] # Custo se inserirmos o ponto entre a e b
                aumento_custo = custo_com_ponto - custo_sem_ponto # Diferença causada pela inserção

                 # Se essa inserção for a mais barata encontrada até agora
                if aumento_custo < menor_custo_insercao:
                    menor_custo_insercao = aumento_custo
                    melhor_ponto = ponto
                    melhor_posicao = i + 1  # Inserir após 'a'

        # Inserimos o ponto na posição que menos aumentou o custo
        rota.insert(melhor_posicao, melhor_ponto)
        visitados[melhor_ponto] = True

    # Após montar a rota completa, calculamos o custo total percorrendo todos os pares consecutivos
    custo_total = 0
    for i in range(len(rota) - 1):
        custo_total += matriz_distancias[rota[i]][rota[i + 1]]

    # Exibir resultado
    print("Rota sugerida (Aresta Mais Barata):", [nome_pontos[i] for i in rota])

    return rota, custo_total