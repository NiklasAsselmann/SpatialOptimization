from pcraster import * 
from calculate_objectives import calculate_tot_revenue, calculate_area
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
default_directory = "your/directory"
cell_area = 200 * 200 # in hectares
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
    f1 = -calculate_tot_revenue(X[:], cell_area)
    f2 = -calculate_area(X[:],cell_area)
    out["F"] = np.column_stack([f1, f2])

problem = MyProblem()
print(problem)

from pymoo.algorithms.nsga2 import NSGA2
from pymoo.factory import get_sampling, get_crossover, get_mutation
algorithm = NSGA2(
 pop_size=70,
 n_offsprings=10,
 sampling=get_sampling("spatial", default_dir = default_directory),
 crossover=get_crossover("spatial_one_point_crossover", n_points = 3),
 mutation=get_mutation("spatial_n_point_mutation", prob = 0.01,
 point_mutation_probability = 0.015),
 eliminate_duplicates=False
 )

from pymoo.factory import get_termination 
termination = get_termination("n_gen", 10)

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

np.save(default_directory +"results/maps",res.X)
np.save(default_directory +"results/values",res.F)

