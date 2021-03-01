from pcraster import *
from pcraster.framework import *
import numpy as np
from compute_genome import create_patch_ID_map
import pickle
import yaml

# Read config.yaml file
with open("config.yaml", 'r') as stream:
    yamlData = yaml.safe_load(stream)

directory = yamlData["directory"]

default_directory = directory



setclone(277, 307, 2000, -60.5615, -12.6411)
sp_slaughterhouses =readmap(default_directory +"/data/finalData/pcraster/slaughterhouses_spread_2001.map") 
sp_soy =readmap(default_directory +"/data/finalData/pcraster/soy_spread_2001.map") 
#sp_slaughterhouses =readmap(default_directory +"/data/finalData/pcraster/slaughterhouses_spread_2016.map") 
#sp_soy =readmap(default_directory +"/data/finalData/pcraster/soy_spread_2016.map") 
soy_pot_yield =readmap( default_directory +"/data/finalData/pcraster/soy_pot_yield.map")
sugarcane_pot_yield=readmap( default_directory +"/data/finalData/pcraster/cotton_pot_yield.map")
cotton_pot_yield=readmap( default_directory +"/data/finalData//pcraster/cotton_pot_yield.map")

sugarcane_npy = numpy_operations.pcr_as_numpy(sugarcane_pot_yield)
sugarcane_pot_yield = numpy_operations.numpy2pcr( Scalar, sugarcane_npy, 0)

# calculate the total yield for sugarcane, soy, cotton and pasture
def calculate_tot_profit2001(landuse_map_in,cellarea):
 all_profits = []

 # loop over the individuals in the population
 for land_use_map in landuse_map_in:


  pcrmap = numpy_operations.numpy2pcr( Nominal, land_use_map, 0)

  #check where the land use is pature
  pasture = pcrmap == 7

  pastureOutcome = ifthenelse(pasture, scalar(cellarea), 0)

  #calculate the revenue of each cell   
  cattleRevenue = pastureOutcome * 300 
  #calculate the production cost of each cell  
  cattleCost = pastureOutcome * 164.78
  #calculate the transportation cost of each cell  
  cattleTransportCost= sp_slaughterhouses/1000 * 0.02 * pastureOutcome 
  #calculate the profit of each cell by substracting the production cost and transportation cost from the revenue
  cattleProfit = cattleRevenue - cattleCost - cattleTransportCost

  #can be used for visualization of the profit or transportation cost of the area
  #aguila(cattleRevenue, cattleProfit, cattleCost, cattleTransportCost)
  
  
  # summarize the profit of each cell inside the study area
  cattleProfitTotal = float(maptotal(cattleProfit))


  # soy

  #check where the land use is soy
  soy = pcrmap == 4

  #calculate the soy yield in tons of every cell
  yield_soy = ifthenelse(soy, soy_pot_yield*cellarea, 0)

  #calculate the revenue of every cell
  soyRevenue = yield_soy * 235.9895

  #calculate the produciton cost of every cell
  soyCost = yield_soy * 189.629798

  #calculate the transportation cost of every cell
  soyTransportCost= (sp_soy/60/1000) * yield_soy * 2.68 

  #calculate the profit of each cell by substracting the production cost and transportation cost from the revenue
  soyProfit = soyRevenue - soyCost - soyTransportCost
  
  # summarize the profit of each cell inside the study area
  soyProfitTotal = float(maptotal(soyProfit))
  

 



  # sugarcane

  #check where the land use is sugarcane
  sugarcane = pcrmap == 5

  #calculate the sugarcane yield in tons of every cell
  yield_sugarcane = ifthenelse(sugarcane, sugarcane_pot_yield*cellarea, 0) # 20 -> sugarcanemap

  #calculate the revenue of every cell
  sugarcaneRevenue = yield_sugarcane * 17.06

  #calculate the produciton cost of every cell
  sugarcaneCost = yield_sugarcane * 13.79

  #calculate the transportation cost of every cell
  sugarcaneTransportCost= (sp_soy/60/1000) * yield_sugarcane * 2.68

  #calculate the profit of each cell by substracting the production cost and transportation cost from the revenue
  sugarcaneProfit = sugarcaneRevenue - sugarcaneCost - sugarcaneTransportCost

  # summarize the profit of each cell inside the study area
  sugarcaneProfitTotal = float(maptotal(sugarcaneProfit))

  
  # cotton

  #check where the land use is cotton
  cotton = pcrmap == 6

  #calculate the cotton yield in tons of every cell
  yield_cotton = ifthenelse(cotton, cotton_pot_yield*cellarea, 0)

  #calculate the revenue of every cell
  cottonRevenue = yield_cotton * 1100.639

  #calculate the produciton cost of every cell
  cottonCost = yield_cotton * 1154.80098

  #calculate the transportation cost of every cell
  cottonTransportCost= (sp_soy/60/1000) * yield_cotton * 2.68 

  #calculate the profit of each cell by substracting the production cost and transportation cost from the revenue
  cottonProfit = cottonRevenue - cottonCost - cottonTransportCost

  # summarize the profit of each cell inside the study area
  cottonProfitTotal = float(maptotal(cottonProfit))

  # total profit agriculture is equal to sum of different products
  tot_Profit = cattleProfitTotal + soyProfitTotal + sugarcaneProfitTotal + cottonProfitTotal
  all_profits.append(tot_Profit)
 return(np.array(all_profits))

#landuse = np.load(default_directory + "/data/finalData/npy/landuse_2001.npy")
#landuse = [landuse]

#print(np.shape(landuse))
# read input data for objectives


#tot_revenue =calculate_tot_revenue(landuse, 40000)
#print(tot_revenue)


def calculate_area2001(landuse_map_in,cellarea):
 # loop over the individuals in the population
 all_area = []
 for land_use_map in landuse_map_in:
  # calculate the total area of each land use class
  forest_area = np.count_nonzero(land_use_map == 1)*cellarea
  cerrado_area = np.count_nonzero(land_use_map == 2)*cellarea
  secondary_vegetation_area = np.count_nonzero(land_use_map == 3)*cellarea

  # sum over all land use classes
  area = forest_area + cerrado_area + secondary_vegetation_area
  # add to the array with all individuals
  all_area.append(area)
 return(np.array(all_area))

#tot_area = calculate_area(landuse, 400)

#print(tot_area)