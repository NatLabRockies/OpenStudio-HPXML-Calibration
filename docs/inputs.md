# Inputs

## Utility consumption

If not included in the hpxml already, we can add it from a csv:

- An example file can be found at [tests/data/test_bills.csv](https://github.com/NatLabRockies/OpenStudio-HPXML-Calibration/blob/main/tests/data/test_bills.csv)
- It has this format:

| Consumption | StartDateTime | EndDateTime | UnitofMeasure | FuelType  |
|:-----------:|:-------------:|:-----------:|:-------------:|:---------:|
|1000         | 2/1/23        | 2/28/23     |kWh            |electricity|
|1000         | 3/1/23        | 3/31/23     |kWh            |electricity|
|120          | 1/1/23        | 1/31/23     |therms         |natural gas|

## Config file

- The default config can be found at [src/openstudio_hpxml_calibration/default_calibration_config.yaml](https://github.com/NatLabRockies/OpenStudio-HPXML-Calibration/blob/main/src/openstudio_hpxml_calibration/default_calibration_config.yaml)
- The default file should not be altered. Create an override config specific for each home
- An example override config can be found at [tests/data/test_config.yaml](https://github.com/NatLabRockies/OpenStudio-HPXML-Calibration/blob/main/tests/data/test_config.yaml)
