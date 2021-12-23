import numpy as np

from population import *
from clip import *

def projection(mutants, fitness_function ,boundary):
    projectiles = []
    
    for i in range(len(mutants)):
        random_int = np.random.randint(len(mutants))

        x_chromosome = mutants[i]
        y_chromosome = mutants[random_int]

        x_gene = np.array(x_chromosome.gene)
        y_gene = np.array(y_chromosome.gene)

        if(x_chromosome.fitness_score < y_chromosome.fitness_score):
            projection_gene = ((x_gene * y_gene) / (y_gene * y_gene))  * y_gene
        else:
            projection_gene = ((y_gene * x_gene) / (x_gene * x_gene) ) * x_gene

        projection_chromosome = Chromosomes(gene=clip(projection_gene, boundary), fitness_function=fitness_function)

        if(projection_chromosome.fitness_score < x_chromosome.fitness_score):
            projectiles.append(projection_chromosome)
        else:
            projectiles.append(x_chromosome)


    return projectiles
