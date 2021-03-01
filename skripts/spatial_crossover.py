import numpy as np
import random
from compute_genome import create_patch_ID_map
from pymoo.model.crossover import Crossover
from calculateConstraints import calculate_constraints

minAreas = calculate_constraints()
minForestArea = minAreas[0]
minCerradoArea = minAreas[1]

import yaml

# Read config.yaml file
with open("config.yaml", 'r') as stream:
    yamlData = yaml.safe_load(stream)

default_directory = yamlData["directory"]
year = yamlData["optimization"]["year"]
protectedArea = np.load(default_directory +"data/finalData/npy/protectedArea.npy")


class SpatialOnePointCrossover(Crossover):

 def __init__(self,n_points, **kwargs):
    super().__init__(2, 2, 1.0) # (n_parents,n_offsprings,probability)
    self.n_points = n_points
 def _do(self, problem, X, **kwargs):
    _, n_matings= X.shape[0],X.shape[1]
    do_crossover = np.full(X[0].shape, True)
    # save dimensions of landuse maps
    shape_landusemaps = [X[0][_].shape[0],X[0][_].shape[1]]
    # child land use maps
    child_landuse_maps1 = []
    child_landuse_maps2 = []
    rows = shape_landusemaps[0]
    cols = shape_landusemaps[1]
    parent1 = X[0][_]
    parent2 = X[1][_]
    #print(rows)
    #print(protectedArea.shape)
    for _ in range(n_matings):
        #transform land use inside protected are to 20
        for x in range(0, cols-1):
                    for y in range(0, rows-1):
                        if protectedArea[y, x] == 1:
                            parent1[y,x] = 20
                            parent2[y,x] = 20
        # create patch map and genome with CoMOLA functions
        patches_parent1, genome_parent1 = create_patch_ID_map(
        parent1,0,[8,9,10,20],"True")
        patches_parent2, genome_parent2 = create_patch_ID_map(
        parent2,0,[8,9,10,20],"True")
        # define number of cuts
        num_crossover_points = self.n_points
        num_cuts = min(len(genome_parent1)-1, num_crossover_points)
        # select random places to cut genome
        cut_points = random.sample(range(1,min(len(genome_parent1),
        len(genome_parent2))), num_cuts)
        cut_points.sort()
        # define initial genome of children
        genome_child1 = list(genome_parent1)
        genome_child2 = list(genome_parent2)
        # get parts of genome from parents to children
        j = 0
        for i in range(0,min(len(genome_parent1),len(genome_parent2))):
                if j < len(cut_points):
                    if i >= cut_points[j]:
                        j = j + 1
                # alternating parent 1 and 0
                if (j % 2) != 0:
                    genome_child1[i] = 0.
                # alternating 0 and parent 2
                if (j % 2) == 0:
                    genome_child2[i] = 0.
        # fill in genome in patches
        child1 = patches_parent1
        child2 = patches_parent2
        for x in range(0, cols):
            for y in range(0, rows):
                if child1[y,x] != 0:
                    child1[y,x] = genome_child1[child1[y,x] - 1]
                    child2[y,x] = genome_child2[child2[y,x] - 1]

        # change land use back to original where forest or cerrado was added
        child1 = np.where(child1 == 1, X[0][_], child1)
        child2 = np.where(child2 == 1, X[1][_], child2)
        child1 = np.where(child1 == 2, X[0][_], child1)
        child2 = np.where(child2 == 2, X[1][_], child2)
        child1full = np.where(child1 == 0, X[1][_], child1)
        child2full = np.where(child2 == 0, X[0][_], child2)
        # change protected are back to original land use
        for x in range(0, cols):
            for y in range(0, rows):
                if child1full[y,x] == 20:
                    child1full[y,x] = X[0][_][y,x]
                if child2full[y,x] == 20:
                    child2full[y,x] = X[1][_][y,x]

        # count area of forest and cerrado
        forrest_remaining_1 = np.count_nonzero(child1full == 1)
        cerrado_remaining_1 = np.count_nonzero(child1full == 2)
        forrest_remaining_2 = np.count_nonzero(child2full == 1)
        cerrado_remaining_2 = np.count_nonzero(child2full == 2)

        print(minAreas)
        # if there was more deforested than allowed, reset forest or cerrado from parent
        if forrest_remaining_1 < minForestArea: 
            child1full = np.where(X[0][_] == 1, 1, child1full)
        if cerrado_remaining_1 < minCerradoArea:
            child1full = np.where(X[0][_] == 2, 2, child1full)
        if forrest_remaining_2 < minForestArea:
            child2full = np.where(X[1][_] == 1, 1, child2full)
        if cerrado_remaining_2 < minCerradoArea:
            child2full = np.where(X[1][_] == 2, 2, child2full)
        child_landuse_maps1.append(child1full)
        child_landuse_maps2.append(child2full)
        
    return np.array([np.array(child_landuse_maps1), np.array(child_landuse_maps2)])

