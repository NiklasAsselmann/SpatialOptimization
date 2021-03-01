from pcraster import * 

from pymoo import factory
from pymoo.model.crossover import Crossover
import spatial_extention_pymoo
# add spatial functions to pymoo library
factory.get_sampling_options = spatial_extention_pymoo._new_get_sampling_options
factory.get_crossover_options = spatial_extention_pymoo._new_get_crossover_options
factory.get_mutation_options = spatial_extention_pymoo._new_get_mutation_options
Crossover.do = spatial_extention_pymoo._new_crossover_do



import numpy as np
import pickle
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from pymoo.util.misc import stack
from pymoo.model.problem import Problem

from pymoo.algorithms.nsga2 import NSGA2
from pymoo.factory import get_sampling, get_crossover, get_mutation
from pymoo.factory import get_termination
from pymoo.optimize import minimize
import yaml


# Read config.yaml file
with open("config.yaml", 'r') as stream:
    yamlData = yaml.safe_load(stream)

#load data saved in yaml
default_directory = yamlData["directory"]
year = yamlData["optimization"]["year"]
crossoverPoints = yamlData["optimization"]["crossoverPoints"]
offspring = yamlData["optimization"]["offspring"]
populationSize = yamlData["optimization"]["populationSize"]
initialPopulationChange = yamlData["optimization"]["initialPopulationChange"]
mutationPropability = yamlData["optimization"]["mutationPropability"]
patchesMutationPropability = yamlData["optimization"]["patchesMutationPropability"]
generations = yamlData["optimization"]["generations"]
resultDirectory = yamlData["resultDirectory"]
cell_area = 400 # in hectares

if year==2001:
   from calculate_objectives_2001 import calculate_tot_profit2001 as calculate_tot_profit
   from calculate_objectives_2001 import calculate_area2001 as calculate_area
else:
   from calculate_objectives_2016 import calculate_tot_profit2016 as calculate_tot_profit
   from calculate_objectives_2016 import calculate_area2016 as calculate_area
# read input data for objectives

from pymoo.model.problem import Problem
class MyProblem(Problem):

 # define the number of variables etc.
 def __init__(self):
    super().__init__(n_var=277, # nr of variables
                     n_obj=2, # nr of objectives
                     n_constr=0, # nr of constraints
                     xl=0.0, # lower boundaries
                     xu=1.0) # upper boundaries

                      # define the objective functions
 def _evaluate(self, X, out, *args, **kwargs):
    f1 = -calculate_tot_profit(X[:], cell_area)
    f2 = -calculate_area(X[:],cell_area)
    out["F"] = np.column_stack([f1, f2])

problem = MyProblem()
print(problem)

from pymoo.algorithms.nsga2 import NSGA2
from pymoo.factory import get_sampling, get_crossover, get_mutation
algorithm = NSGA2(
 pop_size=populationSize,
 n_offsprings= offspring,
 sampling=get_sampling("spatial", default_dir = default_directory),
 crossover=get_crossover("spatial_one_point_crossover", n_points = crossoverPoints),
 mutation=get_mutation("spatial_n_point_mutation", prob = mutationPropability, point_mutation_probability = patchesMutationPropability),
 eliminate_duplicates=False
 )

from pymoo.factory import get_termination 
termination = get_termination("n_gen", generations)

from pymoo.optimize import minimize
res = minimize(problem,
               algorithm,
               termination,
               seed=1, 
               save_history=True,   
               verbose=True)

print(res)
print(res.X)
print(res.F)

#save final land use maps and corresponding values of profit and area of natural vegetation for each map
np.save(default_directory + resultDirectory+"/maps",res.X)
np.save(default_directory + resultDirectory+"/values",res.F)

# Create an empty list to save objective values per generation
# Needed for history 
f = []
# iterate over the generations
for generation in res.history:
 # retrieve the optimal for all objectives from the generation
 opt = generation.opt
 this_f = opt.get("F")
 f.append(this_f)

fNumpy = np.asarray(f)

#save history
np.save(default_directory + resultDirectory +"/history",fNumpy)


