# Import Libraries
import statistics

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_pickle('pickles/basket_count.pkl')
df['set_number'] = df.set.apply(lambda x: f"Set {x}")
df['color'] = df.set.apply(lambda x: "tab:red" if x == 17 else "tab:blue")
df = df.loc[(df["count"] != 0),]
df = df.sort_values(by=["count"])
fig, ax = plt.subplots()

ax.bar(df.set_number, df["count"], color=df["color"])

ax.set_ylabel('Count')
ax.set_xticklabels(df.set_number, rotation=45)
ax.set_title('Total Count of Baskets by Set')
ax.grid(axis='y')
ax.annotate(f'Mean = {round(statistics.mean(df["count"]),2)}', (1, 80))
ax.annotate(f'Median = {round(statistics.median(df["count"]),2)}', (1, 75))


# ax.legend(title='Fruit color')

plt.show()
