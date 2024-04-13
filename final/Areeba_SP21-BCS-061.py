import random
import math

class GeneticAlgorithm:
    def __init__(self, population_size, equation, target_value, error_range):
        self.population = dict()
        self.population_size = population_size
        self.equation = equation
        self.target_value = target_value
        self.error_range = error_range
        self.total_fitness = 0
        i = 0
        while i < population_size:
            chromosome = random.uniform(-10, 10) 
            self.population[i] = [chromosome, self.calculate_fitness(chromosome)]
            self.total_fitness += self.population[i][1]
            i += 1

    def calculate_fitness(self, chromosome):
        calculated_value1 = eval(self.equation.replace('a', str(chromosome)))
        calculated_value2 = eval(self.equation.replace('b', str(chromosome)))
        error = abs(calculated_value1 - self.target_value)
        error = abs(calculated_value2 - self.target_value)
        return error

    def update_population_fitness(self):
        self.total_fitness = sum(individual[1] for individual in self.population)

    def update_population_fitness(self):
        self.total_fitness = 0
        for individual in self.population:
            self.population[individual][1] = self.calculate_fitness(self.population[individual][0])
            self.total_fitness += self.population[individual][1]

    def select_parents(self):
        roulette_wheel = []
        wheel_size = self.population_size * 5
        fitness_scores = [self.population[individual][1] for individual in self.population]
        for individual in self.population:
            individual_length = round(wheel_size * (self.population[individual][1] / sum(fitness_scores)))
            if individual_length > 0:
                roulette_wheel.extend([individual] * individual_length)
        random.shuffle(roulette_wheel)
        parent_indices = random.choices(roulette_wheel, k=self.population_size)
        new_generation = {i: self.population[parent_idx].copy() for i, parent_idx in enumerate(parent_indices)}
        self.population = new_generation.copy()
        self.update_population_fitness()

    def generate_children(self, crossover_probability):
        number_of_pairs = round(crossover_probability * self.population_size / 2)
        individual_indices = list(range(0, self.population_size))
        random.shuffle(individual_indices)
        i = 0
        j = 0
        while i < number_of_pairs:
            crossover_point = random.uniform(-10, 10)
            child1 = crossover_point
            child2 = self.population[j][0] if j < self.population_size - 1 else self.population[0][0]
            self.population[j] = [child1, self.calculate_fitness(child1)]
            self.population[j + 1] = [child2, self.calculate_fitness(child2)]
            i += 1
            j += 2
        self.update_population_fitness()

    def mutate_children(self, mutation_probability):
        number_of_mutations = round(mutation_probability * self.population_size)
        for _ in range(number_of_mutations):
            individual_index = random.randint(0, self.population_size - 1)
            mutation_value = random.uniform(-1, 1)
            self.population[individual_index][0] += mutation_value
            self.population[individual_index][1] = self.calculate_fitness(self.population[individual_index][0])
        self.update_population_fitness()

equation = "a + 2*b"
target_value = 30
error_range = 2
population_size = 10
i = 0
solution_info = None
ga_instance = GeneticAlgorithm(population_size, equation, target_value, error_range)
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
        if individual[1] <= error_range:
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
