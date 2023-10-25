import random
from Organism import Organism

class Population:
    def __init__(self, population_size, num_epochs, min_value, max_value, fitness_function):
        self.population = [Organism(random.randint(min_value, max_value), max_value) for _ in range(population_size)]
        self.num_epochs = num_epochs
        self.fitness_function = fitness_function

    def calculate_fitness(self):
        self.fitness = [self.fitness_function(org.chromosome_decimal) for org in self.population]
        self.minimum_fitness = min(self.fitness)
        self.average_fitness = sum(self.fitness) / len(self.fitness)
        self.maximum_fitness = max(self.fitness)