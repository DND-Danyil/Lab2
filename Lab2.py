import random
import numpy as np
from deap import creator, base, tools, algorithms

def eval_func(chromosome):
    x, y, z = chromosome
    return (1/(1 + (x-2)**2 + (y+1)**2 + (z-1)**2),)

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("attr_float", random.uniform, -10, 10)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=3)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", eval_func)

toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.1)
toolbox.register("select", tools.selBest)

def main():
    random.seed(42)
    pop_size = 100
    num_generations = 100
    cxpb, mutpb = 0.5, 0.2
    
    pop = toolbox.population(n=pop_size)
    best = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("min", np.min)
    stats.register("max", np.max)
    
    pop, log = algorithms.eaSimple(pop, toolbox, cxpb, mutpb, num_generations, stats=stats, halloffame=best, verbose=False)
    
    best_chromosome = best[0]
    print("Найкраща хромосома:", best_chromosome)
    print("Найкраще значення функції:", eval_func(best_chromosome)[0])

if __name__ == "__main__":
    main()
