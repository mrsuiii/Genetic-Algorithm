# Magic Cube Solver - Genetic Algorithm

This project provides a genetic algorithm-based solution for solving the Magic Cube problem. The Magic Cube is a 3D cube filled with numbers, where the sum of each row, column, pillar, and diagonal must equal a predefined magic number. This algorithm aims to find the optimal configuration of numbers to satisfy the Magic Cube conditions.

## Features of the Magic Cube

A Magic Cube is structured such that:
- Each row, column, and pillar (in all 3 dimensions) sums up to a specific magic number.
- All diagonals across planes and space also sum up to this magic number.

The solver in this project uses a genetic algorithm to iteratively optimize the arrangement of numbers in the cube to meet these conditions.

## Genetic Algorithm

The genetic algorithm (GA) implemented here follows these steps:
1. **Initialization**: Generates an initial population of possible solutions.
2. **Selection**: Selects parent solutions based on their scores (how close they are to solving the Magic Cube).
3. **Crossover**: Combines parts of two parents to create new offspring solutions, with variations in crossover methods.
4. **Mutation**: Randomly changes parts of offspring solutions to introduce diversity.
5. **Termination**: The algorithm runs for a set number of iterations, or until it finds an optimal solution.

## Dependencies

- **Python**: Ensure you have Python installed.
- **NumPy**: For efficient numerical computations.
- **Matplotlib**: To visualize the algorithm's progress (e.g., plot of scores over iterations).

Install the dependencies using:
```bash
pip install numpy matplotlib
```
## Usage

 ```python
#import the GeneticAlgorithm from genetic_paralel
from genetic_paralel import GeneticAlgorithm

# Set parameters
population_size = 100
max_iterations = 1000

# Create instance of GeneticAlgorithm
solver = GA_solver(population_size=population_size, iterations=max_iterations, shuffle=True)

# Run the algorithm
solution = solver.solve()

# Display results
print("Best configuration found:", solution["best_config"])
print("Best score achieved:", solution["iteration_scores"][-1][0])  # Last best score in iteration history
print("Elapsed time:", solution["elapsed_time"])
 ```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Author

mrsuiii