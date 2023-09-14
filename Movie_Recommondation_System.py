#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O 


# In[2]:


movies = pd.read_csv('/Users/kinjal/Downloads/movies.csv')
credits = pd.read_csv('/Users/kinjal/Downloads/credits.csv') 


# In[3]:


movies.head(2)


# In[4]:


movies.shape


# In[5]:


credits.head()


# In[6]:


movies = movies.merge(credits,on='title')


# In[7]:


movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']]


# In[8]:


movies.head()


# In[9]:


import ast
def convert(text):
    L = []
    for i in ast.literal_eval(text):
        L.append(i['name']) 
    return L 


# In[10]:


movies.dropna(inplace=True)


# In[11]:


movies['genres'] = movies['genres'].apply(convert)
movies.head()


# In[12]:


movies['keywords'] = movies['keywords'].apply(convert)
movies.head()


# In[13]:


import ast
ast.literal_eval('[{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}, {"id": 14, "name": "Fantasy"}, {"id": 878, "name": "Science Fiction"}]')


# In[14]:


def convert3(text):
    L = []
    counter = 0
    for i in ast.literal_eval(text):
        if counter < 3:
            L.append(i['name'])
        counter+=1
    return L 


# In[15]:


movies['cast'] = movies['cast'].apply(convert)
movies.head()


# In[16]:


movies['cast'] = movies['cast'].apply(lambda x:x[0:3])


# In[17]:


def fetch_director(text):
    L = []
    for i in ast.literal_eval(text):
        if i['job'] == 'Director':
            L.append(i['name'])
    return L 


# In[18]:


movies['crew'] = movies['crew'].apply(fetch_director)


# In[19]:


movies.sample(5)


# In[20]:


def collapse(L):
    L1 = []
    for i in L:
        L1.append(i.replace(" ",""))
    return L1


# In[21]:


movies['cast'] = movies['cast'].apply(collapse)
movies['crew'] = movies['crew'].apply(collapse)
movies['genres'] = movies['genres'].apply(collapse)
movies['keywords'] = movies['keywords'].apply(collapse)


# In[22]:


movies.head()


# In[23]:


movies['overview'] = movies['overview'].apply(lambda x:x.split())


# In[24]:


movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']


# In[25]:


new = movies.drop(columns=['overview','genres','keywords','cast','crew'])


# In[26]:


new['tags'] = new['tags'].apply(lambda x: " ".join(x))
new.head()


# In[27]:


from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000,stop_words='english')


# In[28]:


vector = cv.fit_transform(new['tags']).toarray()


# In[29]:


vector.shape


# In[30]:


from sklearn.metrics.pairwise import cosine_similarity


# In[31]:


similarity = cosine_similarity(vector)


# In[32]:


def recommend(movie):
    index = new[new['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    for i in distances[1:6]:
        print(new.iloc[i[0]].title)
        
    


# In[33]:


recommend('Gandhi')


# In[34]:


import pickle


# In[35]:


pickle.dump(new,open('movie_list.pkl','wb'))
pickle.dump(similarity,open('similarity.pkl','wb'))


# In[ ]:





# In[ ]:





# In[ ]:




