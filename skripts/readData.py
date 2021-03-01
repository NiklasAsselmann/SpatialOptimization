from pcraster import *
from pcraster.framework import *
import numpy as np
import matplotlib.pyplot as plt
import codecs
default_directory = "your/directory"

#read all data
landuse_2001 = plt.imread( default_directory +"data/finalData/initialLandUse2001RasterClippedPixel.tif")
landuse_2016 = plt.imread( default_directory +"data/finalData/initialLandUse2016RasterClippedPixel.tif")
slaughterhouses_2001 = plt.imread( default_directory +"data/finalData/slaugh_2001ReprojectRasterClippedComposite.tif")
slaughterhouses_2016 = plt.imread( default_directory +"data/finalData/slaugh_2016ReprojectRasterClippedComposite.tif")
soy_2001 = plt.imread( default_directory +"data/finalData/soy2001_ReprojectClippedComposite.tif")
soy_2016 = plt.imread( default_directory +"data/finalData/soy2016_ReprojectClippedComposite.tif")
road = plt.imread( default_directory +"data/finalData/roadsReprojectRasterClippedComposite.tif")
protectedArea = plt.imread( default_directory +"data/finalData/areas_protegidas_ReprojectRasterClippedComposite.tif")
soy_pot_yield =readmap( default_directory +"data/finalData/pcraster/potentialYieldSoyReprojectedClippedPCRasterMap.map")
sugarcane_pot_yield=readmap( default_directory +"data/finalData/pcraster/potentialYieldSugarcaneReprojectedClippedPCRasterMap.map")
cotton_pot_yield=readmap( default_directory +"data/finalData/pcraster/potentialYieldCottonReprojectedClippedPCRasterMap.map")

# create pcraster maps
soy_npy = numpy_operations.pcr_as_numpy(soy_pot_yield)
soy_npy = np.where(soy_npy == -9, 0, soy_npy)
soy_pot_yield = numpy_operations.numpy2pcr( Scalar, soy_npy, 0)
cotton_npy = numpy_operations.pcr_as_numpy(cotton_pot_yield)
cotton_npy = np.where(cotton_npy == -9, 0, cotton_npy)
cotton_pot_yield = numpy_operations.numpy2pcr( Scalar, cotton_npy, 0)
sugarcane_npy = numpy_operations.pcr_as_numpy(sugarcane_pot_yield)
sugarcane_npy = np.where(sugarcane_npy == -9, 0, sugarcane_npy)
sugarcane_pot_yield = numpy_operations.numpy2pcr( Scalar, sugarcane_npy, 0)

#reclassify land use map 2001
rows = landuse_2001.shape[0]
cols = landuse_2001.shape[1]
landuse_2001_reclass = np.zeros((rows,cols),dtype= 'uint8')


landuse_2001_reclass[landuse_2001 == 1] = 2
landuse_2001_reclass[landuse_2001 == 2] = 6
landuse_2001_reclass[landuse_2001 == 3] = 1
landuse_2001_reclass[landuse_2001 == 4] = 7
landuse_2001_reclass[landuse_2001 == 5] = 4
landuse_2001_reclass[landuse_2001 == 6] = 4
landuse_2001_reclass[landuse_2001 == 7] = 4
landuse_2001_reclass[landuse_2001 == 8] = 4
landuse_2001_reclass[landuse_2001 == 9] = 5
landuse_2001_reclass[landuse_2001 == 10] = 6
landuse_2001_reclass[landuse_2001 == 11] = 9
landuse_2001_reclass[landuse_2001 == 12] = 8
landuse_2001_reclass[landuse_2001 == 13] = 3
landuse_2001_reclass[landuse_2001 == 15] = 10
landuse_2001_reclass[landuse_2001 == 0] = 10

#reclassify land use map 2016
rows = landuse_2016.shape[0]
cols = landuse_2016.shape[1]
landuse_2016_reclass = np.zeros((rows,cols),dtype= 'uint8')

