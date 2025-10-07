# Getting Started

Generate an HPXML model of home energy use, calibrated to utility data.

!!! note "Nearly everyone will interact solely with the command line interface"
    Custom workflows can be built using the classes & methods. See the `Code Documentation` section for more information. For advanced users only.

- `openstudio-hpxml-calibration --help`
- Or the short version: `oshc -h`

## [Required inputs](inputs.md)

- [Measured consumption data](inputs.md#config-file):
    - In the HPXML model, or
    - A CSV file of utility data
- A [config file](inputs.md#config-file) specific to the home being calibrated

## Usage instructions

1. Use the `calibrate` command of the app. Required parameters:
    - path to hpxml file
    - path to the config file for that home

    `oshc calibrate --hpxml-filepath path/to/asdf.xml --config-filepath path/to/qwer.yml`

1. Optional parameters for the `calibrate` command:
    - path to csv of consumption data (if using that technique)
    - path to output-dir: to save in a custom location
    - num-proc: integer number of processor cores to use for parallel simulations
    - save-all-results: flag to capture all intermediate steps. Useful for debugging
    - verbose: flag to enable more verbose logging during operation. Can be repeated for increased output

    `oshc calibrate --hpxml-filepath path/to/asdf.xml --config-filepath path/to/qwer.yml --csv-bills-filepath path/to/bcde.csv --output-dir path/to/test_output --num-proc 8 --save-all-results --verbose --verbose`

## Outputs

- A folder for each generation of the calibration search, with the best individual HPXML model of the generation.
- `logbook.json` which captures the outputs at each generation, including the value choices of the best individual, the simulation results for that individual, and the corresponding error values.
- `best_individual.xml` model, the calibrated model which meets the acceptance criteria set in the config file.
- Plots showing weather normalization (if using detailed calibration) and calibration search.
