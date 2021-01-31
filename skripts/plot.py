import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.patches as mpatches

default_directory = "your/directory"

landuse_map_in = np.load(default_directory + "/data/finalData/npy/landuse_2001.npy")
#landuse_map_in = np.load(default_directory + "/data/finalData/npy/landuse_2016.npy")


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
#ax2.set_title('Landuse map reclassed')
ax2.set_xlabel('Column #')
ax2.set_ylabel('Row #')
ax2.legend(handles=legend_landuse2,bbox_to_anchor=(1.05, 1), loc=2)
plt.imsave(default_directory +"results/inital.tif", landuse_map_in,format='tiff',cmap=cmap2)
plt.show()


results = np.load(default_directory + "results2016/values.npy")
maps = np.load(default_directory + "results2016/maps.npy")

landuse_max_yield = maps[np.argmin(results[:,0], axis=0)]
landuse_max_biomass = maps[np.argmin(results[:,1], axis=0)]

# Plot them next to each other
f2, (ax2a, ax2b) = plt.subplots(1,2, figsize=(9,5))
im2a = ax2a.imshow(landuse_max_yield,interpolation='None',
 cmap=cmap2,vmin=0.5,vmax=10.5)
ax2a.set_title('Landuse map \nmaximized revenue', fontsize=10)
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
plt.savefig(default_directory+"results/landuse_max.png",dpi=150)
plt.show()


# Pareto Front
f1, ax1 = plt.subplots(1)
im1 = plt.scatter(-results[:,0],-results[:,1])
ax1.set_title("Objective Space")
ax1.set_xlabel('Total revenue [US$]')
ax1.set_ylabel('Natural Vegetation [hectar]')
plt.show()



# Pareto Front different generations 
history = np.load(default_directory + "results/history.npy", allow_pickle=True)
# add here the generations you want to see in the plot
generations2plot = [1,2,3,5,8,10]
# make the plot
fig4, ax4 = plt.subplots(1)
# i - 1, because generation 1 has index 0
for i in generations2plot:
 plt.scatter(-history[i-1][:,0],-history[i-1][:,1])
ax4.set_xlabel('Total revenue [US$]')
ax4.set_ylabel('Natural Vegetation [hectar]')
plt.legend(list(map(str, generations2plot)))
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
