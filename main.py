import pandas as pd
import matplotlib.pyplot as plt

t = pd.read_csv('zillow.csv')

t = t.sort_values(by='ListPrice ($)').reset_index(drop=True)
below100 = over500 = btwn100n200 = btwn200n300 = btwn300n400 = btwn400n500 = 0
for i in range(len(t)):
    if t['ListPrice ($)'][i] < 100000:
        below100 += 1
    if t['ListPrice ($)'][i] >= 100000 & t['ListPrice ($)'][i] < 200000:
        btwn100n200 += 1
    if t['ListPrice ($)'][i] >= 200000 & t['ListPrice ($)'][i] < 300000:
        btwn200n300 += 1
    if t['ListPrice ($)'][i] >= 300000 & t['ListPrice ($)'][i] < 400000:
        btwn300n400 += 1
    if t['ListPrice ($)'][i] >= 400000 & t['ListPrice ($)'][i] < 500000:
        btwn400n500 +=1
    if t['ListPrice ($)'][i] >= 500000:
        over500 += 1
price = [below100, btwn100n200,  btwn200n300,  btwn300n400,  btwn400n500, over500]
axes = ['below 1e5 $', 'btwn 1e5 and 2*1e5 $', 'btwn 2*1e5 and 3*1e5 $', 'btwn 3*1e5 and 4*1e5 $',
        'btwn 4*1e5 and 5*1e5 $', 'over 5*1e5 $']
plt.bar(axes, price)
plt.show()

'''''
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

'''''
'''
#
...
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('udemy_courses.csv')
free = df[df["price"] == 0]
short = df['content_duration']

sortedd = free.sort_values(by=['num_subscribers'])
shortsort = df.sort_values(by=['content_duration'])

top = sortedd.head(10)
topshort = shortsort.head(10)
print(top, topshort)

plt.plot(top['num_subscribers'], top['course_title'])
plt.show()

plt.plot(topshort['content_duration'], topshort['course_title'])
plt.show()
#
'''''
