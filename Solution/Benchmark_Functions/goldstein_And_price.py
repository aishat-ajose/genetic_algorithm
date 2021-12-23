from Benchmark_Functions.functions import BenchmarkFunction
import math


class GoldsteinAndPrice(BenchmarkFunction):

    def __init__(self) -> None:
        self.global_min = 3.0
        self.boundary = [-2, 2]
        self.dimension = 2

    def objectiveFunction(self, chromosome):
        summation = (1+(chromosome[0]+chromosome[1]+1)*(chromosome[0]+chromosome[1]+1)*(19-14*chromosome[0]+3*chromosome[0]*chromosome[0]-14*chromosome[1]+6*chromosome[0]*chromosome[1]+3*chromosome[1]*chromosome[1]))
        summation *= (30+(2*chromosome[0]-3*chromosome[1])*(2*chromosome[0]-3*chromosome[1])*(18-32*chromosome[0]+12*chromosome[0]*chromosome[0]+48*chromosome[1]-36*chromosome[0]*chromosome[1]+27*chromosome[1]*chromosome[1]))

        return summation

    def functionName(self):
        return "Goldstein And Price Function"




