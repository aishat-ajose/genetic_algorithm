from Benchmark_Functions.functions import BenchmarkFunction
import math

class Bohachevsky(BenchmarkFunction):

    def __init__(self, type: int) -> None:
        self.global_min = 0.0
        self.boundary = [-30, 30]
        self.type = type
        self.dimension = 2

    def objectiveFunction(self, chromosome):
        x = chromosome[0]
        y = chromosome[1]
        if self.type == 1:
            return (x**2) + 2*(y**2) - 0.3*(math.cos(3 * math.pi * x)) - 0.4*(math.cos(4*math.pi*y)) + 0.7
        elif self.type == 2:
            return (x**2) + 2*(y**2) - 0.3*(math.cos(3 * math.pi * x))*(math.cos(4*math.pi*y)) + 0.3
        else:
            return "Not a function"
    
    def functionName(self):
        return "Bohachevsky Function " + str(self.type)