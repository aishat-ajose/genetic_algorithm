from Benchmark_Functions.functions import BenchmarkFunction

class BeckerAndLago(BenchmarkFunction):

    def __init__(self) -> None:
        self.global_min = 0.0
        self.boundary = [-10, 10]
        self.dimension = 2

    def objectiveFunction(self, chromosome):
        return ((abs(chromosome[0]) - 5) ** 2) + ((abs(chromosome[1]) - 5) ** 2)

    
    def functionName(self):
        return "Becker and Lago Function"