import random
import math

class GA:
    def __init__(self, individualSize, populationSize):
        self.population = {}
        self.individualSize = individualSize
        self.populationSize = populationSize
        self.totalFitness = 0
        self.initializePopulation()

    def initializePopulation(self):
        for i in range(self.populationSize):
            listOfBits = [1] * self.individualSize
            self.population[i] = [listOfBits, self.individualSize]
            self.totalFitness += self.individualSize

    def updatePopulationFitness(self):
        self.totalFitness = 0
        for individual in self.population:
            individualFitness = sum(self.population[individual][0])
            self.population[individual][1] = individualFitness
            self.totalFitness += individualFitness

    def selectParents(self):
        rouletteWheel = []
        wheelSize = self.populationSize * 5
        h_n = [self.population[individual][1] for individual in self.population]

        for j, individual in enumerate(self.population):
            individualLength = round(wheelSize * (h_n[j] / sum(h_n)))

            if individualLength > 0:
                rouletteWheel.extend([individual] * individualLength)

        random.shuffle(rouletteWheel)
        parentIndices = [random.randint(0, len(rouletteWheel) - 1) for _ in range(self.populationSize)]
        newGeneration = {i: self.population[rouletteWheel[parentIndex]].copy() for i, parentIndex in enumerate(parentIndices)}

        self.population = newGeneration
        self.updatePopulationFitness()

    def generateChildren(self, crossoverProbability):
        numberOfPairs = round(crossoverProbability * self.populationSize / 2)
        individualIndices = list(range(0, self.populationSize))
        random.shuffle(individualIndices)
        i = 0
        j = 0
        while i < numberOfPairs:
            crossoverPoint = random.randint(0, self.individualSize - 1)
            child1 = self.population[j][0][0:crossoverPoint] + self.population[j + 1][0][crossoverPoint:]
            child2 = self.population[j + 1][0][0:crossoverPoint] + self.population[j][0][crossoverPoint:]
            self.population[j] = [child1, sum(child1)]
            self.population[j + 1] = [child2, sum(child2)]
            i += 1
            j += 2
        self.updatePopulationFitness()

    def mutateChildren(self, mutationProbability):
        numberOfBits = round(mutationProbability * self.populationSize * self.individualSize)
        totalIndices = list(range(0, self.populationSize * self.individualSize))
        random.shuffle(totalIndices)
        swapLocations = random.sample(totalIndices, numberOfBits)

        for loc in swapLocations:
            individualIndex = math.floor(loc / self.individualSize)
            bitIndex = loc % self.individualSize

            self.population[individualIndex][0][bitIndex] = 1 - self.population[individualIndex][0][bitIndex]

        self.updatePopulationFitness()


individualSize, populationSize = 8, 10
i = 0
instance = GA(individualSize, populationSize)

while True:
    instance.selectParents()
    instance.generateChildren(0.8)
    instance.mutateChildren(0.03)

    print(instance.population)
    print(instance.totalFitness)
    print(i)

    i += 1
    found = any(individual[1] == individualSize for individual in instance.population.values())

    if found:
        print("Solution found!")
        break