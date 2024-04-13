import random
import math

class GeneticAlgorithm:
    def __init__(self, individual_size, population_size):
        self.population = []
        self.individual_size = individual_size
        self.population_size = population_size
        self.initialize_population()

    def initialize_population(self):
        for _ in range(self.population_size):
            individual = [math.floor(random.uniform(0, 2)) for _ in range(self.individual_size)]
            self.population.append(individual)

    def fitness(self, individual):
        return sum(individual)

    def select_parents(self):
        sorted_population = sorted(self.population, key=lambda ind: self.fitness(ind), reverse=True)
        parents = sorted_population[:self.population_size // 2]

        if len(parents) % 2 != 0:
            parents.pop(math.floor(random.uniform(0, len(parents))))

        return parents

    def crossover(self, parent1, parent2):
        crossover_point = math.floor(random.uniform(1, self.individual_size))
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        return child1, child2

    def mutate(self, individual, mutation_probability):
        for i in range(self.individual_size):
            if random.random() < mutation_probability:
                individual[i] = 1 - individual[i]

    def evolve(self, crossover_probability, mutation_probability):
        parents = self.select_parents()
        children = []

        for i in range(0, len(parents), 2):
            parent1 = parents[i]
            parent2 = parents[i + 1]
            child1, child2 = self.crossover(parent1, parent2)
            self.mutate(child1, mutation_probability)
            self.mutate(child2, mutation_probability)
            children.extend([child1, child2])

        self.population = children

individual_size = 8
population_size = 10
crossover_probability = 0.8
mutation_probability = 0.03

ga_instance = GeneticAlgorithm(individual_size, population_size)

generation = 0
while True:
    print(f"Generation {generation}:")
    for idx, ind in enumerate(ga_instance.population):
        print(f"Individual {idx}: {ind} Fitness: {ga_instance.fitness(ind)}")

    ga_instance.evolve(crossover_probability, mutation_probability)
    best_individual = max(ga_instance.population, key=lambda ind: ga_instance.fitness(ind))
    print(f"Individual {idx}: {best_individual} Fitness: {ga_instance.fitness(best_individual)}\n")
    generation += 1

    if ga_instance.fitness(best_individual) == individual_size:
        print("Solution found!")
        break