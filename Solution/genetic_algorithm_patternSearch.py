
from Benchmark_Functions.rastrigin import *
from population import *
from genetic_algorithm_selection import *
from genetic_algorithm_crossover import *
from genetic_algorithm_mutation import *
from genetic_algorithm_modified_crossover import *

import matplotlib.pyplot as plt


class GeneticAlgorithmPatternSearch:

    def __init__(self, population_size, crossover_probability, mutation_probability, benchmark_function, maximum_iteration):
        self.NP = population_size
        self.dim = benchmark_function.dimension
        self.CR = crossover_probability
        self.MP = mutation_probability
        self.fitness_function = benchmark_function.objectiveFunction
        self.max_iter = maximum_iteration
        self.boundary = benchmark_function.boundary
        self.generationOptimals = []
        self.global_min = benchmark_function.global_min
        self.iter = 0
    
    def initialization(self):
        p = Population(population_size= self.NP, fitness_function=self.fitness_function, dimension=self.dim, boundary=self.boundary)
        self.population = p.get_population()

    def elitism(self):
        self.population = sorted(self.population , key= lambda x : x.fitness_score)
        if(self.population[-1].fitness_score > self.best.fitness_score):
            self.population[-1] = self.best

    def genetic_algorithm(self):
        self.initialization()

        sorted_population = sorted(self.population , key= lambda x : x.fitness_score)
        self.best = sorted_population[0]
        self.generationOptimals.append(self.best)

        print('From ', self.best.fitness_score, end= " ")

        while(self.iter <= self.max_iter ):
            selected_parents = selection(population= self.population)

            modified_crossover= ModifiedCrossover(
                selected_parents = selected_parents, 
                fitness_function = self.fitness_function,
                dim = self.dim,
                boundary= self.boundary,
                CR = self.CR,
                iter= self.iter,
                population= self.population
            )

            crossover_children  = modified_crossover.modifiedCrossover()

            mutated_children = mutation(
                crossover_children = crossover_children,
                MP= self.MP,
                fitness_function= self.fitness_function,
                boundary= self.boundary
            )

            self.population = mutated_children
            self.elitism()

            # add generation best chromose to generationOptimal list
            self.generationOptimals.append(self.population[0])

            # update the best solution by comparing best solution with this generation's best solution
            if (self.population[0].fitness_score < self.best.fitness_score):
                self.best = self.population[0]

            self.iter += 1

        print('To ', self.best.fitness_score, end=' ')
        pop_index = list(range(0, self.iter+1))
        gen_optimal_scores = [x.fitness_score for x in self.generationOptimals]
        average_optimal_score = sum(gen_optimal_scores) / len(pop_index)

        ga_result = {
            "best chromose" : self.best.gene,
            "best fitness score": self.best.fitness_score,
            "average fitness score": average_optimal_score,
            "generation optimal score": gen_optimal_scores,
        } 
        
        return ga_result


# algorithm = GeneticAlgorithmPatternSearch(population_size=500, crossover_probability=0.7, mutation_probability=0.001, benchmark_function=Rastrigin(), maximum_iteration=100)
# algorithm.genetic_algorithm()
