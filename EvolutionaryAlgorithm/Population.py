import random
from Organism import Organism

class Population:
    def __init__(self, population_size, num_epochs, min_value, max_value, fitness_function):
        self.population = [Organism(random.randint(min_value, max_value), max_value, fitness_function) for _ in range(population_size)]
        self.num_epochs = num_epochs
        self.fitness_function = fitness_function
        self.global_minimum_fitness = 0.0

    def calculate_fitness(self):
        self.fitness = [self.fitness_function(org.chromosome_decimal) for org in self.population]

        # Apply transformation to shift all fitness values to non-negative range
        min_fitness = min(self.fitness)
        if min_fitness < self.global_minimum_fitness:
            self.global_minimum_fitness = min_fitness

        self.fitness = [fit - self.global_minimum_fitness for fit in self.fitness]

        self.minimum_fitness = min(self.fitness)
        self.average_fitness = sum(self.fitness) / len(self.fitness)
        self.maximum_fitness = max(self.fitness)