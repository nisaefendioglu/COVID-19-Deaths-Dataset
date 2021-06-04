import numpy as np # linear algebra
import pandas as pd 
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import warnings
from collections import Counter
import operator


df_world = pd.read_csv("all_weekly_excess_deaths.csv")
print (df_world.shape)
df_world.head()



df_world.drop(columns=['days'], inplace=True)
df_temp = df_world['end_date'].str.split('-', expand=True)[[1,0]]
df_world['Date'] = df_temp[1] + '/' + df_temp[0]



corr = df_world.corr()
mask = np.zeros_like(corr)
mask[np.triu_indices_from(mask)] = True
plt.figure(figsize=(12,12))
sns.heatmap(corr, mask=mask, center=0, annot=True,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
plt.show()




fig = px.choropleth(df_world.rename(columns={'covid_deaths':'Covid Deaths'}), 
                    locations='country',
                    locationmode = 'country names',
                    color='Covid Deaths', 
                    animation_frame='Date'
                   )
fig.update_layout(geo=dict(
                  showframe = False,
                  showcoastlines = False)
                )
fig.show()




fig = px.choropleth(df_world.rename(columns={'excess_deaths_per_100k':'Excess Deaths per 100k'}), 
                    locations='country',
                    locationmode = 'country names',
                    color='Excess Deaths per 100k', 
                    animation_frame='Date'
                   )
fig.update_layout(geo=dict(
                  showframe = False,
                  showcoastlines = False)
                )
fig.show()





plt.figure(figsize=(16,8))
sns.barplot(data=df_world, x='total_deaths', y='Date', color='orange', label='Total Deaths')
sns.barplot(data=df_world, x='covid_deaths', y='Date', color='grey', label='Covid Deaths')
plt.xlabel(xlabel = 'Number of Deaths',fontsize=16, fontweight='bold')
plt.ylabel(ylabel = 'Date',fontsize=16, fontweight='bold')
plt.legend()
plt.show()





plt.figure(figsize=(16,8))
sns.countplot(data=df_world, y='country', order=dict(Counter(df_world['country']).most_common(15)))
plt.xlabel(xlabel = 'Count',fontsize=16, fontweight='bold')
plt.ylabel(ylabel = 'Country',fontsize=16, fontweight='bold')
plt.show()





