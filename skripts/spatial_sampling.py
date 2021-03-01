import numpy as np
from pymoo.model.sampling import Sampling
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import initial_population

import yaml

# Read config.yaml file
with open("config.yaml", 'r') as stream:
    yamlData = yaml.safe_load(stream)



default_directory = yamlData["directory"]

class SpatialSampling(Sampling):
 def __init__(self, var_type=np.float,default_dir=None) -> None:
    super().__init__()
    self.var_type = var_type
    self.default_dir = default_dir
 def _do(self, problem, n_samples, **kwargs):
    landusemaps_np = initial_population.initialize_spatial(n_samples,
    self.default_dir)
    return landusemaps_np


