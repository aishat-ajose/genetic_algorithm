import numpy as np
from population import *
from clip import *

def crossover(target_vector, mutant, dimension, CR, fitness_function):
    crossover = np.random.rand(dimension) < CR
    trial_vector =  np.where(crossover, mutant.gene, target_vector.gene)
    trial_vector = Chromosomes(gene= trial_vector , fitness_function= fitness_function)
    return trial_vector


def selection(target_vector, trial_vector, fitness_function, population, target_index):
        target_vec_fit = fitness_function(target_vector.gene)
        trial_vec_fit = fitness_function(trial_vector.gene)

        if(trial_vec_fit < target_vec_fit) :
            return trial_vector
        else:
            return target_vector


def mutation(population, target_index, scale_factor, boundary, best_candidate) :
    pop_indexs = list(range(0,len(population)))
    pop_indexs.remove(target_index)

    x_1, x_2 = np.random.choice(pop_indexs, 2, replace=False)
    mutated_vec = best_candidate.gene + scale_factor * (population[x_1].gene - population[x_2].gene)
    mutated_vec = clip(mutated_vec, boundary=boundary)

    return mutated_vec