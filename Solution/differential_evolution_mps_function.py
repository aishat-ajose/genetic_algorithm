import numpy as np
from numpy.lib.twodim_base import tri

from population import *

class ModifiedPollSearch():
    def __init__(self, population, trial_vector, fitness_function, dimension, boundary, iteration):
        self.fitness_function = fitness_function
        self.dimension = dimension
        self.boundary = boundary
        self.iteration = iteration
        self.population = population
        self.trial_vector = trial_vector

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
            # pop_indexs.remove(target_index)
            q = 10
            k = 5
            q_points_index = np.random.choice(pop_indexs, 10, replace=False)
            q_points = [self.population[q_point].gene for q_point in q_points_index]
            x_bar = self.vector_mean(q_points)

            q_points = sorted(q_points, key= lambda x: self.vector_distance(x_bar, x))
            k_nearest_points = q_points[:k]

            deltaT = self.vector_mean(k_nearest_points)
        
        return deltaT

    def modifiedPollSearch(self):
        r  = 0.4 * self.getDeltaT()
        R = np.random.uniform(-1, 1, size = (self.dimension, 1))
        U_denominator = (sum(x**2 for x in R)) ** 1/2
        U = [ R[j]/ U_denominator for j in range(self.dimension) ]

        y_t = self.trial_vector.gene + r*U[0]

        for j in range(self.dimension):
            alpha = np.random.rand()
            y_t_j = y_t[j]
            if(y_t_j > self.boundary[1]):
                y_t[j] = self.trial_vector.gene[j] + alpha*(self.boundary[1] - self.trial_vector.gene[j])
            if(y_t_j < self.boundary[0]):
                y_t[j] = self.trial_vector.gene[j] +  alpha*(self.trial_vector.gene[j] - self.boundary[0])

        
        # check if y_t is better than trial vector
        if(self.fitness_function(y_t) < self.fitness_function(self.trial_vector.gene)):
            searched_vec  = y_t

        else:
            searched_vec = self.trial_vector.gene

        searched_vec = Chromosomes(gene = searched_vec , fitness_function=self.fitness_function)

        return searched_vec


        