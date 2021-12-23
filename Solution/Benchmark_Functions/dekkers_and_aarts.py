from Benchmark_Functions.functions import BenchmarkFunction
import math


class DekkersAndAarts(BenchmarkFunction):

    def __init__(self) -> None:
        self.global_min = -24776.5183
        self.boundary = [-20, 20]
        self.dimension = 2

    def objectiveFunction(self, chromosome):
        summation = 100000.*chromosome[0]*chromosome[0] + chromosome[1]*chromosome[1] - pow((chromosome[0]*chromosome[0]+chromosome[1]*chromosome[1]),2) +pow((chromosome[0]*chromosome[0]+chromosome[1]*chromosome[1]),4)/100000
        return summation

    def functionName(self):
        return "Dekkers And Aarts Function"




