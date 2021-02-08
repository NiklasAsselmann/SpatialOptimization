# Spatial Optimization Approach to analyse the Impact of Minimizing Transport Distances within the Supply Chains of Agricultural Cultivation and Livestock Farming on the Agricultural Profit and the Area of Natural Vegetation in Mato Grosso, Brazil. 

For this purpose, an NSGA-II optimization is performed to investigate: 

1. How can the study area be used to maximize the agricultural profit but to keep or increase the area of natural vegetation?
2. Which effect has minimizing the transport distances within the supply chains of agricultural cultivation and livestock farming on the gained profit and the land consumption of natural vegetation?

A more detailed explanation of Objectives, Control Variables, Constraints and Implementation will be available here shortly. 
This software was developed as part of the study project "Spatial Optimization" in the winterterm 2020/21 at [ifgi](https://www.uni-muenster.de/Geoinformatics/en/index.html) at the [University of Münster](https://www.uni-muenster.de/en/). 

# How-To 
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

## Start your Enviroment and run the Code(Everytime you want to run the Optimization)
- If your Enviroment is createt you can start it with the conda command: <br/>
conda activate opti
- Then you have to navigate to the location where your script is stored with: <br/>
cd Your Path/SpatialOptimization
- Then run the scripts with: <br/>
python scriptXY.py


## Scripts
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

