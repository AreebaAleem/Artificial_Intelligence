import random
import string

class GeneticAlgorithm:
    def __init__(self, population_size, target_string):
        self.population = []
        self.population_size = population_size
        self.target_string = target_string
        self.total_fitness = 0
        self.generate_initial_population()

    def generate_initial_population(self):
        for _ in range(self.population_size):
            chromosome = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation + ' ') 
                                 for _ in range(len(self.target_string)))
            self.population.append([chromosome, self.calculate_fitness(chromosome)])
            self.total_fitness += self.population[-1][1]

    def calculate_fitness(self, chromosome):
        return sum(1 for c1, c2 in zip(chromosome, self.target_string) if c1 == c2)

    def update_population_fitness(self):
        self.total_fitness = sum(individual[1] for individual in self.population)

    def select_parents(self):
        roulette_wheel = []
        wheel_size = int(self.population_size * 5)
        fitness_scores = [ind[1] for ind in self.population]
        for ind in self.population:
            individual_length = round(wheel_size * (ind[1] / sum(fitness_scores)))
            if individual_length > 0:
                roulette_wheel.extend([ind] * individual_length)
        random.shuffle(roulette_wheel)
        parent_indices = random.choices(roulette_wheel, k=self.population_size)
        self.population = [ind.copy() for ind in parent_indices]
        self.update_population_fitness()

    def generate_children(self, crossover_probability):
        number_of_pairs = round(crossover_probability * self.population_size / 2)
        random.shuffle(self.population)
        for i in range(0, number_of_pairs * 2, 2):
            crossover_point = random.randint(1, len(self.target_string) - 1)
            child1 = self.population[i][0][:crossover_point] + self.population[i + 1][0][crossover_point:]
            child2 = self.population[i + 1][0][:crossover_point] + self.population[i][0][crossover_point:]
            self.population[i] = [child1, self.calculate_fitness(child1)]
            self.population[i + 1] = [child2, self.calculate_fitness(child2)]
        self.update_population_fitness()

    def mutate_children(self, mutation_probability):
        for ind in self.population:
            for i in range(len(ind[0])):
                if random.random() < mutation_probability:
                    ind[0] = ind[0][:i] + random.choice(string.ascii_letters + string.digits + string.punctuation + ' ') + ind[0][i + 1:]
            ind[1] = self.calculate_fitness(ind[0])
        self.update_population_fitness()

# Example usage
target_string = "hello"
population_size = 8
i = 0
solution_info = None
ga_instance = GeneticAlgorithm(population_size, target_string)
while True:
    ga_instance.select_parents()
    ga_instance.generate_children(0.8)
    ga_instance.mutate_children(0.03)
    print(ga_instance.population)
    print("Total fitness: " + str(ga_instance.total_fitness))
    print("Total iterations: " + str(i))
    i += 1
    found = any(ind[1] == len(target_string) for ind in ga_instance.population)
    if found:
        solution_info = {
            "Iteration": i,
            "Total fitness": ga_instance.total_fitness,
            "Population": ga_instance.population
        }
        break

if solution_info:
    print("Solution found:")
    print(solution_info)
else:
    print("No solution found within the given iterations.")
