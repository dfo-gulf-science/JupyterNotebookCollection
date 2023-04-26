# Import Libraries

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import seaborn as sns

#
# import pickle
# with open('basket.pkl', 'rb') as f:
#     baskets = pickle.load(f)
#
# plt.hist(baskets, bins=100)
# plt.show()

df = pd.read_pickle('../pickles/CAR/baskets.pkl')

# plt.style.use('_mpl-gallery')

# make data
y = df.set
x = df.dt
color_labels = df.species.unique()
print()
rgb_values = sns.color_palette("muted", len(color_labels))
color_map = dict(zip(color_labels, rgb_values))
colors = df.species.map(color_map)

# plot
fig, ax = plt.subplots()

ax.scatter(x, y, c=df.species.map(color_map) )

ax.set(ylim=(15, 24))
ax.grid(axis='y')

plt.show()