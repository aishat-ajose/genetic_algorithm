import math
from Benchmark_Functions.functions import BenchmarkFunction


class Schwefel(BenchmarkFunction):

    def __init__(self) -> None:
        self.boundary = [-500, 500]
        self.dimension = 2
        self.global_min = -418.98289 * self.dimension
        # -4189.8289

    def objectiveFunction(self, chromosome):
        alpha = 418.9829
        summation= 0
        for i in chromosome:
            summation -= i*math.sin(math.sqrt(math.fabs(i)))

        return summation

    
    def functionName(self):
        return "Schwefel Function"