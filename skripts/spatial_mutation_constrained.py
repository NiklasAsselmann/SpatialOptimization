import numpy as np
from pymoo.model.mutation import Mutation
from compute_genome import getNbh, determine_patch_elements, create_patch_ID_map

default_directory = "/home/nick/uni/spatialopti/SpatialOptimization/"
protectedArea = np.load(default_directory +"data/finalData/npy/protectedArea.npy")
# function to randomly change a certain patch
def random_reset_mutation(genome_in, point_mutation_prob):
 genome = list(genome_in)
 for i in range(1, len(genome)):
    	if np.random.uniform(0, 1)< point_mutation_prob:
            genome[i] = np.random.randint(low=3,high=7)
 return (genome)
# class that performs the mutation
class SpatialNPointMutation(Mutation):
    def __init__(self, prob=None,point_mutation_probability=0.01):
        super().__init__()
        self.prob = prob
        self.point_mutation_probability = point_mutation_probability
    def _do(self, problem, X, **kwargs):
        23
        shape_landusemaps = [X[0].shape[0], X[0].shape[1]]
        rows = shape_landusemaps[0]
        cols = shape_landusemaps[1]
        offspring = []

        # loop over individuals in population
        for i in X:
            # performe mutation with certain probability
            if np.random.uniform(0, 1) < self.prob:
                # get genome
                patches, genome = create_patch_ID_map(i, 0, [8, 9, 10, 20], "True")
                # perform mutation
                mutated_genome = random_reset_mutation(genome,
                self.point_mutation_probability)
                # go back to land use map
                mutated_individual = patches
                for x in range(0, cols):
                    for y in range(0, rows):
                        if mutated_individual[y,x] != 0 and protectedArea[y,x] != 1:
                            mutated_individual[y,x] = \
                            mutated_genome[mutated_individual[y,x] - 1]
                        else:
                            mutated_individual[y,x] = i[y,x]
                mutated_individual = np.where(mutated_individual == 0, i,
                    mutated_individual)
                forrest_remaining_1 = np.count_nonzero(mutated_individual == 1)
                cerrado_remaining_1 = np.count_nonzero(mutated_individual == 2)
                soy_remaining_1 = np.count_nonzero(mutated_individual == 4)
                pasture_remaining_1 = np.count_nonzero(mutated_individual == 7)
                ratio= pasture_remaining_1/soy_remaining_1
                if forrest_remaining_1 < 6337 or cerrado_remaining_1 < 5554 or ratio < 4 or ratio > 7:
                #if forrest_remaining_1 < 4843 or cerrado_remaining_1 < 5041 or ratio < 1 or ratio > 7:
                   print("failure")
                   mutated_individual = i
                offspring.append(mutated_individual)
        # if no mutation
            else:
                offspring.append(i)
        offspring = np.array(offspring)
        return offspring