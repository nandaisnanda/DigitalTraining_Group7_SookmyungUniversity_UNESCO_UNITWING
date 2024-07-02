import random
import matplotlib.pyplot as plt

# Simulate rolling two fair dice
def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

# Count the number of times each sum appears
def simulate_dice_rolls(num_simulations):
    counts = {k: 0 for k in range(2, 13)}
    for _ in range(num_simulations):
        result = roll_dice()
        counts[result] += 1
    probabilities = {k: v / num_simulations for k, v in counts.items()}
    return probabilities

# Number of simulations
num_simulations = 100000
probabilities = simulate_dice_rolls(num_simulations)

# Print the probabilities
for k in range(2, 13):
    print(f"Sum = {k}, Probability = {probabilities[k]:.4f}")

# Plot the probabilities
plt.bar(probabilities.keys(), probabilities.values())
plt.xlabel('Sum of two dice')
plt.ylabel('Probability')
plt.title('Probability of sums of two dice')
plt.show()
