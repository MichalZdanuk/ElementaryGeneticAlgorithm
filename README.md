# EvolutionaryAlgorithm

## Cel projektu
Celem niniejszego projektu było stworzenie mini aplikacji umożliwiającej znalezienie maksimum funkcji dopasowania jednej zmiennej, zdefiniowanej dla liczb całkowitych w zadanym zakresie. Zadanie to zostało zrealizowane poprzez implementację podstawowego algorytmu genetycznego, wykorzystującego operacje takie jak:
* Reprodukcja z użyciem nieproporcjonalnej ruletki
* Krzyżowanie proste (z jednym punktem krzyżowania)
* Mutacja równomierna

Program pozwala na dostrojenie różnych parametrów, takich jak funkcja dopasowania, rozmiar populacji, liczba epok, prawdopodobieństwo krzyżowania oraz prawdopodobieństwo mutacji. Użytkownik ma możliwość ustawienia dowolnego zakresu min-max, jednak wartości te muszą być liczbami całkowitymi dodatnimi.

W przypadku, gdy zadana funkcja przystosowania przyjmuje wartości ujemne w zadanym zakresie algorytm radzi sobie z tym wykonując przesunięcie i ustawianie globalnego minimum. Wówczas wykres nie przedstawia rzeczywistych wartości przystosowań, lecz tendencje.

Dodatkowo, program zapewnia wizualizację wyników poprzez wykresy, które prezentują średnie, maksymalne i minimalne wartości przystosowania dla kolejnych epok populacji. Ponadto, przedstawiony jest również wykres analizowanej funkcji w określonym zakresie.

## DEMO
Poniżej prezentuję poszukiwania maksimum do zadanych przykładowych funkcji dopasowania:

* **PRZYKŁAD1:**
  
zadana funkcja: y = -0.4x^2 +10x + 5, min = 0, max = 25,

num_of_epos = 30, population_size = 5, crossing_rate = 0.95, mutation_rate = 0.001
![ex1](https://github.com/MichalZdanuk/ElementaryGeneticAlgorithm/assets/76063659/2f21406c-bc32-47d4-9415-0e08fb47b6a4)

![ex1_2](https://github.com/MichalZdanuk/ElementaryGeneticAlgorithm/assets/76063659/c5225f80-e7c5-4d2f-9c8a-34069795e82e)

* **PRZYKŁAD2:**

zadana funkcja: y = -0.1x^2 +13x + 5, min = 0, max = 100,

num_of_epos = 40, population_size = 5, crossing_rate = 0.95, mutation_rate = 0.001
![ex2](https://github.com/MichalZdanuk/ElementaryGeneticAlgorithm/assets/76063659/4f617e70-ad8e-49ee-afb6-922f549ba357)

![ex2_2](https://github.com/MichalZdanuk/ElementaryGeneticAlgorithm/assets/76063659/de3d2058-501c-4583-b81b-5690a742bbe2)
