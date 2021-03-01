im1= plt.imshow(landuse_nearest_area,interpolation='none',
 cmap=cmap2,vmin = 0.5, vmax = 10.5)
#ax2.set_title('Landuse map reclassed')
ax2.set_xlabel('Column #')
ax2.set_ylabel('Row #')
ax2.legend(handles=legend_landuse2,bbox_to_anchor=(1.05, 1), loc=2)
plt.imsave(default_directory +"results2016N6/maximizeProfit.tif", landuse_map_in,format='tiff',cmap=cmap2)
plt.show()