#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sps


shape, scale = 2.,2.
s=np.random.gamma(shape,scale,1000)
print(s)
