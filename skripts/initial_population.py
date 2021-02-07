import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
# make initial population for genetic algorithm
default_directory = "C:/Users/nick1/OneDrive - uni-muenster.de/Master/Semester1/SpatiOptmi/SpatialOptimization/"

protectedArea = np.load(default_directory +"data/finalData/npy/protectedArea.npy")

def initialize_spatial(pop_size,default_directory):
 all_landusemaps = []
 landuse_map_in = np.load(default_directory + "/data/finalData/npy/landuse_2001.npy")
 #landuse_map_in = np.load(default_directory + "/data/finalData/npy/landuse_2016.npy")
 rows = landuse_map_in.shape[0]
 cols = landuse_map_in.shape[1]
 landuse_map_in2 = landuse_map_in.copy()
 #print(rows)
 #print(protectedArea.shape)
 for x in range(0, cols-1):
    for y in range(0, rows-1):
        if protectedArea[y, x] == 1:
            landuse_map_in2[y,x] = 20
 #print(cols)
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
    landuse_map_ini = np.where(random_map_mw>=0,
    landuse_map_in2,landuse_map_ini)

    # 30% of the map will become new
    # urban, water and no data will remain the same
    landuse_map_ini = np.where(landuse_map_in2 >= 8,
    landuse_map_in2,landuse_map_ini)

    for x in range(0, cols-1):
        for y in range(0, rows-1):
            if protectedArea[y, x] == 1:
                landuse_map_ini[y,x] = landuse_map_in[y,x]

    # other land use classes can change into 3, 4, 5, 6 or 7
    # choose which land cover type
    landuse_map_ini = np.where(landuse_map_ini == 0,
    np.random.randint(low=3, high=7,size=(rows,cols)),
    landuse_map_ini)
    forrest_remaining_1 = np.count_nonzero(landuse_map_ini == 1)
    cerrado_remaining_1 = np.count_nonzero(landuse_map_ini == 2)
    soy_remaining_1 = np.count_nonzero(landuse_map_ini == 4)
    pasture_remaining_1 = np.count_nonzero(landuse_map_ini == 7)
    ratio= pasture_remaining_1/soy_remaining_1
    if forrest_remaining_1 < 6337:
    #if forrest_remaining_1 < 4843 or 
        landuse_map_ini = np.where(landuse_map_in2 == 1, landuse_map_in2, landuse_map_ini)
    if cerrado_remaining_1 < 5554:
    #if cerrado_remaining_1 < 5041:
        landuse_map_ini = np.where(landuse_map_in2 == 2, landuse_map_in2, landuse_map_ini) 
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