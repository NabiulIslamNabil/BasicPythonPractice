# S. M. Nabiul Islam
# 0112230261
# Simulated Annealing Seating Arrangement

import random
import math

guest_labels = ['A', 'B', 'C', 'D', 'E']

conflict_matrix = [
    [0, 4, 6, 1, 1],
    [4, 0, 2, 8, 1],
    [6, 2, 0, 1, 7],
    [1, 8, 1, 0, 5],
    [1, 1, 7, 5, 0]
]

def calculate_score(arrangement):
    total_score = 0
    n = len(arrangement)
    for i in range(n):
        total_score += conflict_matrix[arrangement[i]][arrangement[(i + 1) % n]]
    return total_score


def simulated_annealing(initial_arrangement, initial_temperature, cooling_rate, max_iterations):
    current_arrangement = initial_arrangement[:]
    current_score = calculate_score(current_arrangement)
    best_arrangement = current_arrangement[:]
    best_score = current_score
    temperature = initial_temperature
    
    initial_label = [guest_labels[i] for i in current_arrangement]
    print(f"Iteration 0: Current Score = {current_score}, Best Score = {best_score}", initial_label)
    

    for iteration in range(max_iterations+1):
        neighbor = current_arrangement[:]
        i, j = random.sample(range(len(neighbor)), 2)
        neighbor[i], neighbor[j] = neighbor[j], neighbor[i]

        neighbor_score = calculate_score(neighbor)
        delta_score = neighbor_score - current_score

        if delta_score < 0 or random.random() < math.exp(-delta_score / temperature):
            current_arrangement = neighbor
            current_score = neighbor_score

        if current_score < best_score:
            best_arrangement = current_arrangement[:]
            best_score = current_score
            

        temperature *= cooling_rate
        current_arrangement_labels = [guest_labels[i] for i in current_arrangement]
        if (iteration % 2 == 0 or iteration == max_iterations) and iteration!=0:
            if current_score > best_score:
                print(f"Iteration {iteration}: Current Score = {current_score}, Best Score = {best_score}", current_arrangement_labels, "BAD")
            else:
                print(f"Iteration {iteration}: Current Score = {current_score}, Best Score = {best_score}", current_arrangement_labels, "GOOD")
            

    return best_arrangement, best_score


initial_arrangement = [2, 0, 1, 3, 4] #C, A, B, D, E
initial_temperature = 100
cooling_rate = 0.95
max_iterations = 99

initalScore = calculate_score(initial_arrangement)
print("The initial score for the arrangement [2(C), 0(A), 1(B), 3(D), 4(E)] is: ", initalScore)

optimal_arrangement, minimum_score = simulated_annealing(
    initial_arrangement,
    initial_temperature,
    cooling_rate,
    max_iterations
)

optimal_arrangement_labels = [guest_labels[i] for i in optimal_arrangement]

print("\nOptimal Seating Arrangement:", optimal_arrangement_labels)
print("Minimum Conflict Score:", minimum_score)
