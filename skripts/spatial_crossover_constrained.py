import numpy as np
import random
from compute_genome import create_patch_ID_map
from pymoo.model.crossover import Crossover

default_directory = "default_directory = "C:/Users/nick1/OneDrive - uni-muenster.de/Master/Semester1/SpatiOptmi/SpatialOptimization/"
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
        for x in range(0, cols-1):
                    for y in range(0, rows-1):
                        if protectedArea[y, x] == 1:
                            parent1[y,x] = 20
                            parent2[y,x] = 20
        # create patch map and genome with CoMOLA functions
        patches_parent1, genome_parent1 = create_patch_ID_map(
        parent1,0,[8,9,10,20],"True")
        patches_parent2, genome_parent2 = create_patch_ID_map(
        parent2,0,[8,9,10, 20],"True")
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
                    21
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
        child1 = np.where(child1 == 1, X[0][_], child1)
        child2 = np.where(child2 == 1, X[1][_], child2)
        child1 = np.where(child1 == 2, X[0][_], child1)
        child2 = np.where(child2 == 2, X[1][_], child2)
        child1full = np.where(child1 == 0, X[1][_], child1)
        child2full = np.where(child2 == 0, X[0][_], child2)
        for x in range(0, cols):
            for y in range(0, rows):
                if child1full[y,x] == 20:
                    child1full[y,x] = X[0][_][y,x]
                if child2full[y,x] == 20:
                    child2full[y,x] = X[1][_][y,x]
        forrest_remaining_1 = np.count_nonzero(child1full == 1)
        cerrado_remaining_1 = np.count_nonzero(child1full == 2)
        forrest_remaining_2 = np.count_nonzero(child2full == 1)
        cerrado_remaining_2 = np.count_nonzero(child2full == 2)
        soy_remaining_1 = np.count_nonzero(child1full == 4)
        pasture_remaining_1 = np.count_nonzero(child1full == 7)
        soy_remaining_2 = np.count_nonzero(child2full == 4)
        pasture_remaining_2 = np.count_nonzero(child2full == 7)
        ratio1= pasture_remaining_1/soy_remaining_1
        ratio2= pasture_remaining_2/soy_remaining_2

        if forrest_remaining_1 < 6337 or cerrado_remaining_1 < 5554 or ratio1 < 1 or ratio1 > 7:
        #if forrest_remaining_1 < 4843 or cerrado_remaining_1 < 5041 or ratio1 < 1 or ratio1 > 7:
            print("failure")
            child1full = X[0][_]
        if forrest_remaining_2 < 6337 or cerrado_remaining_2 < 5554 or ratio2 < 4 or ratio2 > 7:
        #if forrest_remaining_2 < 4843 or cerrado_remaining_2 < 5041 or ratio2 < 1 or ratio2 > 7:
            print("failure")
            child2full = X[1][_]
        child_landuse_maps1.append(child1full)
        child_landuse_maps2.append(child2full)
        
    return np.array([np.array(child_landuse_maps1), np.array(child_landuse_maps2)])

