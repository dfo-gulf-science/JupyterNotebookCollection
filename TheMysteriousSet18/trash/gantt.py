# # Import Libraries
#
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# import datetime as dt
#
# # Read Data from timeline.csv
# df = pd.read_pickle('pickles/timeline_mod.pkl')
#
# ###### PRE-PROCESSING THE DATA ######
# # Convert dates to datetime format
# # Add Duration
# df['duration'] = df.end - df.start
# df.duration = df.duration.apply(lambda x: x.days + (x.seconds / 60 / 60 / 24))
# # sort in ascending order of start date
# df = df.sort_values(by='start', ascending=True)
#
# # project level variables
# p_start = df.start.min()
# p_end = df.end.max()
# td = p_end - p_start
# p_duration = td.days + (td.seconds / 60 / 60 / 24)
# # Add relative date
# df['rel_start'] = df.start.apply(lambda x: (x - p_start).days + ((x - p_start).seconds) / 60 / 60 / 24)
#
# # add color
# c_dict={'fishing':'red', 'oceanography':'blue', 'basket entry':'green', "specimen entry":"black"}
# df['color'] = df.type.apply(lambda x: c_dict[x])
# df['set'] = df.set_number.apply(lambda x: int(x))
#
# # Create custom x-ticks and x-tick labels
# x_ticks = np.linspace(start=0, stop=p_duration, num=10)
# x_labels = [(p_start + dt.timedelta(days=i)).strftime('%H:%M on %d-%b')
#             for i in x_ticks]
# #
# # ######  PLOTTING GANTT CHART ######
#
#
# o_dict={'fishing':-0.1, 'oceanography':-0.1, 'basket entry':0, "specimen entry":0.1}
#
#
# fig, ax = plt.subplots()
# last_set = None
# `for index, row in df.iterrows():`
#     current_set = int(row.set_number)
#     ax.broken_barh([(row.rel_start, row.duration)], (current_set+o_dict[row.type], 0.25), facecolors=c_dict[row.type])
#
# #
# # plt.barh(y=df.label, left=df.rel_start, width=df.duration, color=df.color)
# # # plt.xlabel("time")
# plt.grid(axis='y')
# ax.set_ylabel('Set Number')
# ax.set_yticks(range(df.set.min(),df.set.max()))     # Modify y-axis tick labels
# ax.set_xticks(ticks=x_ticks, labels=x_labels)
#
#
# plt.title('Sequence of Events - TEL 2022', size=18)
# plt.gca().invert_yaxis()
# plt.show()
