from Benchmark_Functions.functions import BenchmarkFunction
import numpy as np

class Shekel(BenchmarkFunction):

    def __init__(self, type) -> None:
        self.boundary = [0, 10]
        self.type = type
        self.dimension = 4
        if self.type == 5:
            self.global_min = -10.1532
        elif self.type == 7:
            self.global_min = -10.4029
        elif self.type == 10:
            self.global_min =  -10.5364 

    def objectiveFunction(self, chromosome):
        m  = self.type
        c = 0.1 * np.array([1, 2, 2, 4, 4, 6, 3, 7, 5, 5])
        a = np.array([
            [4.0, 1.0, 8.0, 6.0, 3.0, 2.0, 5.0, 8.0, 6.0, 7.0],
            [4.0, 1.0, 8.0, 6.0, 7.0, 9.0, 3.0, 1.0, 2.0, 3.6],
            [4.0, 1.0, 8.0, 6.0, 3.0, 2.0, 5.0, 8.0, 6.0, 7.0],
            [4.0, 1.0, 8.0, 6.0, 7.0, 9.0, 3.0, 1.0, 2.0, 3.6]
        ])
        a = np.transpose(a)


        summation1 = 0
        for i in range(m):
            summation2 = 0
            for j in range(4):
                summation2 += (chromosome[j] - a[i][j])** 2
            
            summation1 -= (1/(c[i] + summation2))
        
        return summation1

    
    def functionName(self):
        return "Shekel Function " + str(self.type)