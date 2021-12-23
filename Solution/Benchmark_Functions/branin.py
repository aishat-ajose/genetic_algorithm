from Benchmark_Functions.functions import BenchmarkFunction
import math


class Branin (BenchmarkFunction):

    def __init__(self) -> None:
        self.global_min = 0.397887
        self.boundary = [-5, 10]
        self.dimension = 2

    def objectiveFunction(self, chromosome):
        summation = 0
        a = 1
        b = 5.1/(4*math.pi* math.pi)
        c=5/math.pi
        d=6
        e=10
        f=1/(8*math.pi)

        summation = a*pow((chromosome[1]-b*chromosome[0]*chromosome[0]+c*chromosome[0]-d),2) + e*(1-f)*math.cos(chromosome[0]) + e;

        return summation

    def functionName(self):
        return "Branin Function"




