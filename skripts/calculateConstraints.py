from pcraster import *
from pcraster.framework import *
import numpy as np
import yaml

# Read config.yaml file
with open("config.yaml", 'r') as stream:
    yamlData = yaml.safe_load(stream)

directory = yamlData["directory"]
year = yamlData["optimization"]["year"]
forestRemain = yamlData["optimization"]["areaForestRemains"]
cerradoRemain = yamlData["optimization"]["areaCerradoRemains"]

default_directory = directory

#calculate the area of forest and cerrado that has to remain
def calculate_constraints():
    if year==2001:
        land_use_map_in = np.load(default_directory + "/data/finalData/npy/landuse_2001.npy")
    elif year == 2016:
        land_use_map_in = np.load(default_directory + "/data/finalData/npy/landuse_2016.npy")
    else:
        raise ValueError("Year must be 2001 or 2016")
        
    #calculate actual area
    forest_area = np.count_nonzero(land_use_map_in== 1)
    cerrado_area= np.count_nonzero(land_use_map_in == 2)

    #calculate are that has to remain
    forest_area_min = forest_area * forestRemain
    cerrado_area_min  = cerrado_area * cerradoRemain

    return([forest_area_min, cerrado_area_min])