from Benchmark_Functions.functions import BenchmarkFunction

class AluffiPentini(BenchmarkFunction):

    def __init__(self) -> None:
        self.global_min = -0.3523
        self.boundary = [-30, 30]
        self.dimension = 2

    def objectiveFunction(self, chromosome):
        x_1 = chromosome[0]
        x_2 = chromosome[1]
        return 0.25*(x_1**4) - 0.5*(x_1**2) + 0.1*x_1 + 0.5*(x_2**2)

    
    def functionName(self):
        return "Aluffi-Pentini Function"