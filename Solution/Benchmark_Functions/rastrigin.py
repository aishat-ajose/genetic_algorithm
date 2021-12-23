
from Benchmark_Functions.functions import BenchmarkFunction
import math

class Rastrigin(BenchmarkFunction):

    def __init__(self) -> None:
        self.global_min = 0.0
        self.boundary = [-512, 512]
        self.dimension = 2

    def objectiveFunction(self, chromosome):
        summation = 0
        for i in chromosome:
            summation+= ((i**2) - (10 * math.cos(2 * math.pi * i)) + 10)
        

        return summation

    
    def functionName(self):
        return "Rastrigin Function"

# a = Rastrigin()
# print(a.objectiveFunction([0,0,0,0,0,0,0,0,0,0,0]))