import random
import math

class GeneticAlgorithm:
    def __init__(self, chromosome_size, population_size):
        self.population = dict()
        self.chromosome_size = chromosome_size
        self.population_size = population_size
        self.total_fitness = 0
        i = 0
        while i < population_size:
            chromosome = [0] * chromosome_size
            gene_locations = list(range(0, chromosome_size))
            ones_count = random.randint(0, chromosome_size - 1)
            ones_positions = random.sample(gene_locations, ones_count)
            for j in ones_positions:
                chromosome[j] = 1
                self.population[i] = [chromosome, ones_count]
                self.total_fitness += ones_count
                i += 1

    def update_population_fitness(self):
        self.total_fitness = 0
        for individual in self.population:
            individual_fitness = sum(self.population[individual][0])
            self.population[individual][1] = individual_fitness
            self.total_fitness += individual_fitness

    def select_parents(self):
        roulette_wheel = []
        wheel_size = self.population_size * 5
        h_n = []
        for individual in self.population:
            h_n.append(self.population[individual][1])
        j = 0
        for individual in self.population:
            individual_length = round(wheel_size * (h_n[j] / sum(h_n)))
            j = j + 1
            if individual_length > 0:
                i = 0
                while i < individual_length:
                    roulette_wheel.append(individual)
                    i += 1
        random.shuffle(roulette_wheel)
        parent_indices = []
        i = 0
        while i < self.population_size:
            parent_indices.append(roulette_wheel[random.randint(0, len(roulette_wheel) - 1)])
            i += 1
        new_generation = dict()
        i = 0
        while i < self.population_size:
            new_generation[i] = self.population[parent_indices[i]].copy()
            i += 1
        del self.population
        self.population = new_generation.copy()
        self.update_population_fitness()

    def generate_children(self, crossover_probability):
        number_of_pairs = round(crossover_probability * self.population_size / 2)
        individual_indices = list(range(0, self.population_size))
        random.shuffle(individual_indices)
        i = 0
        j = 0
        while i < number_of_pairs:
            crossover_point = random.randint(0, self.chromosome_size - 1)
            child1 = self.population[j][0][0:crossover_point] + self.population[j + 1][0][crossover_point:]
            child2 = self.population[j + 1][0][0:crossover_point] + self.population[j][0][crossover_point:]
            self.population[j] = [child1, sum(child1)]
            self.population[j + 1] = [child2, sum(child2)]
            i += 1
            j += 2
        self.update_population_fitness()

    def mutate_children(self, mutation_probability):
        number_of_bits = round(mutation_probability * self.population_size * self.chromosome_size)
        total_indices = list(range(0, self.population_size * self.chromosome_size))
        random.shuffle(total_indices)
        swap_locations = random.sample(total_indices, number_of_bits)

        for loc in swap_locations:
            individual_index = math.floor(loc / self.chromosome_size)
            bit_index = math.floor(loc % self.chromosome_size)

            if self.population[individual_index][0][bit_index] == 0:
                self.population[individual_index][0][bit_index] = 1
            else:
                self.population[individual_index][0][bit_index] = 0
        self.update_population_fitness()

chromosome_size = 8
population_size = 8
i = 0
solution_info = None
ga_instance = GeneticAlgorithm(chromosome_size, population_size)
while True:
    ga_instance.select_parents()
    ga_instance.generate_children(0.8)
    ga_instance.mutate_children(0.03)
    print(ga_instance.population)
    print("Total fitness: " + str(ga_instance.total_fitness))
    print("Total iterations: " + str(i))
    i += 1
    found = False
    for index, individual in ga_instance.population.items():
        if individual[1] == chromosome_size:
            found = True
            solution_info = {
                "Iteration": i,
                "Total fitness": ga_instance.total_fitness,
                "Individual": index,
                "Chromosome": individual[0],
                "Fitness": individual[1]
            }
            break
    if found:
        break

if solution_info:
    print("Solution found:")
    print(solution_info)
else:
    print("No solution found within the given iterations.")
