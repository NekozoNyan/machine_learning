import numpy as np
scores =np.array([[1.1, 2.2, 3.3], [2.1, 3.2, 4.3], [3.1, 4.2, 5.3]])
c_scores = scores[np.array([0, 1, 2]), np.array([0, 1, 2])]
print(c_scores)
