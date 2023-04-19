import random

def eval_func(chromosome):
    x, y, z = chromosome
    return (1/(1 + (x-2)**2 + (y+1)**2 + (z-1)**2),)

def generate_population(size, chromosome_size):
    population = []
    for i in range(size):
        chromosome = [random.uniform(-10, 10) for j in range(chromosome_size)]
        population.append(chromosome)
    return population

def select_parents(population, k=3):
    parents = random.sample(population, k)
    parents.sort(key=lambda chromosome: eval_func(chromosome), reverse=True)
    return parents[0], parents[1]

def crossover(parent1, parent2):
    child = []
    for i in range(len(parent1)):
        if random.random() < 0.5:
            child.append(parent1[i])
        else:
            child.append(parent2[i])
    return child

def mutate(chromosome, probability):
    for i in range(len(chromosome)):
        if random.random() < probability:
            chromosome[i] = random.uniform(-10, 10)
    return chromosome

def genetic_algorithm(population_size, chromosome_size, generations):
    population = generate_population(population_size, chromosome_size)
    for i in range(generations):
        new_population = []
        for j in range(population_size//2):
            parent1, parent2 = select_parents(population)
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            child1 = mutate(child1, 0.1)
            child2 = mutate(child2, 0.1)
            new_population.append(child1)
            new_population.append(child2)
        population = new_population
    population.sort(key=lambda chromosome: eval_func(chromosome), reverse=True)
    return population[0]

best_chromosome = genetic_algorithm(population_size=100, chromosome_size=3, generations=100)
print("Найкращий хромосома:", best_chromosome)
print("Найкраще значення функції:", eval_func(best_chromosome)[0])
