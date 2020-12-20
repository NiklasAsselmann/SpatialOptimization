# SpatialOptimization
Spatial  Optimization project at the ifgi in Münster <br/>
Code written by Niklas Aßelmann, Tom Niers, Nick Jakuschona, Mirjeta Musallaj

## Create the neede Enviroment (Once)
Open Anaconda Prompt (Windows) or Terminal (MacOS / Linux). <br/>
- Check if conda is available by typing:
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