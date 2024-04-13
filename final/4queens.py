import random
import math

class FourQueensGeneticAlgorithm:
    def __init__(self, chromosome_size, population_size):
        self.population = dict()
        self.chromosome_size = chromosome_size
        self.population_size = population_size
        self.total_fitness = 0
        i = 0
        while i < population_size:
            chromosome = [0] * chromosome_size
            queen_positions = random.sample(range(chromosome_size), chromosome_size)
            for j in range(chromosome_size):
                chromosome[j] = queen_positions[j]
            self.population[i] = [chromosome, self.calculate_fitness(chromosome)]
            self.total_fitness += self.population[i][1]
            i += 1

    def calculate_fitness(self, chromosome):
        conflicts = 0
        for i in range(self.chromosome_size):
            for j in range(i + 1, self.chromosome_size):
                if (
                    chromosome[i] == chromosome[j] or
                    abs(chromosome[i] - chromosome[j]) == abs(i - j)
                ):
                    conflicts += 1
        return conflicts

    def update_population_fitness(self):
        self.total_fitness = 0
        for individual in self.population:
            individual_fitness = self.calculate_fitness(self.population[individual][0])
            self.population[individual][1] = individual_fitness
            self.total_fitness += individual_fitness

    def select_parents(self):
        roulette_wheel = []
        wheel_size = self.population_size * 5
        h_n = [1 / (fit + 1) for fit in [ind[1] for ind in self.population.values()]]
        j = 0
        for individual in self.population:
            individual_length = round(wheel_size * (h_n[j] / sum(h_n)))
            j += 1
            if individual_length > 0:
                roulette_wheel.extend([individual] * individual_length)
        random.shuffle(roulette_wheel)
        parent_indices = random.sample(roulette_wheel, self.population_size)
        new_generation = dict()
        for i, idx in enumerate(parent_indices):
            new_generation[i] = self.population[idx].copy()
        del self.population
        self.population = new_generation.copy()
        self.update_population_fitness()

    def crossover(self, parent1, parent2):
        crossover_point = random.randint(1, self.chromosome_size - 1)
        child1 = parent1[0][:crossover_point] + parent2[0][crossover_point:]
        child2 = parent2[0][:crossover_point] + parent1[0][crossover_point:]
        return child1, child2

    def generate_children(self, crossover_probability):
        number_of_pairs = round(crossover_probability * self.population_size / 2)
        individual_indices = list(range(self.population_size))
        random.shuffle(individual_indices)
        i = 0
        j = 0
        while i < number_of_pairs:
            child1, child2 = self.crossover(self.population[individual_indices[j]], self.population[individual_indices[j + 1]])
            self.population[individual_indices[j]] = [child1, self.calculate_fitness(child1)]
            self.population[individual_indices[j + 1]] = [child2, self.calculate_fitness(child2)]
            i += 1
            j += 2
        self.update_population_fitness()

    def mutate_children(self, mutation_probability):
        number_of_mutations = round(mutation_probability * self.population_size)
        for _ in range(number_of_mutations):
            individual_index = random.randint(0, self.population_size - 1)
            bit_index = random.randint(0, self.chromosome_size - 1)
            new_position = random.randint(0, self.chromosome_size - 1)
            self.population[individual_index][0][bit_index] = new_position
            self.population[individual_index][1] = self.calculate_fitness(self.population[individual_index][0])
        self.update_population_fitness()

# Main part of the code
chromosome_size = 4
population_size = 8
i = 0
solution_info = None
ga_instance = FourQueensGeneticAlgorithm(chromosome_size, population_size)
while True:
    ga_instance.select_parents()
    ga_instance.generate_children(0.8)
    ga_instance.mutate_children(0.03)
    print(ga_instance.population)
    print("Total fitness: " + str(ga_instance.total_fitness))
    # print("Total iterations: " + str(i))
    i += 1
    found = False
    for index, individual in ga_instance.population.items():
        if individual[1] == 0:
            found = True
            solution_info = {
                "Iteration": i,
                "Total fitness": ga_instance.total_fitness,
                "Individual": index,
                "Chromosome": individual[0],
                # "Fitness": individual[1]
            }
            break
    if found:
        break

if solution_info:
    print("Solution found:")
    print(solution_info)
else:
    print("No solution found within the given iterations.")

# print({
#     0: [[2, 1, 4, 3], 4], 1: [[2, 2, 4, 3], 2], 2: [[2, 4, 3, 1], 4], 3: [[4, 2, 3, 1], 1], 4: [[1, 4, 3, 1], 3], 5: [[2, 4, 1, 3], 1], 6: [[2, 4, 3, 1], 4], 7: [[4, 2, 3, 1], 1]})
# print("Total fitness: 12")
# print("Solution found:")
# print({'Iteration': 1, 'Total fitness': 12, 'Individual': 2, 'Chromosome': [2, 4, 3, 1]})



