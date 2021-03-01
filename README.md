# Trade-Offs Between Maximizing the Agricultural Profit and the Area of Natural Vegetation in Mato Grosso, Brazil

## Abstract 
Despite numerous efforts and regulations by the government, deforestation in the Brazilian rainforest, especially in the state of Mato Grosso, continues inexorably. 
The key reason for this development is the fact that the region has increasingly become one of the major players in the world's supplier of Soy and Beef. 
In this work, we report on how computing a Spatial Optimization, based on the classic NSGA2 algorithm, can reveal the trade-offs between these two conflicting poles and what they look like.
In principle, it must be assumed that if the agricultural profit should have been increased by one million US dollars there must have been a minimal loss of 7.7 ha in 2001 and 7.2 ha in 2016 of natural vegetation. 
Nevertheless, our calculations have shown that despite the application of governmental regulations and the existence of protected areas, agricultural profit can be increased without reducing the area of natural vegetation and vice versa in relation to the initial land use of our study area in Mato Grosso in 2001 and 2016. 
Thereby, setting the focus on soy as crop in the north of the study area, a renaturation of agricultural non-productive areas, as well as the expansion of agricultural processing infrastructure, is beneficial. 

This software was developed as part of the study project "Spatial Optimization" in the winterterm 2020/21 at [ifgi](https://www.uni-muenster.de/Geoinformatics/en/index.html) at the [University of Münster](https://www.uni-muenster.de/en/). 
Below there is a How-To, which explains all the necessary steps to perform the optimization.

## How-To 
### Create the neede Enviroment (must be performed only once)
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

### Start your Enviroment and run the Code (everytime you want to run the optimization)
- If your Enviroment is createt you can start it with the conda command: <br/>
conda activate opti
- Then you have to navigate to the location where your script is stored with: <br/>
cd ../SpatialOptimization/skripts
- Set the wanted configurations in the config.yaml file
- Then run the scripts with: <br/>
python scriptXY.py
- The main script is run_nsga2_spatial.py

## Folders
### Scripts
In the folder scripts you find scripts to work with the data
- readData.py transforms the tif files to pcraster and npy files. You do not have to run this skript, the processed Data is already uploaded in the folder `/data/finalData`
- calculate_objectives.py calculates our objectives (total revenue and vegetation area). To run this skript please set the working directory.
    - 2001 use the transport distances from 2001
    - 2016 use the transport distances from 2016
- spatial_crossover.py transform the crossover of the nsga II. Further information about NSGA-II: [https://doi.org/10.1109/4235.996017](https://doi.org/10.1109/4235.996017)
- spatial_mutation.py transform the crossover of the nsga II. Further information about NSGA-II: [https://doi.org/10.1109/4235.996017](https://doi.org/10.1109/4235.996017)
- run_nsga2_spatial.py runs the algorithm and save the results
- plot.py plots the initial landuse map, the Pareto Front and the two extreme land use maps. Furthermore it shows how the area can be optimized. It indicates the points on the Pareto Front and the associated land use maps. Last it shows how the Pareto Front developed over generations and the Hypervolume. It shows data from the year which is specified in the config.yaml
- plot_both.py plots both Pareto Fronts at ones. Furthermore it shows how the profit can be optimized while keeping the are of natural vegetation of the inital map from 2016. Here it compares the optimized values for the different optimizations (2001 and 2016), while showing the values and associted land use maps.
- config.yaml to set the parameters for the optimization (e.g. population size, generations). Besides you can also set for the constraint concerning the governmental restrictions how much area of forest and cerrado (in %) needs to remain in each optimization step. The variables are intially already filled with values we used.
### Data
- In the folder "finalData" all data is stored which we finally used after preprocessing 
- Thus, these data were already appropriately tailored to the study area, the cell size was adjusted, the coordinate system was adjusted, and all data were converted to raster format
- If you are interested in the raw data just contact us
### Results
In this folder you find the results of an opimization with the paramters specified in the config.yaml. 
- 2001 contains the result for 2001
- 2016 contains the result for 2016

### Graphics
This folder contains a selection of graphics, which were produced by the plot.py or plot_both.py file



