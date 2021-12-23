import numpy as np

from population import *

class ModifiedCrossover():
    def __init__(self, population, selected_parents: list, CR, fitness_function, dim, boundary, iter):
        self.selected_parents = selected_parents
        self.crossover_probability = CR
        self.fitness_function = fitness_function
        self.dimension = dim
        self.boundary = boundary
        self.iteration = iter
        self.population = population

    def vector_mean(self, points):
        result = np.array( [0 for _ in range(len(points[0]))] )
        for point in points:
            result = result + np.array(point)

        return result/len(points)

    def vector_distance(self, x,y):
        summation = 0

        for i in range(len(x)):
            summation += (x[i] - y[i])**2
        
        return summation ** 0.5

    def getDeltaT(self):
        if(self.iteration == 0):
            max_l = np.empty(self.dimension)
            max_l.fill(self.boundary[1] - self.boundary[0])
            deltaT = 0.2 * max_l
        else:
            pop_indexs = list(range(0,len(self.population)))
            q = 10
            k = 5
            q_points_index = np.random.choice(pop_indexs, 10, replace=False)
            q_points = [self.population[q_point].gene for q_point in q_points_index]
            x_bar = self.vector_mean(q_points)

            q_points = sorted(q_points, key= lambda x: self.vector_distance(x_bar, x))
            k_nearest_points = q_points[:k]

            deltaT = self.vector_mean(k_nearest_points)
        
        return deltaT

    def perturbStep(self, x, y):
        r  = 0.4 * self.getDeltaT()
        R = np.random.uniform(-1, 1, size = (self.dimension, 1))
        U_denominator = (sum(x**2 for x in R)) ** 1/2
        U = [R[j]/ U_denominator for j in range(self.dimension) ]

        y_i_t = y + r*U[0]

        return y_i_t

    def pollStep(self, index, x):
        D = [1 if i == index else -1 if i == self.dimension +index   else 0 for i in range(self.dimension * 2)]
        dk = D[np.random.randint(0, self.dimension * 2)]
        step_size = 0
        # self.getDeltaT()
        y_hat_i_t = x.gene + step_size*dk

        return y_hat_i_t

    def modifiedCrossover(self):
        children = []
        for i in range(len(self.selected_parents)):
            x_i_t = self.selected_parents[i]
            p_mps= np.random.rand()
            p_psac = 1 - p_mps

            if(p_mps < self.crossover_probability ):
                y_hat_i_t = self.pollStep(i, x_i_t)
                y_i_t = self.perturbStep(x_i_t, y_hat_i_t)
                
            elif(p_psac < self.crossover_probability):
                pop_indexs = list(range(0,len(self.selected_parents)))
                pop_indexs.remove(i)
                j= np.random.choice(pop_indexs, 1)
                j = j[0]
                x_j_t = self.selected_parents[j]
                
                y_hat_i_t = self.pollStep(index=i, x=x_i_t)
                y_1_t = self.perturbStep(x_i_t, y_hat_i_t,)
                
                y_hat_j_t = self.pollStep(index=j, x=x_i_t)
                y_2_t = self.perturbStep(x_j_t, y_hat_j_t)
                

                if(self.fitness_function(y_1_t) < self.fitness_function(y_2_t)):
                    y_i_t = y_1_t
                else:
                    y_i_t = y_2_t

            else:
                y_i_t = x_i_t.gene


            for j in range(self.dimension):
                alpha = np.random.rand()
                y_j_t = y_i_t[j]
                if(y_j_t > self.boundary[1]):
                    y_i_t[j] = x_i_t.gene[j] + alpha*(self.boundary[1] - x_i_t.gene[j])
                if(y_j_t < self.boundary[0]):
                    y_i_t[j] = x_i_t.gene[j] +  alpha*(x_i_t.gene[j] - self.boundary[0])

            children.append(Chromosomes(gene=y_i_t, fitness_function= self.fitness_function))

        return children
