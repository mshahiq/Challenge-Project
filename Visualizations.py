import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


location_csv = 'D:/AI-Course/Challenge-IMDB/Challenge-Project/imdb_challenge_drsort.csv'

data = pd.read_csv(location_csv)
#print(data)

df = pd.DataFrame(data)

#sorted_dateyears = df.sort_values("Date Release")
#sorted_dateyears.to_csv('D:/AI-Course/Challenge-IMDB/Challenge-Project/imdb_challenge_drsort.csv')

# Rating movies vs. Release Year (Figure_1)

x = df['Date Release']
y = df['Ratings']
plt.scatter(x,y)
plt.xlabel('Release Year')
plt.ylabel('Ratings')

plt.title('Ratings of the Movies')
plt.show()
'''
# no.of movies vs. director

#plt.plot(df['Director'], df['Movie Number'])

location_csv1 = 'D:/AI-Course/Challenge-IMDB/Challenge-Project/imdb_challenge_sortdirector.csv'
data1 = pd.read_csv(location_csv1)
df1 = pd.DataFrame(data1)

plt.figure(figsize=(10,30))
plt.xlabel('Director')
plt.xticks(rotation=90)
plt.ylabel('Number of Movies')
plt.title('Relation of directors and # of movies')
plt.bar(df1['Director'], df1['Count'])
plt.show()
'''
'''
# no.of movies vs. actors

location_csv2 = 'D:/AI-Course/Challenge-IMDB/Challenge-Project/imdb_challenge_sortactor.csv'
data2 = pd.read_csv(location_csv2)
df2 = pd.DataFrame(data2)

plt.figure(figsize=(10,20))

plt.ylim(0.0,3.0)
plt.xlabel('Actor')
plt.xticks(rotation=90)
plt.ylabel('Number of Movies')
plt.title('Relation of actors and # of movies')
plt.bar(df2['Movie Stars'], df2['Count'])
plt.show()
'''
