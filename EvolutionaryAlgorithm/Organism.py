class Organism:
    def __init__(self, value, max_value):
        self.value = value
        self.max_value = max_value

    @property
    def chromosome_binary(self):
        binary_string = bin(self.value)[2:]
        num_bits = len(bin(self.max_value)[2:])
        binary_string = '0' * (num_bits - len(binary_string)) + binary_string
        return binary_string

    @property
    def chromosome_decimal(self):
        return self.value

    def __str__(self):
        return f"Organism value: {self.value}, binary: {self.chromosome_binary}"