# Search Algorithm Configuration

The calibration process utilizes a genetic algorithm. The configuration file includes parameters that allow users to tune the genetic algorithm for optimal performance.

- **population_size**: Defines the number of candidate solutions in each generation. A larger population increases diversity and enhances the search, but require more computational resources. Very small populations can reduce the genetic algorithm's ability to explore the solution space, potentially preventing it from finding the optimal solution.
- **generations**: Specifies the maximum number of iterations the algorithm can perform. Increasing this value allows more opportunities for improvement, but leads to longer runtimes. The calibration process will terminate early if a solution that meets the user's acceptance criteria is found before reaching this limit.
- **mutation_probability**: Determines the likelihood of random changes being introduced in offspring. Higher mutation rates encourage exploration of new solutions but may destabilize good candidates.
- **crossover_probability**: Specifies the probability that two parent solutions will combine to produce a child. Higher crossover rates encourage the exploitation of good solutions; however, excessive rates may reduce overall diversity.

## Optimizing Parameters: Practical Guidance

- **Testing with Small Values:** Employ reduced population sizes and fewer generations during initial testing phases to quickly validate code and workflow.
- **Calibration with Larger Values:** For full-scale calibration, increase both population_size and generations to achieve a more comprehensive search. We recommend population sizes between 30–100 and similar ranges for generations. Note that the effectiveness of larger population sizes or more generations depends on the number and granularity of available calibration adjustment knobs. If only a few knobs are being tuned, excessively large values may not provide meaningful improvements.
- **Balance Exploration and Intensification:**
    - if the search space is complex, consider increasing the crossover and mutation probabilities to ensure thorough exploration and solution coverage.
    - Higher crossover and mutation probabilities can enhance the algorithm's ability to investigate new search spaces, while lower probabilities tend to concentrate the search on refining and intensifying existing solutions.
    - Higher crossover and mutation probabilities may result in longer search time.
- **Evaluating Results:** Experiment with different parameter settings and compare outcomes to achieve an optimal balance between solution quality and computational efficiency.
- **Tune Based on Constraints:** When computational resources are limited, smaller populations, fewer generations, and smaller crossover and mutation probabilities may still yield useful results. It’s often necessary to experiment with different values to find the optimal values for a particular problem.

## Value Choices

These arrays contain the discrete options that the genetic algorithm will evaluate to calibrate the model. The values are multipliers of the element values in the hpxml model. 1 means the exact value that is in the original model. 0.1 means 1/10th of the original value. 10 means 10x the original value. Each home should have a custom config file for what is known about that home in particular. For instance, if a blower door test was completed on a home, you could probably have very small or no range for the air leakage choices in that home. We think a safe principle is to start with narrow ranges and few options the first time you attempt calibration of a home.

- Numbers farther away from 1 signify more uncertainty in the original model.
    - If those settings aren't able to generate a model that meets the acceptance criteria, try expanding the range.
        - Instead of `[0.5, 1, 2]`, consider `[0.25, 1, 4]`
- More values inside the array give the genetic algorithm more granularity to find a solution.
    - If the quality of the output isn't very good, more granularity could help.
        - Instead of `[0.5, 1, 2]`, consider `[0.5, 0.75, 1, 1.5, 2]`

### The choices in the config file adjust the following hpxml values

If your model doesn't contain any of them, that field is ignored.

### misc_load_multiplier_choices

- plug load
- fuel load
- pool pump usage
- pool heater usage
- permanent spa pump usage
- permanent spa heater usage

### air_leakage_multiplier_choices

- air leakage
- effective leakage area

### heating_efficiency_multiplier_choices

- heating efficiency afue
- heating efficiency percent
- heat pump hspf
- heat pump hspf2
- heat pump cop

### cooling_efficiency_multiplier_choices

- cooling efficiency seer
- cooling efficiency seer2
- cooling efficiency eer
- cooling efficiency ceer
- heat pump cooling efficiency seer
- heat pump cooling efficiency seer2
- heat pump cooling efficiency eer
- heat pump cooling efficiency ceer

### roof_r_value_multiplier_choices

- insulation assembly r value

### ceiling_r_value_multiplier_choices

- attic floor insulation assembly r value

### above_ground_walls_r_value_multiplier_choices

- above-ground walls and rim joists assembly r value

### below_ground_walls_r_value_multiplier_choices

- exterior insulation r value
- interior insulation r value
- assembly insulation r value

### slab_r_value_multiplier_choices

- under-slab insulation r value
- slab perimeter insulation r value
- slab exterior horizontal insulation r value
- slab gap insulation r value

### floor_r_value_multiplier_choices

- floor insulation assembly r value

### heating_setpoint_offset_choices

- heating setpoint
- heating setback
- wekday heating setpoints

### cooling_setpoint_offset_choices

- cooling setpoint
- cooling setback
- wekday cooling setpoints

### water_heater_efficiency_multiplier_choices

- water heater energy factor
- water heater uniform energy factor

### water_fixtures_usage_multiplier_choices

- water fixtures usage

### window_u_factor_multiplier_choices

- window u factor

### window_shgc_multiplier_choices

- window shgc

### appliance_usage_multiplier_choices

- appliance usage
    - refrigerators
    - clothes washers
    - clothes dryers
    - dishwashers
    - freezers
    - cooking ranges

### lighting_load_multiplier_choices

- interior lighting usage
