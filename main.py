import numpy as np
import matplotlib.pyplot as plt

data = np.random.default_rng(12345)
nums = data.integers(low=0, high=10, size=10)

plt.bar(range(len(nums)), nums)
plt.show()