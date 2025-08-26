import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend

import matplotlib.pyplot as plt

print("hello world")
plt.plot([1, 2, 3], [4, 5, 1])
plt.savefig('test.png')



