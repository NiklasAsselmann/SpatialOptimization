from pcraster import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.patches as mpatches
import matplotlib.colors

import yaml

# Read config.yaml file
with open("config.yaml", 'r') as stream:
    yamlData = yaml.safe_load(stream)

directory = yamlData["directory"]
year = yamlData["optimization"]["year"]
results = yamlData["resultDirectory"]

default_directory = directory


results2001 = np.load(default_directory + "results/results2001/values.npy")
maps2001 = np.load(default_directory + "results/results2001/maps.npy")
results2016 = np.load(default_directory + "results/results2016/values.npy")
maps2016 = np.load(default_directory + "results/results2016/maps.npy")

landuse_map_in2001 = np.load(default_directory + "data/finalData/npy/landuse_2001.npy")
landuse_map_in2016 = np.load(default_directory + "/data/finalData/npy/landuse_2016.npy")

def find_nearest(array, value):
    idx = np.argmin(np.abs(array - value))
    return idx

# Pareto Front
from calculate_objectives_2001 import calculate_tot_profit2001, calculate_area2001
from calculate_objectives_2016 import calculate_tot_profit2016, calculate_area2016
revenue2001= calculate_tot_profit2001([landuse_map_in2001], 400)
area2001= calculate_area2016([landuse_map_in2001], 400)
revenue2016= calculate_tot_profit2016([landuse_map_in2016], 400)
area2016= calculate_area2016([landuse_map_in2016], 400)

#show both initial land uses and parteo fronts
fig1, ax1 = plt.subplots(1)
# i - 1, because generation 1 has index 0
plt.scatter(-results2001[:,0],-results2001[:,1])
plt.scatter(-results2016[:,0],-results2016[:,1])
ax1.set_xlabel('Total profit [US$]')
ax1.set_ylabel('Natural Vegetation [hectar]')
plt.plot(revenue2001[0],area2001[0], "sr")
plt.plot(revenue2016[0],area2016[0], "xr")
plt.legend(["inital 2001", "inital 2016", "2001", "2016"])
#plt.savefig(default_directory+"/figures/pareto_front_over_generations.png")
plt.show()

#find maps, where the area is the same as in the initial map from 2001 but the profit is maximized
idx1= find_nearest(results2001[:,1],- area2016[0])
idx2= find_nearest(results2016[:,1],- area2016[0])
cmap2 = ListedColormap(["#10773e","#b3cc33", "#0cf8c1", "#a4507d",
 "#877712","#be94e8","#eeefce","#1b5ee4",
"#614040","#00000000"])

#pareto front for the detailed view
fig1, ax1 = plt.subplots(1)
# i - 1, because generation 1 has index 0
plt.scatter(-results2001[:,0],-results2001[:,1])
plt.scatter(-results2016[:,0],-results2016[:,1])
ax1.set_xlabel('Total profit [US$]')
ax1.set_ylabel('Natural Vegetation [hectar]')
plt.plot(revenue2016[0],area2016[0], "xr")
plt.plot(-results2001[:,0][idx1],-results2001[:,1][idx1], "sy")
plt.plot(-results2016[:,0][idx2],-results2016[:,1][idx2], "sg")
#plt.legend(list(map(str, [2001,2016,2001,2016])))
#plt.savefig(default_directory+"/figures/pareto_front_over_generations.png")
plt.show()

landuse2001= maps2001[idx1]
landuse2016= maps2016[idx2]
legend_landuse2 = [mpatches.Patch(color="#10773e",label = 'Forest'),
 mpatches.Patch(color="#b3cc33",label = 'Cerrado'),
 mpatches.Patch(color="#0cf8c1",label = 'Secondary vegetation'),
 mpatches.Patch(color="#a4507d",label = 'Soy'),
 mpatches.Patch(color="#877712",label = 'Sugarcane'),
 mpatches.Patch(color="#be94e8",label = 'Fallow/cotton'),
 mpatches.Patch(color="#eeefce",label = 'Pasture'),
 mpatches.Patch(color="#1b5ee4",label = 'Water'),
 mpatches.Patch(color="#614040",label = 'Urban'),
 mpatches.Patch(color="#00000000",label = 'No data')]

# Landuse map from 2001 which has the same area of natural vegetation like the initial 2016 (yellow square)
f2, ax2 = plt.subplots(1)
im1= plt.imshow(landuse2001,interpolation='none',
 cmap=cmap2,vmin = 0.5, vmax = 10.5)
ax2.set_title('Landuse map 2001 \n same area initial 2016')
ax2.set_xlabel('Column #')
ax2.set_ylabel('Row #')
ax2.legend(handles=legend_landuse2,bbox_to_anchor=(1.05, 1), loc=2)
#plt.imsave(default_directory +"results2001N6/maximimzeArea.tif", landuse_map_in,format='tiff',cmap=cmap2)
plt.show()

# Landuse map from 2016 which has the same area of natural vegetation like the initial 2016 (green square)
f2, ax2 = plt.subplots(1)
im1= plt.imshow(landuse2016,interpolation='none',
 cmap=cmap2,vmin = 0.5, vmax = 10.5)
ax2.set_title('Landuse map 2016 \n same area initial 2016')
ax2.set_xlabel('Column #')
ax2.set_ylabel('Row #')
ax2.legend(handles=legend_landuse2,bbox_to_anchor=(1.05, 1), loc=2)
#plt.imsave(default_directory +"results2001N6/maximimzeArea.tif", landuse_map_in,format='tiff',cmap=cmap2)
plt.show()