# Import Libraries

import matplotlib.pyplot as plt
import pandas as pd

# #
# # import pickle
# # with open('basket.pkl', 'rb') as f:
# #     baskets = pickle.load(f)
# #
#
# df = pd.read_pickle('pickles/baskets17.pkl')
# plt.hist(df.dt, bins=40)
# plt.title('Histogram of Baskets Entered During Set 17', size=18)
# # plt.show()
#
#
# df = pd.read_pickle('pickles/specimens17.pkl')
# plt.hist(df.dt, bins=40)
# plt.title('Histogram of Specimens Measured During Set 17', size=18)
# # plt.show()
#
#

#
# nrow = 2
# ncol = 2
# rows = range(0, nrow)
# cols = range(0, ncol)
# sets = 17, 21, 25, 29
# i = 0
# fig, axs = plt.subplots(nrow, ncol)
# for row in rows:
#     for col in cols:
#         ax = axs[row, col]
#         ax.set_title(f'Set {sets[i]}')
#         ax.hist(df.loc[(df["set"] == sets[i]),].dt, bins=30)
#         i += 1


#
# df = df.loc[(df["set"]==17),]
# nrow = 2
# ncol = 2
# rows = range(0, nrow)
# cols = range(0, ncol)
# species = df["species"].unique()
# species = ["Greenland halibut", "American plaice", "Snow crab", "Rockfishes, Redfish unidentified (Sebastes sp.)"]
# i = 0
# fig, axs = plt.subplots(nrow, ncol)
# for row in rows:
#     for col in cols:
#         ax = axs[row, col]
#         ax.set_title(f'{species[i]}')
#         dts = df.loc[(df["species"] == species[i]),].dt
#
#         ax.hist(dts, bins=30)
#         i += 1

#
# for s in species:
#     dts = df.loc[(df["species"] == s),].dt
#     plt.hist(dts, bins=40)
#

plt.title('Histogram of Specimens Measured During Set 17', size=18)
# plt.show()



df = pd.read_pickle('../pickles/CAR/specimens.pkl')
sets = df["set"].unique()
set_labels = [f"set {s}" for s in sets]


colors = list()
for s in sets:
    if s != 21:
        colors.append("tab:blue")
    else:
        colors.append("yellow")
spp_count = list()
print(sets)
for s in sets:
    spp_count.append(len(df.loc[df["set"]==s].species.unique()))
fig, ax = plt.subplots()
ax.bar(set_labels, spp_count, color=colors)
ax.set_ylabel('Count')
ax.set_xticklabels(set_labels, rotation=45)
ax.set_title('Total Count of Species by Set')
ax.grid(axis='y')
#
#
# ax.legend(title='Fruit color')
#
plt.show()

#
#
#
# # make data
# x = set_starts
# x = [1,2,3,4,5,6]
# # y = [1,1,1,1,1,1]
# y = np.repeat(1, len(x))
# fig, ax = plt.subplots()
# #
# print(y)
# ax.stem(x,y)
#
# print(x)
# plt.stem(x)

# ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#        ylim=(0, 8), yticks=np.arange(1, 8))


#
# # plt.style.use('_mpl-gallery')
#
# # make data
# y = df.set
# x = df.dt
# color_labels = df.species.unique()
# print()
# rgb_values = sns.color_palette("muted", len(color_labels))
# color_map = dict(zip(color_labels, rgb_values))
#
# #
# # plot
# fig, ax = plt.subplots()
#
# ax.scatter(x, y, c=df.species.map(color_map) )
#
# # ax.set(ylim=(15, 24))
# ax.grid(axis='y')
#


