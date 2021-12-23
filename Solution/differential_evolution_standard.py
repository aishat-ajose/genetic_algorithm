from Benchmark_Functions.rosenbrock import *

from differential_evolution_functions import *

from population import *

class DifferentialEvolutionStandard:
 
    def __init__(self, benchmark_function, scale_factor: float, crossover_probability:float, population_size:int, max_iter: int):
        self.population_size = population_size
        self.dim = benchmark_function.dimension
        self.CR = crossover_probability
        self.F = scale_factor
        self.fitness_function = benchmark_function.objectiveFunction
        self.max_iteration = max_iter
        self.boundary = benchmark_function.boundary
        self.generationOptimals = []
        self.global_min = benchmark_function.global_min

        self.iter = 0

    def initialization(self):
        p = Population(population_size= self.population_size, fitness_function=self.fitness_function, dimension=self.dim, boundary=self.boundary)
        self.population = p.get_population()
    
    def differentialEvolution(self):

        self.initialization()

        sorted_population = sorted(self.population , key= lambda x : x.fitness_score)
        self.best = sorted_population[0]
        self.generationOptimals.append(self.best)

        print('From ', self.best.fitness_score, end= " ")

        while(self.iter <= self.max_iteration):
            for target_index in range(self.population_size):
                self.target_index = target_index
                target_vector = self.population[target_index]
                mutated_vector = mutation(self.population, target_index=target_index, scale_factor=self.F, boundary = self.boundary, best_candidate=self.best)
                mutated_vector = Chromosomes(gene= mutated_vector, fitness_function=self.fitness_function)
                
                trail_vector = crossover(
                    target_vector= target_vector,
                    mutant= mutated_vector,
                    dimension= self.dim,
                    CR= self.CR,
                    fitness_function= self.fitness_function
                )

                selector_vector = selection(
                    target_index= target_index,
                    trial_vector= trail_vector,
                    fitness_function= self.fitness_function,
                    population= self.population,
                    target_vector= target_vector
                )

                self.population[target_index] = selector_vector


            self.population = sorted(self.population , key= lambda x : x.fitness_score)

            # add generation best chromose to generationOptimal list
            self.generationOptimals.append(self.population[0])

            # update the best solution by comparing best solution with this generation's best solution
            if (self.population[0].fitness_score < self.best.fitness_score):
                self.best = self.population[0]

            self.iter += 1

        print('To ', self.best.fitness_score, end=' ')
        pop_index = list(range(0, self.iter))
        gen_optimal_scores = [x.fitness_score for x in self.generationOptimals]
        average_optimal_score = sum(gen_optimal_scores) / len(pop_index)

        de_result = {
            "best chromose" : self.best.gene,
            "best fitness score": self.best.fitness_score,
            "average fitness score": average_optimal_score,
            "generation optimal score": gen_optimal_scores,
        } 
        
        return de_result        

# a = DifferentialEvolutionStandard(population_size=500, crossover_probability=0.9, scale_factor= 0.4, max_iter=100, benchmark_function=Rosenbrock())
# a.differentialEvolution()
