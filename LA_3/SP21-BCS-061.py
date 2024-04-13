import random
import math

class GA:
    def __init__(self, individualSize, populationSize):
        self.population = []
        self.individualSize = individualSize
        self.populationSize = populationSize
        self.totalFitness = 0

        for _ in range(populationSize):
            listOfBits = [random.randint(0, 1) for _ in range(individualSize)]
            numberOfOnes = sum(listOfBits)
            self.population.append([listOfBits, numberOfOnes])
            self.totalFitness += numberOfOnes

    def updatePopulationFitness(self):
        self.totalFitness = sum(individual[1] for individual in self.population)

    def selectParents(self):
        rouletteWheel = []
        wheelSize = self.populationSize * 5
        h_n = [individual[1] for individual in self.population]

        for j, individual in enumerate(self.population):
            individualLength = round(wheelSize * (h_n[j] / sum(h_n)))
            individualLength = max(individualLength, 1)
            rouletteWheel.extend([j] * individualLength)

        random.shuffle(rouletteWheel)
        parentIndices = random.sample(rouletteWheel, self.populationSize)

        newGeneration = [self.population[i].copy() for i in parentIndices]
        self.population = newGeneration
        self.updatePopulationFitness()

    def generateChildren(self, crossoverProbability):
        numberOfPairs = round(crossoverProbability * self.populationSize / 2)
        individualIndices = list(range(self.populationSize))
        random.shuffle(individualIndices)

        for i in range(0, numberOfPairs * 2, 2):
            crossoverPoint = random.randint(0, self.individualSize - 1)
            child1 = self.population[individualIndices[i]][0][:crossoverPoint] + \
                     self.population[individualIndices[i + 1]][0][crossoverPoint:]
            child2 = self.population[individualIndices[i + 1]][0][:crossoverPoint] + \
                     self.population[individualIndices[i]][0][crossoverPoint:]
            self.population[individualIndices[i]] = [child1, sum(child1)]
            self.population[individualIndices[i + 1]] = [child2, sum(child2)]

        self.updatePopulationFitness()

    def mutateChildren(self, mutationProbability):
        numberOfBits = round(mutationProbability * self.populationSize * self.individualSize)

        for _ in range(numberOfBits):
            individualIndex = random.randint(0, self.populationSize - 1)
            self.population[individualIndex][0] = [1 - bit for bit in self.population[individualIndex][0]]

        self.updatePopulationFitness()


individualSize, populationSize = 8, 10
i = 0
instance = GA(individualSize, populationSize)

while True:
    instance.selectParents()
    instance.generateChildren(0.8)
    instance.mutateChildren(0.03)

    print(f"\nGeneration {i}:")
    for idx, ind in enumerate(instance.population):
        print(f"Individual {idx}: {ind[0]} Fitness: {ind[1]}")

    print(f"Total Fitness: {instance.totalFitness}")

    i += 1
    maxFitness = max(ind[1] for ind in instance.population)

    if maxFitness == individualSize:
        print(f"\nSolution found in {i} iterations!")
        break