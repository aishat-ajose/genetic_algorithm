from Benchmark_Functions.functions import BenchmarkFunction
import math


class Ackley (BenchmarkFunction):

    def __init__(self) -> None:
        self.global_min = 0.0
        self.boundary = [-30, 30]
        self.dimension = 2

    def objectiveFunction(self, chromosome):
        firstSum = 0.0
        secondSum = 0.0

        for c in chromosome:
            firstSum += c**2.0
            secondSum += math.cos(2.0*math.pi*c)

        n = float(len(chromosome)) 
        return -20.0*math.exp(-0.2*math.sqrt(firstSum/n)) - math.exp(secondSum/n) + 20 + math.e

    
    def functionName(self):
        return "Ackley Function"




