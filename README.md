# SpatialOptimization
Spatial  Optimization project at the ifgi in Münster <br/>
Code written by Niklas Aßelmann, Tom Niers, Nick Jakuschona, Mirjeta Musallaj

## Create the neede Enviroment (Once)
Open Anaconda Prompt (Windows) or Terminal (MacOS / Linux). <br/>
- Check if conda is available by typing: <br/>
conda --version 
- Now, create a new environment with python and Numpy installed: <br/>
conda create -n opti -y python==3.7 numpy 
- Activate the environment: <br/>
conda activate opti 
- Next, install the pymoo libr/ary: <br/>
pip install -U pymoo 
- Install pyyampl library: <br/>
pip install pyyaml

## Start your Enviroment and run the Code(Everytime you want to run the Optimization)
- If your Enviroment is createt you can start it with the conda command: <br/>
conda activate opti
- Then you have to navigate to the location where your script is stored with: <br/>
cd Your Path/SpatialOptimization
- Then run the scripts with: <br/>
python scriptXY.py


## Skripts
In this folder you find skripts to work with the data
- readData.py transforms the tif files to pcraster and npy files. You don`t have to run this skript, the processed Data is already uploaded
- calculate_objectives.py calculates our objectives (total revenue and vegetation area). To run this skript please set the working directory.
- spatial_crossover.py transform the croosover of the nsga II. Further information about NSGA-II: [https://doi.org/10.1109/4235.996017](https://doi.org/10.1109/4235.996017)
    - _constrained constraint the ratio between soy and pasture
- spatial_mutation.py transform the croosover of the nsga II. Further information about NSGA-II: [https://doi.org/10.1109/4235.996017](https://doi.org/10.1109/4235.996017)
    - _constrained constraint the ratio between soy and pasture
- run_nsga2_spatial.py runs the algorithm and save the results
- plot.py plots the initial landuse map and the two result maps. Furter plot possibilities in possible_plots.py

## Run Optimization
- Activate created Environment
- Set in every skript the default_directory
- Set the number of genartions in the run_nsga2_spatial.py skript
- run ``` python run_nsga2_spatial.py```
- The skript will transform unconstrained transformations with data from 2001

### Change to the constrained transformation
- spatial_extention.py
    - uncomment line 33 and 57
    - comment line 32 and 56

### Change the use Data to 2016
- calculate_objectives.py
    - uncomment line 13 and 14
    - comment line 11 and 12
- spatial_crossover.py / spatial_crossover_constrained.py
    - uncomment line 95 and 99
    - comment line 94 and 98
- spatial_mutation.py / spatial_mutation_constrained.py
    - uncomment line 53
    - comment line 52
- initial_population.py
    - uncomment line 10
    - comment line 9
- run_nsga2_spatial.py
    - specify result directory in line 76 and 77


### Use your own data
-  Thats a lot of work ...

