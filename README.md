# SpatialOptimization
Spatial  Optimization project at the ifgi in Münster
Code written by Niklas Aßelmann,

## Create the neede Enviroment (Once)
Open Anaconda Prompt (Windows) or Terminal (MacOS / Linux). 
-Check if conda is available by typing:
conda --version 
-Now, create a new environment with python and Numpy installed:
conda create -n opti -y python==3.7 numpy 
-Activate the environment:
conda activate opti 
-Next, install the pymoo library:
pip install -U pymoo 

## Start your Enviroment and run the Code(Everytime you want to run the Optimization)
-If your Enviroment is createt you can start it with the conda command:
conda activate opti
- Then you have to navigate to the location where your script is stored with:
cd Your Path/SpatialOptimization
- Then run the scripts with:
python scriptXY.py