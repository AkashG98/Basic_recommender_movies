import pandas as pd
import numpy as np

r_cols=['user_id','movie_id','ratings']
ratings=pd.read_csv('u.data',sep='\t',names=r_cols,usecols=range(3))


m_cols=['movie_id','title']
movies=pd.read_csv('u.item',sep='|',names=m_cols,usecols=range(2),encoding='latin-1')


ratings=pd.merge(movies,ratings)


mov_ratings=ratings.pivot_table(index=['user_id'],columns=['title'], values='ratings')

#THIS DATA CAN BE USED FOR BOTH ITME BASED AND USER BASED FILTERING
#for user relations we see row wise data & for item based we see column wise data

#we will do item based filtering

s_war_ratings=mov_ratings['Star Wars (1977)']
s_war_ratings.head()

#pandas corrwith function compares given value in data with every other present value

similar_mov=mov_ratings.corrwith(s_war_ratings)
similar_mov=similar_mov.dropna()
df=pd.DataFrame(similar_mov)
df.head()

similar_mov.sort_values(ascending=False)

movieStats=ratings.groupby('title').agg({'ratings':[np.size,np.mean]})
movieStats.head()
 
#by hit and try I am classifying that ratings size for more than 100 people should be used here.

popularMovies=movieStats['ratings']['size']>=100
movieStats[popularMovies].sort_values([('ratings','mean')],ascending=False)[:15]

#lets make new datframe with all our movies similar to StarWars 

df=movieStats[popularMovies].join(pd.DataFrame(similar_mov,columns=['similarity']))
df.head()
df.sort_values(['similarity'],ascending=False)

#
#this is more genuine value set but therue is still more on what we can improvise 

#this is a old dataset so we will get mostly old data to process upon
