from pcraster import *
from pcraster.framework import *
import numpy as np
from compute_genome import create_patch_ID_map
import pickle

default_directory = "<enter-directory-path>"

setclone(2351, 2655, 250, -60.5615, -12.6411) 
#setclone(100, 100, 250, -60.5615, -12.6411) 
sp_slaughterhouses =readmap(default_directory +"/data/finalData/pcraster/slaughterhouses_spread_2001.map") 
sp_soy =readmap(default_directory +"/data/finalData/pcraster/soy_spread_2001.map") 
soy_pot_yield =readmap( default_directory +"/data/finalData/pcraster/soy_pot_yield.map")
sugarcane_pot_yield=readmap( default_directory +"/data/finalData/pcraster/sugarcane_pot_yield.map")
cotton_pot_yield=readmap( default_directory +"/data/finalData/pcraster/cotton_pot_yield.map")

sugarcane_npy = numpy_operations.pcr_as_numpy(sugarcane_pot_yield)
sugarcane_pot_yield = numpy_operations.numpy2pcr( Scalar, sugarcane_npy, 0)

# calculate the total yield for sugarcane, soy, cotton and pasture
def calculate_tot_revenue(landuse_map_in,cellarea):
 all_revenues = []

 # loop over the individuals in the population
 for land_use_map in landuse_map_in:
  pcrmap = numpy_operations.numpy2pcr( Nominal, land_use_map, 0)
  pasture = pcrmap == 7

  pastureOutcome = ifthenelse(pasture, scalar(cellarea), 0)
     
  cattleProfit = pastureOutcome * 300 
  cattleCost = pastureOutcome * 164.78
  
  cattleTransportCost= sp_slaughterhouses/1000 * 0.02 * pastureOutcome # /cellare has to be transformed to hectar

  cattleRevenue = cattleProfit - cattleCost - cattleTransportCost

  cattleRevenueTotal = float(maptotal(cattleRevenue))


  # soy

  soy = pcrmap == 4


  yield_soy = ifthenelse(soy, soy_pot_yield*cellarea, 0) # 20 -> soymap
  
  
  

  soyProfit = yield_soy * 235.9895
  soyCost = yield_soy * 189.629798
  soyTransportCost= (sp_soy/60/1000) * yield_soy * 2.68 

  soyRevenue = soyProfit - soyCost - soyTransportCost
  

  soyRevenueTotal = float(maptotal(soyRevenue))
  

 



  # sugarcane

  sugarcane = pcrmap == 5

  #soy

  yield_sugarcane = ifthenelse(sugarcane, sugarcane_pot_yield*cellarea, 0) # 20 -> sugarcanemap


  sugarcaneProfit = yield_sugarcane * 17.06
  sugarcaneCost = yield_sugarcane * 13.79
  sugarcaneTransportCost= (sp_soy/60/1000) * yield_sugarcane * 2.68 
  sugarcaneRevenue = sugarcaneProfit - sugarcaneCost - sugarcaneTransportCost

  sugarcaneRevenueTotal = float(maptotal(sugarcaneRevenue))

  
  # cotton
  cotton = pcrmap == 6


  yield_cotton = ifthenelse(cotton, cotton_pot_yield*cellarea, 0) # 20 -> cottom
  
  

  cottonProfit = yield_cotton * 1100.639
  cottonCost = yield_cotton * 1154.80098
  cottonTransportCost= (sp_soy/60/1000) * yield_cotton * 2.68 
  cottonRevenue = cottonProfit - cottonCost - cottonTransportCost

  cottonRevenueTotal = float(maptotal(cottonRevenue))

  


  # total yield agriculture is equal to sum of different crops
  tot_revenue = cattleRevenueTotal + soyRevenueTotal + sugarcaneRevenueTotal + cottonRevenueTotal
  all_revenues.append(tot_revenue)
  #aguila(cottonRevenue,  cattleRevenue, soyRevenue, sugarcaneRevenue, pcrmap)
 return(np.array(all_revenues))

#landuse = np.load(default_directory + "/SpatialOptimization-main/data/finalData2/npy/landuse_2001.npy")
#landuse = [landuse]

# print(np.shape(landuse))
# read input data for objectives


#tot_revenue =calculate_tot_revenue(landuse, soy_pot_yield, sugarcane_pot_yield, cotton_pot_yield, 6.25)
#print(tot_revenue)


def calculate_area(landuse_map_in,cellarea):
 # loop over the individuals in the population
 all_area = []
 for land_use_map in landuse_map_in:
  # calculate the total area of each land use class
  forest_area = np.count_nonzero(land_use_map == 1)*cellarea
  cerrado_area = np.count_nonzero(land_use_map == 2)*cellarea
  secondary_vegetation_area = np.count_nonzero(land_use_map == 3)*cellarea

 # multiply area of the land use class (ha) with the AGB (tonnes/ha)

  # sum over all land use classes
  area = forest_area + cerrado_area + secondary_vegetation_area
  # add to the array with all individuals
  all_area.append(area)
 return(np.array(all_area))

#tot_area = calculate_area(landuse, 6.25)

#print(tot_area)