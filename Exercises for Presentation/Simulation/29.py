import random

# Simulate flipping 3 fair coins
def flip_coins():
    return [random.choice(['H', 'T']) for _ in range(3)]

# Count the number of times two coins land heads and one lands tails
def simulate_flips(num_simulations):
    two_heads_one_tail = 0
    for _ in range(num_simulations):
        result = flip_coins()
        if result.count('H') == 2 and result.count('T') == 1:
            two_heads_one_tail += 1
    return two_heads_one_tail / num_simulations

# Number of simulations
num_simulations = 100000
probability = simulate_flips(num_simulations)
print(probability)
