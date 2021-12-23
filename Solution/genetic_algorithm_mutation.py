import numpy as np

from population import *
from clip import *

def mutation(crossover_children: list, MP, boundary, fitness_function):
    mutants = []
    for i in range(len(crossover_children)):
        child = crossover_children[i].gene
        for j in range(len(child)):
            if(np.random.rand() < MP):
                alpha = np.random.uniform(-0.01, 0.01)
                
                child[j] = child[j] + alpha * (boundary[1] - boundary[0])
                

        mutated_child = Chromosomes(gene=clip(child, boundary), fitness_function=fitness_function) 
        if(mutated_child.fitness_score < crossover_children[i].fitness_score):            
            mutants.append(mutated_child)
        else:
            mutants.append(crossover_children[i])


    return mutants
    