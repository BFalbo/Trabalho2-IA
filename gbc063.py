#! /usr/bin/env python3

import random

def algoritmo(posic, lista):
	return lista[random.randint(0,len(lista)-1)]


def algoritmo_profundidade(current, options, visitados):
    """
    <current> -> Posição atual no labirinto.
    <options> -> Possíveis movimentos.
    <visitados> -> Histórico de estados já visitados e suas <options>
    """
    # Cria o histórico para o estado current
    if not current in visitados.keys():
        visitados[current] = options

    # Se o histórico estiver vazio, então o ramo foi finalizado.
    # Retrocede para o próximo ramo.
    if not visitados[current]:
        return retroceder(current, visitados)
    
    # Pega o próximo movimento a ser executado.
    array_current = visitados[current].copy()
    for op in array_current:
        # Se o estado ainda não foi visitado, move para ele.
        if op not in visitados.keys():
            return op
        # Se já foi visitado, remove das opções de movimentos para o estado CURRENT
        else:
            visitados[current].remove(op)
    
    # Retrocede
    return retroceder(current, visitados)

def algoritmo_profundidade_iterativo(current, options, visitados, limite_altura):
    """
    Versão Iterativa
    <current> -> Posição atual no labirinto.
    <options> -> Possíveis movimentos.
    <visitados> -> Histórico de estados já visitados e suas <options>
    """
    # Cria o histórico para o estado current
    if not current in visitados.keys():
        visitados[current] = options

    # limita a busca
    if len(visitados.keys()) == 0:
        # Aumenta o limit (altura) de varredura
        limite_altura += 1
        return (0, 0), limite_altura

    # Se chegou no limite da altura da varredura, retrocede
    if (len(visitados.keys()) -1) >= limite_altura:
        return retrocede_iterativo(current, visitados, limite_altura)

    # Se o histórico estiver vazio, então o ramo foi finalizado.
    # Retrocede para o próximo ramo.
    if not visitados[current]:
        return retrocede_iterativo(current, visitados, limite_altura)
    
    # Pega o próximo movimento a ser executado.
    array_current = visitados[current].copy()
    for op in array_current:
        # Se o estado ainda não foi visitado, move para ele.
        if op not in visitados.keys():
            return op, limite_altura
        # Se já foi visitado, remove das opções de movimentos para o estado CURRENT
        else:
            visitados[current].remove(op)
    
    # Retrocede
    return retrocede_iterativo(current, visitados, limite_altura)
        
def retrocede_iterativo(current, visitados, limite_altura):
    """
    Responsável por preparar as estruturas de <visitados> e <current> para
    retroceder na árvore
    """
    # Aumenta o limit (altura) de varredura
    limite_altura += 1
    # Retira o current da lista de visitados
    visitados.pop(current)
    # Se ainda existe estados no <visitados> então pega o próximo estado na lista
    if len(visitados.keys()) > 0:
        # Pega o próximo estado.
        next_current = list(visitados.keys())[(len(visitados.keys())-1)]
        # Retira o CURRENT das opções do próximo estado
        visitados[next_current].remove(current)
        # Retorna o próximo estado
        return next_current, limite_altura
    # Se não tiver nenhum, retorna ao ponto inicial
    else:
        return (0, 0), limite_altura 

def retroceder(current, visitados):
    """
    Responsável por preparar as estruturas de <visitados> e <current> para
    retroceder na árvore
    """
    # Retira o current da lista de visitados
    visitados.pop(current)
    # Pega o próximo estado.
    next_current = list(visitados.keys())[len(visitados.keys())-1]
    # Retira o CURRENT das opções do próximo estado
    visitados[next_current].remove(current)
    # Retorna o próximo estado
    return next_current

def calculateManhattan(initial_state):
    initial_config = initial_state
    manDict = 0
    for i,item in enumerate(initial_config):
        prev_row,prev_col = int(i/ 3) , i % 3
        goal_row,goal_col = int(item /3),item % 3
        manDict += abs(prev_row-goal_row) + abs(prev_col - goal_col)
    return manDict
    



