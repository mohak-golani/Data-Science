years_List=[]
i=2011
while(i<2021):
    years_List.append(i)
    i=i+1
durations_list=[103,101,99,100,100,95,95,96,93,90]
mov_dict={"years":years_List, "durations":durations_list}
print(mov_dict)
 
import pandas as pd
movie_df=pd.DataFrame(mov_dict)
print(movie_df)

import matplotlib.pyplot as plt
fig1=plt.figure
plt.plot(years_List,durations_list, linewidth=5.0, color="g")
plt.title("Netflix Movie Durations for the year between 2011-2020")
plt.show()

from google.colab import files
uploaded = files.upload()
import io

netflix_movies_only_df= netflix_df[netflix_df.type == "Movie"]
netflix_movies_column_subset = netflix_movies_only_df[["title","country","genre","release_year","duration"]]
print(netflix_movies_column_subset[:5])

fig = plt.figure(figsize=(12,8))
plt.scatter(netflix_movies_column_subset.release_year,netflix_movies_column_subset.duration,color="black")
plt.title("Movie Duration by Year of Release")
plt.show()

short_movies = netflix_movies_column_subset[netflix_movies_column_subset['duration'] < 60]
print(short_movies[:21])

for lab, row in netflix_movies_column_subset.iterrows() :
    if row['genre']=='Children' :
        colors_list.append('red')
    elif row['genre'] == "Documentaries" :
        colors_list.append('blue')
    elif row['genre']=='Stand-Up' :
         colors_list.append('green')
    else:
         colors_list.append('black')
print(colors_list[:11])

plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12,8))
plt.scatter(netflix_movies_column_subset.release_year,netflix_movies_column_subset.duration, c = colors_list)
plt.title("Movie duration by year of release")
plt.xlabel("Release year")
plt.ylabel("Duration (min)")
plt.show()