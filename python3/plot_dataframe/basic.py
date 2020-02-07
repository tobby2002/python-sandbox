import matplotlib.pyplot as plt
import pandas as pd

# http://queirozf.com/entries/pandas-dataframe-plot-examples-with-matplotlib-pyplot
df = pd.DataFrame({
    'name': ['john','mary','peter','jeff','bill','lisa','jose'],
    'age': [23,78,22,19,45,33,20],
    'gender': ['M','F','M','M','M','F','M'],
    'state': ['california','dc','california','dc','california','texas','texas'],
    'num_children': [2,0,0,3,2,1,4],
    'num_pets': [5,1,0,5,2,2,3]
})
print(df)

# 1. a scatter plot comparing num_children and num_pets
df.plot(kind='scatter', x='num_children', y='num_pets', color='red')
plt.show()
# plt.savefig('output.png')


# 2. a simple line plot
df.plot(kind='bar', x='name', y='age')
plt.show()

# 3. gca stands for 'get current axis'
plt.clf()
ax = plt.gca()
df.plot(kind='line', x='name', y='num_children', ax=ax)
df.plot(kind='line', x='name', y='num_pets', color='red', ax=ax)
plt.show()

# 4. Bar plot with group by
plt.clf()
df.groupby('state')['name'].nunique().plot(kind='bar')
plt.show()

# 5. Stacked bar plot with group byPermalink
# Example: plot count by category as a stacked column:
# create a dummy variable and do a two-level group-by based on it:
# fix the x axis label and the legend
df.assign(dummy = 1).groupby(
  ['dummy','state']
).size().to_frame().unstack().plot(kind='bar',stacked=True,legend=False)

plt.title('Number of records by State')

# other it'll show up as 'dummy'
plt.xlabel('state')

# disable ticks in the x axis
plt.xticks([])

# fix the legend
current_handles, _ = plt.gca().get_legend_handles_labels()
reversed_handles = reversed(current_handles)

labels = reversed(df['state'].unique())

plt.legend(reversed_handles,labels,loc='lower right')
plt.show()


# 6. Stacked bar plot with group by, normalized to 100%Permalink
# A plot where the columns sum up to 100%.
#
# Similar to the example above but:
#
# normalize the values by dividing by the total amounts
#
# use percentage tick labels for the y axis
#
# Example: Plot percentage count of records by state
import matplotlib.ticker as mtick
# create dummy variable then group by that
# set the legend to false because we'll fix it later
df.assign(dummy = 1).groupby(
  ['dummy','state']
).size().groupby(level=0).apply(
    lambda x: 100 * x / x.sum()
).to_frame().unstack().plot(kind='bar',stacked=True,legend=False)

# or it'll show up as 'dummy'
plt.xlabel('state')

# disable ticks in the x axis
plt.xticks([])

# fix the legend or it'll include the dummy variable
current_handles, _ = plt.gca().get_legend_handles_labels()
reversed_handles = reversed(current_handles)
correct_labels = reversed(df['state'].unique())

plt.legend(reversed_handles,correct_labels)

plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())
plt.show()


# 7. Stacked bar plot with two-level group byPermalink
# Just do a normal groupby() and call unstack():
df.groupby(['state','gender']).size().unstack().plot(kind='bar',stacked=True)
plt.show()
# Another example: count the people by gender, spliting by state:
df.groupby(['gender','state']).size().unstack().plot(kind='bar',stacked=True)
plt.show()


# 8. Stacked bar plot with two-level group by, normalized to 100%Permalink
# Sometimes you are only ever interested in the distributions, not raw amounts:
df.groupby(['gender','state']).size().groupby(level=0).apply(
    lambda x: 100 * x / x.sum()
).unstack().plot(kind='bar',stacked=True)

plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())
plt.show()


# 9. Plot histogram of column values
df[['age']].plot(kind='hist',bins=[0,20,40,60,80,100],rwidth=0.8)
plt.show()


#10. Plot date histogram
# To plot the number of records per unit of time, you must first convert the date column to datetime using pandas.to_datetime().
df = pd.DataFrame({
    'name':[
        'john','lisa','peter','carl','linda','betty'
    ],
    'date_of_birth':[
        '01/21/1988','03/10/1977','07/25/1999','01/22/1977','09/30/1968','09/15/1970'
    ]
})
#Now convert the date column into datetime type and use plot(kind='hist'):
df['date_of_birth'] = pd.to_datetime(df['date_of_birth'],infer_datetime_format=True)

plt.clf()
df['date_of_birth'].map(lambda d: d.month).plot(kind='hist')
plt.show()