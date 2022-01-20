#!/usr/bin/env python3

from random import randint
import cv2
import numpy as np
from time import sleep


def novoGrid(geracaoAtual):
    aux = []
    novaGeracao = []

    # Gera uma matriz vazia que sera atualizada depois de contar os vizinhos
    for k in range(0, quant_arrays):
        for j in range(0, quant_items_por_array):
            aux.append(0)
        novaGeracao.append(aux[:])
        aux.clear()

    # Recebe o numero de vizinhos do elemento e define o elemento da nova geracao
    l, e = 0, 0
    while l < quant_arrays:
        e = 0
        while e < quant_items_por_array:
            numViz = contaVizinhos(geracaoAtual, l, e)
            if geracaoAtual[l][e] == 1 and (numViz < 2 or numViz > 3) or (geracaoAtual[l][e] == 0 and (numViz != 3)):
                novaGeracao[l][e] = 0

            elif (geracaoAtual[l][e] == 1 and (numViz == 2 or numViz == 3)) or geracaoAtual[l][e] == 0 and numViz == 3:
                novaGeracao[l][e] = 1

            # else:
            #     # print(f"Erro. Numero de vizinhos nao foi valido no elemento ({l}, {e})")

            e += 1
        l += 1

    # for line in gridNovo:
    #     print(line)

    return novaGeracao

def jogoDaVida(principal, jgeracao=0):
    criaImagem(principal, jgeracao)
    jgeracao += 1
    atualizado = novoGrid(principal)[:]
    return atualizado

