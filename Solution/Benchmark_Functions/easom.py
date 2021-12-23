from Benchmark_Functions.functions import BenchmarkFunction
import math


class Easom(BenchmarkFunction):

    def __init__(self) -> None:
        self.global_min = -1.0
        self.boundary = [-10, 10]
        self.dimension = 2

    def objectiveFunction(self, chromosome):
        summation = -math.cos(chromosome[0])*math.cos(chromosome[1])*math.exp((-(chromosome[0]-math.pi)** 2)-((chromosome[1]-math.pi)**2))
        return summation

    def functionName(self):
        return "Easom Function"




