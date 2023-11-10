#PYTHON MP CODE & OUTPUT
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import random
df=pd.read_csv(r'C:\Users\MUSTERYA SM\Dropbox\My PC (LAPTOP-VAG6P3ER)\Desktop\python PRJ\most_subscribed_youtube_channels.csv')
df.isnull()
df = df.dropna()
fig, axs = plt.subplots(2,1, figsize=(10, 10))
category = df['category']
df2 = pd.DataFrame(category)
views = df['views']
df3 = pd.DataFrame(views)
combined_list = zip(category, views)
category_views = {key: value for key, value in combined_list}
less_than_two = []
for category, views in category_views.items():
    if len(category) < 2:
        less_than_two.append(category)
for category in less_than_two:
    if "Other" in category_views:
        category_views["Other"] += category_views.pop(category)
    else:
        category_views["Other"] = category_views.pop(category)
labels = list(category_views.keys())
sizes = list(category_views.values())
sizes = [int(size.replace(',','')) if isinstance(size, str) else size for size in sizes]
wedgeprops = {'linewidth': 2, 'edgecolor':'black'}
axs[0].pie(sizes, labels=labels, autopct='%1.1f%%',startangle=90,textprops={'color':'white'} , wedgeprops=wedgeprops)
axs[0].set_title('Total Views on the basis of Category')
axs[0].axis('equal')  
axs[0].legend(bbox_to_anchor=(1, 1), loc='upper right', borderaxespad=0.)
df = df.head(10)
df['subscribers'] = df['subscribers'].str.replace(',','').astype(float)
df['views'] = df['views'].str.replace(',','').astype(float)
Youtuber = df['Youtuber']
subscribers = df['subscribers']
views = df['views']
axs[1].bar(Youtuber, subscribers, color='r', width=0.4)
axs[1].set_ylabel('Subscribers (in million)')
ax2 = axs[1].twinx()
ax2.plot(Youtuber, views, '-o')
ax2.set_title('Average Views and Subscribers count of TOP 10 youtubers')
ax2.set_ylabel('Views (in hundred Billion)')
plt.tight_layout()
plt.show()
