#! /usr/bin/env python3

import random

def algoritmo(posic, lista):
	return lista[random.randint(0,len(lista)-1)]


def algoritmo_profundidade(current, options, visitados):
    if not current in visitados.keys():
        visitados[current] = options

    if not visitados[current]:
        # retroceder
        return retroceder(current, visitados)
    
    array_current = visitados[current].copy()
    for op in array_current:
        if op not in visitados.keys():
            return op
        else:
            visitados[current].remove(op)
    
    # retroceder
    return retroceder(current, visitados)
        


def retroceder(current, visitados):
    visitados.pop(current)
    next_current = list(visitados.keys())[len(visitados.keys())-1]
    visitados[next_current].remove(current)
    return next_current
    



