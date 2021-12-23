import numpy as np

from population import *
from clip import *

def crossover(selected_parents: list, CR, fitness_function, boundary):
    crossover_parents = []
    
    for i in range(0, len(selected_parents), 2):
        p1 = selected_parents[i].gene
        p2 = selected_parents[i+1].gene

        p_cr = np.random.rand()

        if(p_cr < CR):
            alpha = np.random.rand()

            c1 = alpha * p1 + (1-alpha) * p2
            c2 = alpha * p2 + (1-alpha) * p1

        else:
            c1 = p1
            c2 = p2
        
        child_chromose_1 = Chromosomes(gene= clip(c1, p1), fitness_function=fitness_function)
        child_chromose_2 = Chromosomes(gene= clip(c2, p2), fitness_function=fitness_function)
        crossover_parents.append(child_chromose_1)
        crossover_parents.append(child_chromose_2)

    return crossover_parents

    