from Benchmark_Functions.functions import BenchmarkFunction

import math

class CosineMixture(BenchmarkFunction):

    def __init__(self) -> None:
        self.global_min = -0.200
        self.boundary = [-1, 1]
        self.dimension = 2

    def objectiveFunction(self, chromosome):
        summation1 = 0
        summation2 = 0

        for i in chromosome:
            summation1 += math.cos(5* math.pi * i)
            summation2+= i**2

        return -((0.1*summation1) - summation2)

    
    def functionName(self):
        return "Cosine Mixture Function"