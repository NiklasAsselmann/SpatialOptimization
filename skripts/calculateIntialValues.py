from pcraster import *
from pcraster.framework import *
import numpy as np

default_directory = "C:/Users/nick1/OneDrive - uni-muenster.de/Master/Semester1/SpatiOptmi/SpatialOptimization/"

land_use_map_2001 = np.load(default_directory + "/data/finalData/npy/landuse_2001.npy")
land_use_map_2016 = np.load(default_directory + "/data/finalData/npy/landuse_2016.npy")


forest_area_2001 = np.count_nonzero(land_use_map_2001 == 1)
cerrado_area_2001 = np.count_nonzero(land_use_map_2001 == 2)
soy_area_2001 = np.count_nonzero(land_use_map_2001 == 4)
pasture_area_2001 = np.count_nonzero(land_use_map_2001 == 7)
forest_area_2016 = np.count_nonzero(land_use_map_2016 == 1)
cerrado_area_2016 = np.count_nonzero(land_use_map_2016 == 2)
soy_area_2016 = np.count_nonzero(land_use_map_2016 == 4)
pasture_area_2016 = np.count_nonzero(land_use_map_2016 == 7)

forest_area_min_2001 = forest_area_2001 * 0.8
cerrado_area_min_2001  = cerrado_area_2001 * 0.35
forest_area_min_2016 = forest_area_2016 * 0.8
cerrado_area_min_2016  = cerrado_area_2016 * 0.35

ratio_2001 = pasture_area_2001/soy_area_2001
ratio_2016 = pasture_area_2016/soy_area_2016

print(forest_area_2001, cerrado_area_2001)

print(forest_area_min_2001, cerrado_area_min_2001)
print(forest_area_min_2016, cerrado_area_min_2016)
#landuse = [landuse]