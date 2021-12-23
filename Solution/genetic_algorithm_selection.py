import numpy as np

def selection(population):
    selected_parents = []

    for i in range(len(population)):
        pop_indexs = list(range(0, len(population)))
        pop_indexs.remove(i)

        x_1, x_2 = np.random.choice(pop_indexs, 2, replace=False)

        tournament_best_selected = population[i]
        chromose_1 = population[x_1]
        chromose_2 = population[x_2]

        if(tournament_best_selected.fitness_score > chromose_1.fitness_score):
            tournament_best_selected = chromose_1
        if(tournament_best_selected.fitness_score > chromose_2.fitness_score):
            tournament_best_selected = chromose_2

        selected_parents.append(tournament_best_selected)
    return selected_parents