import numpy as np

def clip(vector, boundary):
    alpha = np.random.rand()
    for i in range(len(vector)):
        if(vector[i] >= boundary[1]):
            vector[i] = boundary[1] - alpha * (boundary[1] - boundary[0])

        if(vector[i] <= boundary[0]):
            vector[i] = boundary[0] + alpha * (boundary[1] - boundary[0])

    return vector