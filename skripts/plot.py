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

if year==2001:
        landuse_map_in = np.load(default_directory + "/data/finalData/npy/landuse_2001.npy")
        from calculate_objectives_2001 import calculate_tot_profit2001 as calculate_tot_profit
        from calculate_objectives_2001 import calculate_area2001 as calculate_area
elif year == 2016:
        landuse_map_in = np.load(default_directory + "/data/finalData/npy/landuse_2016.npy")
        from calculate_objectives_2016 import calculate_tot_profit2016 as calculate_tot_profit
        from calculate_objectives_2016 import calculate_area2016 as calculate_area
else:
        raise ValueError("Year must be 2001 or 2016")


f2, ax2 = plt.subplots(1)
cmap2 = ListedColormap(["#10773e","#b3cc33", "#0cf8c1", "#a4507d",
 "#877712","#be94e8","#eeefce","#1b5ee4",
"#614040","#00000000"])
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
im1= plt.imshow(landuse_map_in,interpolation='none',
 cmap=cmap2,vmin = 0.5, vmax = 10.5)
ax2.set_title('Landuse map reclassed')
ax2.set_xlabel('Column #')
ax2.set_ylabel('Row #')
ax2.legend(handles=legend_landuse2,bbox_to_anchor=(1.05, 1), loc=2)
plt.show()

#load results
path=default_directory + results
results = np.load(path + "/values.npy")
maps = np.load(path + "/maps.npy")

landuse_max_profit = maps[np.argmin(results[:,0], axis=0)]
landuse_max_biomass = maps[np.argmin(results[:,1], axis=0)]

# Plot extremes next to each other
f2, (ax2a, ax2b) = plt.subplots(1,2, figsize=(9,5))
im2a = ax2a.imshow(landuse_max_profit,interpolation='None',
 cmap=cmap2,vmin=0.5,vmax=10.5)
ax2a.set_title('Landuse map \nmaximized profit', fontsize=10)
ax2a.set_xlabel('Column #')
ax2a.set_ylabel('Row #')
im2b = ax2b.imshow(landuse_max_biomass,interpolation='None',
 cmap=cmap2,vmin=0.5,vmax=10.5)
ax2b.set_title('Landuse map \nmaximized natural vegetation', fontsize=10)
ax2b.set_xlabel('Column #')
plt.legend(handles=legend_landuse2,bbox_to_anchor=(1.05, 1), loc=2,
 prop={'size': 9})
# Adjust location of the plots to make space for legend and save
plt.subplots_adjust(right = 0.6, hspace=0.2)
plt.show()

def find_nearest(array, value):
    idx = np.argmin(np.abs(array - value))
    return idx

# Pareto Front
revenue= calculate_tot_profit([landuse_map_in], 400)
area= calculate_area([landuse_map_in], 400)
f1, ax1 = plt.subplots(1)
plt.scatter(-results[:,0],-results[:,1])
coef = np.polyfit(-results[:,0],-results[:,1],1)
print(coef[0]*1000000)
poly1d_fn = np.poly1d(coef)
plt.plot(-results[:,0],poly1d_fn(-results[:,0]), "--k")
plt.plot(revenue[0],area[0], "sr")
ax1.set_title("Objective Space")
ax1.set_xlabel('Total profit [US$]')
ax1.set_ylabel('Natural Vegetation [hectar]')
#plt.savefig(default_directory+"/results2016N6/pareto_front.png")
plt.show()

#find the maps, where the profit or natural vegetation was optimized
idx1= find_nearest(results[:,0],- revenue[0])

landuse_nearest_revenue = maps[idx1]
idx2= find_nearest(results[:,1],- area[0])
landuse_nearest_area = maps[idx2]

print(-results[:,0][idx1])

#pareto front for detailed view
f1, ax1 = plt.subplots(1)
plt.scatter(-results[:,0],-results[:,1])
plt.plot(revenue[0],area[0], "sr")
plt.plot(-results[:,0][idx1],-results[:,1][idx1], "sy")
plt.plot(-results[:,0][idx2],-results[:,1][idx2], "sg")
ax1.set_title("Objective Space")
ax1.set_xlabel('Total profit [US$]')
ax1.set_ylabel('Natural Vegetation [hectar]')
#plt.savefig(default_directory+"/results2016N6/pareto_front_2.png")
plt.show()

#Maximize the area of natural vegetation while keeping the profit (yellow square)
im1= plt.imshow(landuse_nearest_revenue,interpolation='none',
 cmap=cmap2,vmin = 0.5, vmax = 10.5)
ax2.set_title('Maximize the area of natural vegetation while keeping the profit')
ax2.set_xlabel('Column #')
ax2.set_ylabel('Row #')
ax2.legend(handles=legend_landuse2,bbox_to_anchor=(1.05, 1), loc=2)
plt.show()

#Maximized profit while keeping the are of natural vegetation (green square)
im1= plt.imshow(landuse_nearest_area,interpolation='none',
 cmap=cmap2,vmin = 0.5, vmax = 10.5)
ax2.set_title('Maximize the profit while keeping the area of natural vegetation')
ax2.set_xlabel('Column #')
ax2.set_ylabel('Row #')
ax2.legend(handles=legend_landuse2,bbox_to_anchor=(1.05, 1), loc=2)
plt.show()


# Pareto Front different generations 
history = np.load(path+"/history.npy", allow_pickle=True)
# add here the generations you want to see in the plot
generations2plot = [500, 1000, 1500, 2000, 2500, 3000]
# make the plot
fig4, ax4 = plt.subplots(1)
# i - 1, because generation 1 has index 0
for i in generations2plot:
 plt.scatter(-history[i-1][:,0],-history[i-1][:,1])
ax4.set_xlabel('Total profit [US$]')
ax4.set_ylabel('Natural Vegetation [hectar]')
plt.plot(revenue[0],area[0], "sr")
plt.legend(["initial", 500, 1000, 1500, 2000, 2500, 3000])
#plt.savefig(default_directory+"/figures/pareto_front_over_generations.png")
plt.show()




# Hypervolume 
from pymoo.performance_indicator.hv import Hypervolume
# make an array of the generation numbers
n_gen = np.array(range(1,len(history)+1))
# set reference point
ref_point = np.array([0.0, 0.0])
# create the performance indicator object with reference point
metric = Hypervolume(ref_point=ref_point, normalize=False)
# calculate for each generation the HV metric
hv = [metric.calc(i) for i in history]
# visualze the convergence curve
fig5, ax5 = plt.subplots(1)
ax5.plot(n_gen, hv, '-o', markersize=4, linewidth=2)
ax5.set_xlabel("Generation")
ax5.set_ylabel("Hypervolume")
#plt.savefig(default_directory+"/figures/hypervolume.png")
plt.show()