def criaImagem(vetor, gera):
    taxa_tamanho = 5
    vertical = 0
    image = np.zeros((alt, lar), np.uint8)
    horizontal = 0
    generation = "Gen: " + str(gera)
    cv2.putText(image, generation, (int(lar * 6/7), 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

    for a in vetor:
        for b in a:
            if b == 0:
                cv2.rectangle(image, (horizontal, vertical), (horizontal + taxa_tamanho, vertical + taxa_tamanho),
                              (256, 256, 256), -1)
            if b == 1:
                cv2.rectangle(image, (horizontal, vertical), (horizontal + taxa_tamanho, vertical + taxa_tamanho),
                              (0, 0, 0), -1)
            horizontal += taxa_tamanho
        horizontal = 0
        vertical += taxa_tamanho

    cv2.imshow('JOGO DA VIDA', image)
    cv2.waitKey(20)


def geraModelo():
    modelo = []
    aux = []

    # Taxa 1/0 igualitaria

    # for k in range(0, quant_arrays):
    #     for j in range(0, quant_items_por_array):
    #         aux.append(randint(0, 1))
    #     modelo.append(aux[:])
    #     aux.clear()

    # Taxa 1/0 menor
    for k in range(0, quant_arrays):
        for j in range(0, quant_items_por_array):
            temp = randint(0, 100)
            if temp > 25:
                aux.append(0)
            else:
                aux.append(1)
        modelo.append(aux[:])
        aux.clear()

    # Modelo para testes

    # modelo = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #           ]

    return modelo


def defineAnalises(vetor, linhaElemento, colunaElemento):  # Retorna uma TUPLA de INTEIROS com a coluna/linha certas
    maxLinhas = len(vetor) - 1
    maxColunas = len(vetor[0]) - 1

    # Define o primeiro elemento da contagem de vizinhos, baseando-se na posicao (0,0; 0,max; max,0; max,max)
    if linhaElemento == 0 and colunaElemento == 0:
        linha_analisada = linhaElemento
        coluna_analisada = colunaElemento

    elif linhaElemento == 0 and colunaElemento == maxColunas:
        linha_analisada = linhaElemento
        coluna_analisada = colunaElemento - 1

    elif linhaElemento == maxLinhas and colunaElemento == 0:
        linha_analisada = linhaElemento - 1
        coluna_analisada = colunaElemento

    elif linhaElemento == maxLinhas and colunaElemento == maxColunas:
        linha_analisada = linhaElemento - 1
        coluna_analisada = colunaElemento - 1

    return linha_analisada, coluna_analisada


def contaVizinhos(vetor, linhaElemento, colunaElemento):  # Retorna um INTEIRO de vizinhos do elemento
    maxLinhas = len(vetor) - 1
    maxColunas = len(vetor[0]) - 1
    numVizinhos = 0

    # MEIOS - Unidades que possuem todos os 8 vizinhos
    if 0 < linhaElemento < maxLinhas and 0 < colunaElemento < maxColunas:
        listaV = []
        linhaSeguinte = linhaElemento + 1
        colunaSeguinte = colunaElemento + 1
        linha_analisada = linhaElemento - 1

        while linha_analisada <= linhaSeguinte:
            coluna_analisada = colunaElemento - 1
            while coluna_analisada <= colunaSeguinte:
                if linhaElemento != linha_analisada or colunaElemento != coluna_analisada:
                    numVizinhos += vetor[linha_analisada][coluna_analisada]
                if vetor[linha_analisada][coluna_analisada] == 1 and (
                        linhaElemento != linha_analisada or colunaElemento != coluna_analisada):
                    listaV.append([linha_analisada, coluna_analisada])
                coluna_analisada += 1
            linha_analisada += 1

    # EXTREMOS - Unidades que so possuem 3 vizinhos
    elif (linhaElemento == 0 or linhaElemento == maxLinhas) and (colunaElemento == 0 or colunaElemento == maxColunas):
        listaV = []
        linha_analisada, coluna_analisada = defineAnalises(vetor, linhaElemento, colunaElemento)
        linhaSeguinte, colunaSeguinte = linha_analisada + 1, coluna_analisada + 1

        while linha_analisada <= linhaSeguinte:
            while coluna_analisada <= colunaSeguinte:
                if linhaElemento != linha_analisada or colunaElemento != coluna_analisada:
                    numVizinhos += vetor[linha_analisada][coluna_analisada]
                if vetor[linha_analisada][coluna_analisada] == 1 and (
                        linhaElemento != linha_analisada or colunaElemento != coluna_analisada):
                    listaV.append([linha_analisada, coluna_analisada])
                coluna_analisada += 1
            coluna_analisada -= 2
            linha_analisada += 1

    # BORDAS - Unidades que possuem 5 vizinhos
    elif linhaElemento == 0 or linhaElemento == maxLinhas or colunaElemento == 0 or colunaElemento == maxColunas:
        listaV = []

        if linhaElemento == 0:  # Cima
            linha_analisada = linhaElemento

            while linha_analisada < linhaElemento + 2:
                coluna_analisada = colunaElemento - 1
                while coluna_analisada < colunaElemento + 2:
                    if linhaElemento != linha_analisada or colunaElemento != coluna_analisada:
                        numVizinhos += vetor[linha_analisada][coluna_analisada]
                    if vetor[linha_analisada][coluna_analisada] == 1 and (linhaElemento != linha_analisada or
                                                                          colunaElemento != coluna_analisada):
                        listaV.append([linha_analisada, coluna_analisada])
                    coluna_analisada += 1
                linha_analisada += 1

        elif linhaElemento == maxLinhas:  # Baixo

            linha_analisada = linhaElemento - 1

            while linha_analisada <= linhaElemento:
                coluna_analisada = colunaElemento - 1
                while coluna_analisada < colunaElemento + 2:
                    if linhaElemento != linha_analisada or colunaElemento != coluna_analisada:
                        numVizinhos += vetor[linha_analisada][coluna_analisada]
                    if vetor[linha_analisada][coluna_analisada] == 1 and (linhaElemento != linha_analisada or
                                                                          colunaElemento != coluna_analisada):
                        listaV.append([linha_analisada, coluna_analisada])
                    coluna_analisada += 1
                linha_analisada += 1

        elif colunaElemento == 0:  # Esquerda
            linha_analisada = linhaElemento - 1

            while linha_analisada < linhaElemento + 2:
                coluna_analisada = colunaElemento - 1
                while coluna_analisada <= colunaElemento + 1:
                    if linhaElemento != linha_analisada or colunaElemento != coluna_analisada:
                        numVizinhos += vetor[linha_analisada][coluna_analisada]
                    if vetor[linha_analisada][coluna_analisada] == 1 and (linhaElemento != linha_analisada or
                                                                          colunaElemento != coluna_analisada):
                        listaV.append([linha_analisada, coluna_analisada])
                    coluna_analisada += 1
                linha_analisada += 1

        elif colunaElemento == maxColunas:  # Direita
            linha_analisada = linhaElemento - 1

            while linha_analisada < linhaElemento + 2:
                coluna_analisada = colunaElemento - 1
                while coluna_analisada <= colunaElemento:
                    if linhaElemento != linha_analisada or colunaElemento != coluna_analisada:
                        numVizinhos += vetor[linha_analisada][coluna_analisada]
                    if vetor[linha_analisada][coluna_analisada] == 1 and (linhaElemento != linha_analisada or
                                                                          colunaElemento != coluna_analisada):
                        listaV.append([linha_analisada, coluna_analisada])
                    coluna_analisada += 1
                linha_analisada += 1
    else:
        print("\nOcorreu um erro.\n")

    return numVizinhos


# Declaracao das variaveis
alt = 715
lar = 1200
fator = 6
vivos, geracao, tempo, geras = 0, 0, 0, 10
quant_arrays = int(alt / fator)
quant_items_por_array = int(lar / fator)
# print(quant_items_por_array, "x", quant_arrays)
grid = geraModelo()
atualiza = grid[:]

# Inicio do jogo
while True:
    grid = jogoDaVida(grid, geracao)
    geracao += 1
