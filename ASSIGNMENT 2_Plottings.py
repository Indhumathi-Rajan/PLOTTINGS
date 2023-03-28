#!/usr/bin/env python
# coding: utf-8

# ## PLOTTING DISTRIBUTIONS

# ## The World's Biggest Public Companies 2021
# 
# #### Since 2003, Forbes’ Global 2000 list has measured the world’s largest public companies in terms of four equally weighted metrics: assets, market value, sales and profits.You can find the biggest 500 companies in this data.

# In[1]:


import pandas as pd
import matplotlib.pyplot as plot
import seaborn as sns


# #### pandas library imported as pd for data exploration
# #### matplotlib library imported as plot and seaborn library imported as sns for plotting.

# In[2]:


data=pd.read_csv("C://Users//indhu//OneDrive//Documents//PYTHON WORKINGS//The Worlds Biggest Public Companies.csv")


# #### The Worlds Biggest Public Companies data is read from location.

# In[3]:


data


# #### This dataset is downloaded from kaggle.com

# In[4]:


data1=data[(data['Market Value(in Billion)']>200)]
data1


# #### Subset for the dataset is created based on Market value.

# In[5]:


x= list(data1.iloc[:,1])
y= list(data1.iloc[:,6])
plot.bar(x,y,color='purple')
plot.title("Name vs Market Value")
plot.xlabel("Name")
plot.ylabel("Market Value(in Billion)")
plot.xticks(color='r',rotation=90,fontweight='bold',fontsize='7',horizontalalignment='right')


# #### From this bar graph we can find the highest market value companies.
# #### Here we can see tha Apple company has the highest market value.
# #### Only 5 companies have market value more than 1000 billion.
# #### Most of the companies falls below 500 billion of market value.

# In[6]:


data.describe()


# #### Basic statistics of the dataset.

# In[7]:


plot.boxplot(data['Assets(in Billion)'])
plot.show()


# #### From this boxplot we can find the outliers.
# #### Most of the values falls approximately between 750 and 1500 billion.

# In[8]:


plot.boxplot(data['Assets(in Billion)'])
plot.yscale('log')
plot.show()


# #### Log is taken for the boxplot for better understanding.
# #### Here the mean value is situated apart from the Asset values of the companies. So the mean value doesnot provide us more accurate details.

# In[9]:


plot.hist(data['Sales(in Billion)'],color='violet')
plot.show()


# #### From this histogram, we can find that most of the sales takes place below 50 billion.

# In[10]:


plot.hist(data['Sales(in Billion)'],color='blue')
plot.yscale('log')
plot.show()


# #### From this histogram, we can find that sales doesnot takes place between 400 and 500 billion.

# In[11]:


plot.scatter(data['Sales(in Billion)'],data['Profit(in Billion)'],color='red')
plot.show()


# #### From this scatterplot we can understand that most of the Sales takes place below 100 billion and Profit takes place between -5 and 10 billion.
# #### Only very few sales takes place more than 300 billion.
# #### Only few profit takes place more than 40 billion.

# In[12]:


sns.distplot(data['Sales(in Billion)'],color='red')
plot.show()


# #### From this distplot we can find that most of the sales falls below 50 billion.
# #### Very few sales takes place more than 300 billion.

# In[13]:


sns.distplot(data['Sales(in Billion)'][:250],rug=True,color='red')
plot.show()


# #### From this distplot with showing rug we can find highest density tales place below 100 billion.
# #### Very few sales takes place between 150 and 300 billion.
# #### There is only 1 sales takes place between 300 and 400 billion.
# #### There is only 1 sales takes place above 400 billion.

# In[14]:


sns.distplot(data['Sales(in Billion)'],hist=False)
plot.show()


# #### From this distplot without Histogram,the line shows the level of highest and lowest sales that takes place.

# In[15]:


plot.subplot(3,2,1)
plot.title('Sales(in Billion)')
sns.distplot(data['Sales(in Billion)'])

plot.subplot(3,2,2)
plot.title('Profit(in Billion)')
sns.distplot(data['Profit(in Billion)'])

plot.subplot(3,2,3)
plot.title('Assets(in Billion)')
sns.distplot(data['Assets(in Billion)'])

plot.subplot(3,2,4)
plot.title('Market Value(in Billion)')
sns.distplot(data['Market Value(in Billion)'])

plot.tight_layout()
plot.show()


# #### Subplots are created to compare with each other.

# In[16]:


sns.boxplot(y=data['Sales(in Billion)'])
plot.title('SALES(in Billion)')

plot.show()


# #### Here the Seaborn library is used for plotting the boxplot.From this boxplot we can find the outliers.
# #### Most of the sales takes place approximately between 120 and 200 billion.

# In[17]:


sns.boxplot(y=data['Sales(in Billion)'])
plot.title('SALES(in Billion)')
plot.yscale('log')

plot.show()


# #### Log is taken for clear observation.
# #### The mean value is situated apart from the Sales values. So the mean value doesnot provide any accurate observation.

# In[18]:


sns.jointplot('Sales(in Billion)','Profit(in Billion)', data)
plot.show()


# #### Seaborn library is used for plotting tha joinplot.
# #### Here the scatterplot and the histogram is joined together to provide us clear observation.
# #### We can find that most of the Sales takes place below 100 billion and Profit takes place between -5 and 10 billion.
# #### Only very few sales takes place more than 300 billion.
# #### Only few profit takes place more than 40 billion.

# In[19]:


subset=data[(data['Sales(in Billion)'] <200) & (data['Profit(in Billion)']<20)]


# In[20]:


subset


# #### Subset is created from the dataset based on Sales and Profit.

# In[21]:


sub_heat=data[(data['Profit(in Billion)'] <10) & (data['Profit(in Billion)'] <10) & (data['Sales(in Billion)'])]
sns.jointplot('Sales(in Billion)','Profit(in Billion)',sub_heat,kind='hex', color='Purple')
plot.show()


# #### From this heatmap, we can understand that most of the sales takes place below 25 billion and profit takes place below 3 billion.
# #### Negative profits also takes place.
# #### Few sales takes place more than 150 billion.
# 
