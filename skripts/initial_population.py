import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import yaml

# Read config.yaml file
with open("config.yaml", 'r') as stream:
    yamlData = yaml.safe_load(stream)



default_directory = yamlData["directory"]
year = yamlData["optimization"]["year"]
forestRemain = yamlData["optimization"]["areaForestRemains"]
cerradoRemain = yamlData["optimization"]["areaCerradoRemains"]
protectedArea = np.load(default_directory +"data/finalData/npy/protectedArea.npy")
from calculateConstraints import calculate_constraints

minAreas = calculate_constraints()
minForestArea = minAreas[0]
minCerradoArea = minAreas[1]

# make initial population for genetic algorithm
def initialize_spatial(pop_size,default_directory):
 all_landusemaps = []
 # read land use map dedending on the year
 if year==2001:
        landuse_map_in = np.load(default_directory + "/data/finalData/npy/landuse_2001.npy")
 elif year == 2016:
        landuse_map_in = np.load(default_directory + "/data/finalData/npy/landuse_2016.npy")
 rows = landuse_map_in.shape[0]
 cols = landuse_map_in.shape[1]
 landuse_map_in2 = landuse_map_in.copy()
 # transform land use inside protected areas to new land use class
 for x in range(0, cols-1):
    for y in range(0, rows-1):
        if protectedArea[y, x] == 1:
            landuse_map_in2[y,x] = 20

 # iterate to get multiple realizations for the initial population
 for i in range(1,pop_size+1):
 #use uniform distribution to select 30% of the cells 
    landuse_map_ini = np.zeros((rows,cols),dtype='uint8')
    random_map = np.random.uniform(0.0,1.0,(rows,cols))
    random_map_mw = np.zeros((rows,cols))
    #print(random_map_mw.shape)

 # take window average of random map to create larger patches
    
    for x in range(0, cols-2):
        for y in range(0,rows):
            if x == 0 or y == 0 or x == cols-1 or y == rows-1:
                random_map_mw[y,x] = 1.0
            else:
                random_map_mw[y,x] = random_map[y-1:y+2,x-1:x+2].mean()

    # 70% of the map remains the current land use
    landuse_map_ini = np.where(random_map_mw>= 0.3,
    landuse_map_in2,landuse_map_ini)

    # 30% of the map will become new
    # urban, water, protected areas and no data will remain the same
    landuse_map_ini = np.where(landuse_map_in2 >= 8,
    landuse_map_in2,landuse_map_ini)

    landuse_map_ini = np.where(landuse_map_in2 <= 2,
    landuse_map_in2,landuse_map_ini)

    for x in range(0, cols-1):
        for y in range(0, rows-1):
            if protectedArea[y, x] == 1:
                landuse_map_ini[y,x] = landuse_map_in[y,x]

    # other land use classes can change into 3, 4, 5, 6 or 7
    # choose which land cover type
    landuse_map_ini = np.where(landuse_map_ini == 0,
    np.random.randint(low=3, high=6,size=(rows,cols)),
    landuse_map_ini)

    #calculate remaining forest and cerrado areas 
    forrest_remaining_1 = np.count_nonzero(landuse_map_ini == 1)
    cerrado_remaining_1 = np.count_nonzero(landuse_map_ini == 2)

    # if there was more deforested than allowed, reset forest or cerrado from parent        
    if forrest_remaining_1 < minForestArea:
        landuse_map_ini = np.where(landuse_map_in2 == 1, 1, landuse_map_ini)
    if cerrado_remaining_1 < minCerradoArea:
        landuse_map_ini = np.where(landuse_map_in2 == 2, 2, landuse_map_ini) 

    # take one time the unchanged inital map
    if i == 1:
        landuse_map_ini = landuse_map_in
    all_landusemaps.append(landuse_map_ini)
 return np.array(all_landusemaps)

# maps = initialize_spatial(3, default_directory)
# f, axes = plt.subplots(1,3)
# cmap = ListedColormap(["#10773e","#b3cc33", "#0cf8c1", "#a4507d",
#  "#877712","#be94e8","#eeefce","#1b5ee4",
# "#614040","#00000000"])
# for amap, ax in zip(maps, axes):
#  im = ax.imshow(amap,interpolation='none', cmap=cmap,vmin = 0.5, vmax =
# 10.5)

# plt.colorbar(im, orientation='horizontal')
# plt.show()