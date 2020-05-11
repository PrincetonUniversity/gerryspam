# https://github.com/gerrymandr/georgia/blob/master/competitiveness.ipynb
import numpy as np
import pickle

# save np.load
np_load_old = np.load

# modify the default parameters of np.load
np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)

sen = np.load("/Users/hopecj/projects/gerryspam/MO/res/MO_state_senate_1000_0.05.p")