landuse_2016_reclass[landuse_2016 == 1] = 2
landuse_2016_reclass[landuse_2016 == 2] = 6
landuse_2016_reclass[landuse_2016 == 3] = 1
landuse_2016_reclass[landuse_2016 == 4] = 7
landuse_2016_reclass[landuse_2016 == 5] = 4
landuse_2016_reclass[landuse_2016 == 6] = 4
landuse_2016_reclass[landuse_2016 == 7] = 4
landuse_2016_reclass[landuse_2016 == 8] = 4
landuse_2016_reclass[landuse_2016 == 9] = 5
landuse_2016_reclass[landuse_2016 == 10] = 6
landuse_2016_reclass[landuse_2016 == 11] = 9
landuse_2016_reclass[landuse_2016 == 12] = 8
landuse_2016_reclass[landuse_2016 == 13] = 3
landuse_2016_reclass[landuse_2016 == 15] = 10
landuse_2016_reclass[landuse_2016 == 0] = 10

# data 5023; study area 12048; none 65535
# reclassify soy and slaughterhouses maps to 1,2 1 means there is a slaughterhouse 2 means not
rows = slaughterhouses_2001.shape[0]
cols = slaughterhouses_2001.shape[1]
slaughterhouses_2001_reclass = np.zeros((rows,cols),dtype= 'uint8')
slaughterhouses_2001_reclass[slaughterhouses_2001 == 5023] = 1
slaughterhouses_2001_reclass[slaughterhouses_2001 == 10248] = 2
slaughterhouses_2001_reclass[slaughterhouses_2001 == 65535] = 2

rows = slaughterhouses_2016.shape[0]
cols = slaughterhouses_2016.shape[1]
slaughterhouses_2016_reclass = np.zeros((rows,cols),dtype= 'uint8')
slaughterhouses_2016_reclass[slaughterhouses_2016 == 5023] = 1
slaughterhouses_2016_reclass[slaughterhouses_2016 == 10248] = 2
slaughterhouses_2016_reclass[slaughterhouses_2016 == 65535] = 2

rows = soy_2001.shape[0]
cols = soy_2001.shape[1]
soy_2001_reclass = np.zeros((rows,cols),dtype= 'uint8')
soy_2001_reclass[soy_2001 == 5023] = 1
soy_2001_reclass[soy_2001 == 10248] = 2
soy_2001_reclass[soy_2001 == 65535] = 2

rows = soy_2016.shape[0]
cols = soy_2016.shape[1]
soy_2016_reclass = np.zeros((rows,cols),dtype= 'uint8')
soy_2016_reclass[soy_2016 == 5023] = 1
soy_2016_reclass[soy_2016 == 10248] = 2
soy_2016_reclass[soy_2016 == 65535] = 2

rows = road.shape[0]
cols = road.shape[1]
road_reclass = np.zeros((rows,cols),dtype= 'uint8')
road_reclass[road == 5023] = 1
road_reclass[road == 10248] = 3
road_reclass[road == 65535] = 5

rows = protectedArea.shape[0]
cols = protectedArea.shape[1]
protectedArea_reclass = np.zeros((rows,cols),dtype= 'uint8')
protectedArea_reclass[protectedArea == 5023] = 1
protectedArea_reclass[protectedArea == 10248] = 2


# clip all maps to the same extend
landuse_2001_clipped = landuse_2001_reclass[0:277, 0:307]
landuse_2016_clipped = landuse_2016_reclass[0:277, 0:307]
slaughterhouses_2001_clipped = slaughterhouses_2001_reclass[0:277, 0:307]
slaughterhouses_2016_clipped = slaughterhouses_2016_reclass[0:277, 0:307]
soy_2001_clipped = soy_2001_reclass[0:277, 0:307]
soy_2016_clipped = soy_2016_reclass[0:277, 0:307]
road_clipped = road_reclass[0:277, 0:307]
protectedArea_clipped = protectedArea_reclass[0:277, 0:307]




