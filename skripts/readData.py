from pcraster import *
from pcraster.framework import *
import numpy as np
import matplotlib.pyplot as plt
default_directory = "C:/Users/nick1/OneDrive - uni-muenster.de/Master/Semester1/SpatiOptmi/Tutorial_data/SpatialOptimization-main/data/finalData2"
landuse_2001 = plt.imread( default_directory +"/initialLandUse2001RasterClipped.tif")
landuse_2016 = plt.imread( default_directory +"/initialLandUse2016RasterClipped.tif")
slaughterhouses_2001 = plt.imread( default_directory +"/slaughterhouses2001RasterClippedComposite.tif")
slaughterhouses_2016 = plt.imread( default_directory +"/slaugtherhouses2016RasterClippedComposite.tif")
soy_2001 = plt.imread( default_directory +"/soy2001RasterClippedComposite.tif")
soy_2016 = plt.imread( default_directory +"/soy2016RasterClippedComposite.tif")
road = plt.imread( default_directory +"/roadsRasterClippedComposite.tif")
soy_pot_yield =readmap( default_directory +"/pcraster/potentialYieldSoyReprojectedPCRasterMapClippedResampled.map")
sugarcane_pot_yield=readmap( default_directory +"/pcraster/potentialYieldSugarcaneReprojectedPCRasterMapClippedResampled.map")
cotton_pot_yield=readmap( default_directory +"/pcraster/potentialYieldCottonReprojectedPCRasterMapClippedResampled.map")


soy_npy = numpy_operations.pcr_as_numpy(soy_pot_yield)
soy_pot_yield = numpy_operations.numpy2pcr( Scalar, soy_npy, 0)
cotton_npy = numpy_operations.pcr_as_numpy(cotton_pot_yield)
cotton_pot_yield = numpy_operations.numpy2pcr( Scalar, cotton_npy, 0)
sugarcane_npy = numpy_operations.pcr_as_numpy(sugarcane_pot_yield)
sugarcane_pot_yield = numpy_operations.numpy2pcr( Scalar, sugarcane_npy, 0)

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

# data 5023; study area 12048; none 65535

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


landuse_2001_clipped = landuse_2001_reclass[0:2351,0:2655]
landuse_2016_clipped = landuse_2001_reclass[0:2351,0:2655]
slaughterhouses_2001_clipped = slaughterhouses_2001_reclass[0:2351,60:2715]
slaughterhouses_2016_clipped = slaughterhouses_2016_reclass[0:2351,59:2714]
soy_2001_clipped = soy_2001_reclass[0:2351,60:2715]
soy_2016_clipped = soy_2016_reclass[0:2351,60:2715]
road_clipped = road_reclass[0:2351,60:2715]





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

slaughterhouses_2001= np.load(default_directory +"/npy/slaughterhouses_2001.npy")
slaughterhouses_2016= np.load(default_directory +"/npy/slaughterhouses_2016.npy")
soy_2001= np.load(default_directory +"/npy/soy_2001.npy")
soy_2016 =np.load(default_directory +"/npy/soy_2016.npy")
roads =np.load(default_directory +"/npy/roads.npy")


setclone(2351, 2655, 250, -60.5615, -12.6411)
slaughterhouses_2001 = numpy_operations.numpy2pcr( Nominal , slaughterhouses_2001, 0)
slaughterhouses_2016 = numpy_operations.numpy2pcr( Nominal, slaughterhouses_2016, 0)
soy_2001 = numpy_operations.numpy2pcr( Nominal, soy_2001, 0)
soy_2016 = numpy_operations.numpy2pcr( Nominal, soy_2016, 0)
roads = numpy_operations.numpy2pcr( Nominal, roads, 2)

slaughterhouses_2001 = nominal(slaughterhouses_2001 == 1)
spSlaughterhouses_2001= spread(slaughterhouses_2001, 0, scalar(roads))
slaughterhouses_2016 = nominal(slaughterhouses_2016 == 1)
spSlaughterhouses_2016= spread(slaughterhouses_2016, 0, scalar(roads))
soy_2001 = nominal(soy_2001 == 1)
spSoy_2001= spread(soy_2001, 0, scalar(roads))
soy_2016 = nominal(soy_2016 == 1)
spSoy_2016= spread(soy_2016, 0, scalar(roads))



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


