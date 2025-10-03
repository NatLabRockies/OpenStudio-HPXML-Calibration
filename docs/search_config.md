# Search Algorithm Configuration

The calibration process utilizes a genetic algorithm. The configuration file includes parameters that allow users to tune the genetic algorithm for optimal performance.

- **population_size**: Defines the number of candidate solutions in each generation. A larger population increases diversity and enhances the search, but require more computational resources. Very small populations may lead to premature convergence.
- **generations**: Specifies the maximum number of iterations the algorithm can perform. Increasing this value allows more opportunities for improvement, but leads to longer runtimes. The calibration process will terminate early if an optimal solution is found before reaching this limit.
- **mutation_probability**: Determines the likelihood of random changes being introduced in offspring. Higher mutation rates encourage exploration of new solutions but may destabilize good candidates.
- **crossover_probability**: Specifies the probability that two parent solutions will combine to produce a child. Higher crossover rates encourage the exploitation of good solutions; however, excessive rates may reduce overall diversity.

## Optimizing Parameters: Practical Guidance

- **Testing with Small Values:** Employ reduced population sizes and fewer generations during initial testing phases to quickly validate code and workflow.
- **Calibration with Larger Values:** For full-scale calibration, increase both population_size and generations to achieve a more comprehensive search. Studies recommend population sizes between 30–100 and similar ranges for generations, particularly for building energy applications.
- **Balance Exploration and Intensification:**
    - if the search space is complex, consider increasing the crossover and mutation probabilities to ensure thorough exploration and solution coverage.
    - Higher crossover and mutation probabilities can enhance the algorithm's ability to investigate new search spaces, while lower probabilities tend to concentrate the search on refining and intensifying existing solutions.
    - Higher crossover and mutation probabilities may result in longer search time.
- **Evaluating Results:** Experiment with different parameter settings and compare outcomes to achieve an optimal balance between solution quality and computational efficiency.
- **Tune Based on Constraints:** When computational resources are limited, smaller populations, fewer generations, and smaller crossover and mutation probabilities may still yield useful results. It’s often necessary to experiment with different values to find the optimal values for a particular problem.
