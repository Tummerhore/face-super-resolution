# Hochschule Karlsruhe: Autonome Systeme Labor SS20 - Face Super-Resolution (Jetson Nano)

## Requirements

- Python 3.6
- Pipenv (`pip install pipenv`)
- To install the face-recognition package, CMake

## Start the program

1. Install dependencies (`pipenv install`)
2. Run the program (`pipenv run python src/main.py`)

### Dependencies on Jetson

As the Jetson is using an ARM architecture, some dependencies may not be easily installable trough pip. The following links may help if you run into problems during dependency installation:

- Pytorch: https://forums.developer.nvidia.com/t/pytorch-for-jetson-nano-version-1-5-0-now-available/72048