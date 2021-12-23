import numpy as np

class Chromosomes:
    def __init__(self, gene, fitness_function):
        self.gene = gene
        self.fitness_score = fitness_function(gene)
        


class Population:
    def __init__(self, population_size, fitness_function, dimension , boundary):
        self.chromoses = []
        self.fitness_function = fitness_function
        self.population_size = population_size
        self.dimension = dimension
        self.boundary = boundary

    def generate_population(self):
        for _ in range(self.population_size):
            generated_gene = np.random.uniform(self.boundary[0], self.boundary[1], size = (1, self.dimension))
            generated_chromosome = Chromosomes(gene= generated_gene[0], fitness_function= self.fitness_function)
            self.chromoses.append(generated_chromosome)

    def get_population(self) -> list:
        self.generate_population()
        return self.chromoses
    









