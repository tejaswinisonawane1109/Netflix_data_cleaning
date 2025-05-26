#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_csv('netflix_titles.csv')
df


# In[2]:


'''Identify Missing Values'''

df.isnull().sum()


# In[3]:


'''Handle Missing Values'''

df = df.dropna(subset=['title'])
df['country'] = df['country'].fillna('Unknown')
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Not Rated')
df['date_added'] = df['date_added'].fillna('01-Jan-1900')  # placeholder
print("\nMissing values after handling:\n", df.isnull().sum())


# In[4]:


'''Remove Duplicate Rows'''

print("\nShape before removing duplicates:", df.shape)
df = df.drop_duplicates()
print("Shape after removing duplicates:", df.shape)


# In[5]:


'''Standardize Text Values'''

df['country'] = df['country'].str.title().str.strip()
df['type'] = df['type'].str.title().str.strip()
df['rating'] = df['rating'].str.upper().str.strip()

print("\nUnique 'type' values after standardization:", df['type'].unique())
print("Unique 'rating' values after standardization:", df['rating'].unique())


# In[6]:


''' Convert Date Formats to dd-mm-yyyy'''

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['date_added'] = df['date_added'].dt.strftime('%d-%m-%Y')

print("\nSample 'date_added' values after formatting:")
print(df['date_added'].head())



# In[7]:


'''Rename Column Headers'''

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
print("\nColumn names after renaming:", df.columns.tolist())


# In[8]:


'''Check and Fix Data Types'''


print("\nData types after cleaning:\n", df.dtypes)


# In[9]:


df.to_excel('netflix_cleaned.xlsx', index=False)


# In[ ]:




