from Benchmark_Functions.goldstein_And_price import GoldsteinAndPrice
from Benchmark_Functions.griewank import Griewank
from Benchmark_Functions.easom import Easom
from Benchmark_Functions.dekkers_and_aarts import DekkersAndAarts
from Benchmark_Functions.branin import Branin
from Benchmark_Functions.ackley import Ackley
from Benchmark_Functions.rastrigin import Rastrigin
from Benchmark_Functions.rosenbrock import Rosenbrock
from Benchmark_Functions.schwefel import Schwefel
from Benchmark_Functions.sphere import Sphere
from Benchmark_Functions.aluffi_pentini import AluffiPentini
from Benchmark_Functions.becker_and_lago import BeckerAndLago
from Benchmark_Functions.bohachevsky import Bohachevsky
from Benchmark_Functions.camel_back import CamelBack
from Benchmark_Functions.cosine_mixture import CosineMixture
from Benchmark_Functions.shekel import Shekel

import time
import os.path
from differential_evolution_mps import DifferentialEvolutionMPS
from differential_evolution_standard import DifferentialEvolutionStandard
from genetic_algorithm_patternSearch import GeneticAlgorithmPatternSearch
from genetic_algorithm_projectionBased import GeneticAlgorithmProjection
from genetic_algorithm_standard import GeneticAlgorithmStandard

from plot_graphs import *


def main():
    save_path = 'Experiments/'
    timestr = time.strftime("%d-%m-%Y %H-%M-%S")
    name =  " Experiment Result at " + timestr
    filename = os.path.join(save_path, name + '.csv')
    f = open(filename, "x")
    
    benchmark_functions = [  
        Ackley(),  Rastrigin(), Rosenbrock(), Schwefel(),Sphere(), 
        AluffiPentini(), BeckerAndLago(), Bohachevsky(type=1), Bohachevsky(type=2),
        Branin(), CamelBack(type=3),CamelBack(type=6), CosineMixture(), DekkersAndAarts(),
        Easom(), GoldsteinAndPrice(), Griewank(),  Shekel(type=5),Shekel(type=7), Shekel(type=10), 
    ]

    # scalable functions
    scalable_benchmark_functions = [  
        Ackley(), Rastrigin(), Rosenbrock(), Schwefel(), Sphere(), Griewank()
    ]


    for i in range(len(benchmark_functions)):

        optimization_algorithms = {
            'Standard Genetic Algorithm' : 1,
            'Projection Based Genetic Algorithm' : 2,
            'Pattern Search Genetic Algorithm': 3,

            'Standard Differential Evolution' : 4,
            'Modified Differential Evolution' : 5
        }

        f.write(benchmark_functions[i].functionName())
        f.write('\n')

        for optimization_algorithm in optimization_algorithms:
            f.write(optimization_algorithm)
            f.write('\n')

            for _ in range(15):
                if(optimization_algorithms[optimization_algorithm] == 1):
                    algorithm = GeneticAlgorithmStandard(population_size=500, benchmark_function= benchmark_functions[i], crossover_probability=0.7, mutation_probability=0.001, maximum_iteration=100)
                    algorithm_result = algorithm.genetic_algorithm()
                    
                if(optimization_algorithms[optimization_algorithm]== 2):
                    algorithm = GeneticAlgorithmProjection(population_size=500, benchmark_function= benchmark_functions[i], crossover_probability=0.7, mutation_probability=0.001, maximum_iteration=100)
                    algorithm_result = algorithm.genetic_algorithm()

                if(optimization_algorithms[optimization_algorithm]== 3):
                    algorithm = GeneticAlgorithmPatternSearch(population_size=500, benchmark_function= benchmark_functions[i], crossover_probability=0.7, mutation_probability=0.001, maximum_iteration=100)
                    algorithm_result = algorithm.genetic_algorithm()
                    
                if(optimization_algorithms[optimization_algorithm] == 4):
                    algorithm = DifferentialEvolutionStandard(population_size=500, benchmark_function= benchmark_functions[i], crossover_probability=0.9, scale_factor= 0.4, max_iter=100)
                    algorithm_result = algorithm.differentialEvolution()
                    
                if(optimization_algorithms[optimization_algorithm]== 5):
                    algorithm = DifferentialEvolutionMPS(population_size=500, benchmark_function= benchmark_functions[i], crossover_probability=0.9, scale_factor= 0.4, max_iter=100)
                    algorithm_result = algorithm.differentialEvolution()
                

                f.write(str(algorithm_result['best fitness score']))
                f.write(',')

            

            f.write('\n')
    
    f.close()
    plotGraph = PlotGraph(filePath = filename)
    plotGraph.plotGraph()

main()