# save all maps as npy arrays
np.save(default_directory +"/npy/landuse_2001.npy",landuse_2001_clipped)
np.save(default_directory +"/npy/landuse_2016.npy",landuse_2016_clipped)
np.save(default_directory +"/npy/slaughterhouses_2001.npy",slaughterhouses_2001_clipped)
np.save(default_directory +"/npy/slaughterhouses_2016.npy",slaughterhouses_2016_clipped)
np.save(default_directory +"/npy/soy_2001.npy",soy_2001_clipped)
np.save(default_directory +"/npy/soy_2016.npy",soy_2016_clipped)
np.save(default_directory +"/npy/roads.npy",road_clipped)
np.save(default_directory +"/npy/soy_pot_yield.npy",soy_npy)
np.save(default_directory +"/npy/sugarcane_pot_yield.npy",sugarcane_npy)
np.save(default_directory +"/npy/cotton_pot_yield.npy",cotton_npy)
np.save(default_directory +"/npy/protectedArea.npy",protectedArea_clipped)

slaughterhouses_2001= np.load(default_directory +"/npy/slaughterhouses_2001.npy")
slaughterhouses_2016= np.load(default_directory +"/npy/slaughterhouses_2016.npy")
soy_2001= np.load(default_directory +"/npy/soy_2001.npy")
soy_2016 =np.load(default_directory +"/npy/soy_2016.npy")
roads =np.load(default_directory +"/npy/roads.npy")


#transform the clipped maps to pcr raster
setclone(277, 307, 2000, -60.5615, -12.6411)
slaughterhouses_2001 = numpy_operations.numpy2pcr( Nominal , slaughterhouses_2001, 0)
slaughterhouses_2016 = numpy_operations.numpy2pcr( Nominal, slaughterhouses_2016, 0)
soy_2001 = numpy_operations.numpy2pcr( Nominal, soy_2001, 0)
soy_2016 = numpy_operations.numpy2pcr( Nominal, soy_2016, 0)
roads = numpy_operations.numpy2pcr( Nominal, roads, 2)

#calculate distances for every cell to a slaughterhouse or processing mill
slaughterhouses_2001 = nominal(slaughterhouses_2001 == 1)
spSlaughterhouses_2001= spread(slaughterhouses_2001, 0, scalar(roads))
slaughterhouses_2016 = nominal(slaughterhouses_2016 == 1)
spSlaughterhouses_2016= spread(slaughterhouses_2016, 0, scalar(roads))
soy_2001 = nominal(soy_2001 == 1)
spSoy_2001= spread(soy_2001, 0, scalar(roads))
soy_2016 = nominal(soy_2016 == 1)
spSoy_2016= spread(soy_2016, 0, scalar(roads))


#save the PCraster maps
report(slaughterhouses_2001, default_directory +"/pcraster/slaughterhouses_2001.map")
report(slaughterhouses_2016, default_directory +"/pcraster/slaughterhouses_2016.map")
report(soy_2001, default_directory +"/pcraster/soy_2001.map")
report(soy_2016, default_directory +"/pcraster/soy_2016.map")
report(spSlaughterhouses_2001, default_directory +"/pcraster/slaughterhouses_spread_2001.map")
report(spSlaughterhouses_2016, default_directory +"/pcraster/slaughterhouses_spread_2016.map")
report(spSoy_2001, default_directory +"/pcraster/soy_spread_2001.map")
report(spSoy_2016, default_directory +"/pcraster/soy_spread_2016.map")
report(roads, default_directory +"/pcraster/roads.map")
report(soy_pot_yield, default_directory +"/pcraster/soy_pot_yield.map")
report(sugarcane_pot_yield, default_directory +"/pcraster/sugarcane_pot_yield.map")
report(cotton_pot_yield, default_directory +"/pcraster/cotton_pot_yield.map")




