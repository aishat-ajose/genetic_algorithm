from Benchmark_Functions.functions import BenchmarkFunction

class Rosenbrock(BenchmarkFunction):

    def __init__(self) -> None:
        self.global_min = 0.0
        self.boundary = [-30, 30]
        self.dimension = 2

    def objectiveFunction(self, chromosome):
        summation = 0
        for i in range(len(chromosome) - 1):
            a = chromosome[i] * chromosome[i] - chromosome[i+1]
            b = 1-chromosome[i]
            summation += 100 * a*a + b*b
        return  summation

    
    def functionName(self):
        return "Rosenbrock Function"