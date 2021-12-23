from Benchmark_Functions.functions import BenchmarkFunction
import math

class Griewank(BenchmarkFunction):

    def __init__(self):
        self.global_min = 0.0
        self.boundary = [-500, 500]
        self.dimension = 2

    def objectiveFunction(self, chromosome):
        summation = 0
        prod = 1
        for i in range(len(chromosome)):
            summation+= chromosome[i] * chromosome[i]
            prod *= math.cos(chromosome[i]/ math.sqrt(i+1))
        
        summation = summation/( 4000-prod+1)
        return summation

    
    def functionName(self):
        return "Griewank Function"