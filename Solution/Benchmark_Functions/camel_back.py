from Benchmark_Functions.functions import BenchmarkFunction

import math

class CamelBack(BenchmarkFunction):

    def __init__(self, type: int) -> None:
        self.global_min = 0.0
        self.boundary = [-5, 5]
        self.type = type
        self.dimension = 2

    def objectiveFunction(self, chromosome):
        x = chromosome[0]
        y = chromosome[1]
        if self.type == 3:
            
            return (x**2) + 2*(y**2) - 0.3*(math.cos(3 * math.pi * x)) - 0.4*(math.cos(4*math.pi*y)) + 0.7
        elif self.type == 6:
            self.global_min = -1.0316
            return (4 - 2.1*(x*x) + (x*x*x*x)/3.0)*(x*x) + x*y + (-4 + 4*(y*y))*(y*y)
        else:
            return "Not a function"
    
    def functionName(self):
        return "Camel_Back Function " + str(self.type)