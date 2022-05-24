import matplotlib.pyplot as plt
import pandas as pd
zillow = pd.read_csv("zillow.csv")
Year_groups = zillow.groupby(["Year"])
figure, axes = plt.subplots(nrows=1, ncols=len(Year_groups.groups.keys()))
for(key, ax) in zip(Year_groups.groups.keys(), axes.flatten()):
    Year_groups.get_group(key).plot(ax=ax)
    ax.legend()
    ax.set_title(key)
plt.show()