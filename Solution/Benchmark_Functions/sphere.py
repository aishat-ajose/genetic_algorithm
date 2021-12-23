from Benchmark_Functions.functions import BenchmarkFunction

class Sphere(BenchmarkFunction):

    def __init__(self) -> None:
        self.global_min = 0.0
        self.boundary = [-30, 30]
        self.dimension = 2

    def objectiveFunction(self, chromosome):
        summation = 0
        for i in chromosome:
            summation += i**2
        return summation/len(chromosome)

    
    def functionName(self):
        return "Sphere Function"