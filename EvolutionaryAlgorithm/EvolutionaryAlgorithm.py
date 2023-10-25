# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
import numpy as np

from Population import Population
from Organism import Organism

class EvolutionaryAlgorithm:
    fitness_per_epoch = []

    def __init__(self, population, num_epochs, crossing_rate, mutation_rate, min_value, max_value):
        self.population = population
        self.num_epochs = num_epochs
        self.crossing_rate = crossing_rate
        self.mutation_rate = mutation_rate
        self.min_value = min_value
        self.max_value = max_value
        self.best_organism = None

    def reproduction(self):
        self.population.calculate_fitness()
        adaptation_values = self.population.fitness
        total_adaptation = sum(adaptation_values)
        probabilities = [adaptation / total_adaptation for adaptation in adaptation_values]

        new_population = []
        for _ in range(len(self.population.population)):
            selected = random.choices(self.population.population, probabilities)[0]
            new_population.append(selected)

        self.population.population = new_population

    def crossing(self):
        new_population = []

        while len(self.population.population) >= 2:
            org1 = random.choice(self.population.population)
            self.population.population.remove(org1)
            org2 = random.choice(self.population.population)
            self.population.population.remove(org2)

            rand_num = random.random()

            if rand_num <= self.crossing_rate:
                crossing_position = random.randint(1, 4)

                new_org1_binary = org1.chromosome_binary[:crossing_position] + org2.chromosome_binary[crossing_position:]
                new_org2_binary = org2.chromosome_binary[:crossing_position] + org1.chromosome_binary[crossing_position:]
                new_org1_decimal = int(new_org1_binary, 2)
                new_org2_decimal = int(new_org2_binary, 2)             

                if new_org1_decimal < self.min_value or new_org1_decimal > self.max_value:
                    new_org1_decimal = random.randint(self.min_value, self.max_value)
                if new_org2_decimal < self.min_value or new_org2_decimal > self.max_value:
                    new_org2_decimal = random.randint(self.min_value, self.max_value)

                new_population.append(Organism(new_org1_decimal, self.max_value))
                new_population.append(Organism(new_org2_decimal, self.max_value))
            else:
                new_population.append(org1)
                new_population.append(org2)

        if len(self.population.population) == 1:
            new_population.append(self.population.population[0])

        self.population.population = new_population

    def mutation(self):
        new_population = []

        for org in self.population.population:
            new_org_binary = ''
            for bit in org.chromosome_binary:
                rand_num = random.random()
                if rand_num <= self.mutation_rate:
                    new_org_binary += '0' if bit == '1' else '1'
                else:
                    new_org_binary += bit

            new_org_decimal = int(new_org_binary, 2)

            if new_org_decimal < self.min_value or new_org_decimal > self.max_value:
                new_org_decimal = random.randint(self.min_value, self.max_value)

            new_population.append(Organism(new_org_decimal, self.max_value))

        self.population.population = new_population

    def run_evolution(self):
        for epoch in range(self.num_epochs):
            self.reproduction()
            self.crossing()
            self.mutation()
            self.population.calculate_fitness()

            current_maximum_fitness = self.population.maximum_fitness
            current_best_organism = next(org for org in self.population.population if self.population.fitness_function(org.chromosome_decimal) == current_maximum_fitness)

            if self.best_organism is None or self.population.fitness_function(self.best_organism.chromosome_decimal) < current_maximum_fitness:
                self.best_organism = current_best_organism

            self.fitness_per_epoch.append({
                "minimum_fitness": self.population.minimum_fitness,
                "average_fitness": self.population.average_fitness,
                "maximum_fitness": self.population.maximum_fitness
            })

        return self.fitness_per_epoch, self.best_organism


def given_fitness_function(x):
    return -0.4*x*x+10*x+5

print("--------------------------------")
print("Project - evolutionary algorithm")
print("--------------------------------")
MIN_VALUE = 0
MAX_VALUE = 25
NUM_OF_EPOCHS = 30
POPULATION_SIZE = 5
CROSSING_RATE = 0.95
MUTATION_RATE = 0.001

population = Population(population_size=POPULATION_SIZE, num_epochs=NUM_OF_EPOCHS, min_value=MIN_VALUE, max_value=MAX_VALUE, fitness_function=given_fitness_function)
evolution_algorithm = EvolutionaryAlgorithm(population, population.num_epochs, crossing_rate=CROSSING_RATE, mutation_rate=MUTATION_RATE, min_value=MIN_VALUE, max_value=MAX_VALUE)
fitness_per_epoch, best_organism = evolution_algorithm.run_evolution()
for i, fitness in enumerate(fitness_per_epoch):
    formatted_epoch = f"{i + 1:02}"
    formatted_min_fitness = f"{fitness['minimum_fitness']:.6f}"
    formatted_avg_fitness = f"{fitness['average_fitness']:.6f}"
    formatted_max_fitness = f"{fitness['maximum_fitness']:.6f}"
    print(f"Epoch {formatted_epoch}: Minimum Fitness: {formatted_min_fitness}, Average Fitness: {formatted_avg_fitness}, Maximum Fitness: {formatted_max_fitness}")

print("---------------")
print("Best Organism:")
print("---------------")
print(best_organism)
print(f"Fitness: {population.fitness_function(best_organism.chromosome_decimal)}")

epochs = list(range(1, len(fitness_per_epoch) + 1))
min_fitness = [fitness["minimum_fitness"] for fitness in fitness_per_epoch]
avg_fitness = [fitness["average_fitness"] for fitness in fitness_per_epoch]
max_fitness = [fitness["maximum_fitness"] for fitness in fitness_per_epoch]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# First plot - Fitness in Populations
ax1.plot(epochs, min_fitness, label='Minimum Fitness')
ax1.plot(epochs, avg_fitness, label='Average Fitness')
ax1.plot(epochs, max_fitness, label='Maximum Fitness')
ax1.set_title('Fitness in Populations')
ax1.set_xlabel('Population')
ax1.set_ylabel('Fitness')
ax1.legend()

# Second plot - Function Plot
x = np.arange(MIN_VALUE, MAX_VALUE+1)
y = -0.4 * x * x + 10 * x + 5
ax2.plot(x, y, label='Fitness Function')
ax2.set_title('Fitness Function: y=-0.4x^2 + 10x + 5')
ax2.set_xlabel('Input Values')
ax2.set_ylabel('Fitness')
ax2.legend()

plt.show()