#!/usr/bin/env python
# coding: utf-8

# <center><img src="http://i.imgur.com/sSaOozN.png" width="500"></center>

# ## Course: Computational Thinking for Governance Analytics
# 
# ### Prof. José Manuel Magallanes, PhD 
# * Visiting Professor of Computational Policy at Evans School of Public Policy and Governance, and eScience Institute Senior Data Science Fellow, University of Washington.
# * Professor of Government and Political Methodology, Pontificia Universidad Católica del Perú. 
# 
# _____
# <a id='home'></a>
# 
# # Data collecting

# 1. [The GitHub Repo](#part1) 
# 2. [Uploading files](#part2)
# 3. [APIs](#part3) 
# 4. [Scraping](#part4) 
# 5. [Social media](#part5) 

# ____
# <a id='part1'></a>
# 
# ## 1. The GitHub Repo
# 
# **Where is the Data?**
# **Where is the Code?**
# 
# We used GitHub as a way to organize our work. It helps transforming the way you access your code and data beyond your local machine; an easy way of experiencing the cloud. Follow these steps now:
# 
# 1. Go to [github.com](https://github.com/), and sign up. Remember your _username_ and _password_.
# 2. Install the Github *desktop app* in your computer. It is available [here](https://desktop.github.com/). Sign in using your _username_ and _password_ from GitHub web.
# 3. Once you are signed in, go back to the Github web, and create a _repository_. Choose a name. **DO NOT forget** to select the option to add a READ ME file, choose a **LICENSE** too.
# 4. **Clone** the repository just created into your computer. You can select where to clone the repository, avoid cloning into another's app folder (i.e. Dropbox).
# 
# 
# After those steps, let's open the data file that you find [here](https://drive.google.com/drive/folders/1uH6S-8rns8THDnBRCy3OGLEki9LjyTCL?usp=sharing). Once you open the file, you will see something like this:
# 

# In[8]:


from IPython.display import IFrame  
wikiLink="https://docs.google.com/spreadsheets/d/e/2PACX-1vRXdVAxZTnQ6N7bI1xJ_XRQSoG-FsiucGI_fsyBuKCi6TcO3guGB_-6nk4i6so7SG__eIpfS0o8pUuZ/pubhtml?widget=true&amp;headers=false" 
IFrame(wikiLink, width=700, height=300)


# Understanding what you see is not straightforward:
# 
# * What does these data represent?
# * What does each column represent?
# * What possible mistakes can appear in the data values?
# * What variables will be useful for my hypotheses and goals?
# 
# If this is the first time you run into a data set like this, you first need to **read** the documentation of the data (available in the same folder).
# 
# At this stage, you can download this data from GoogleDocs into the folder cloned from GitHub (now in your local machine). Download it first as a CSV file into your computer. 
# 
# Now, open GitHub Desktop App. You will see that the app is trying to tell you some changes have ocurred in your local folder cloned from GitHub. Now, let's **Commit** and **Push**, that will syncronize contents in your local repo and your cloud repo.
# 
# In *my own* repo, it looks like [this](https://github.com/EvansDataScience/data/blob/master/HSBfromGoogle.csv).
# 
# GitHub allows you to see the data contents (it is not always possible). Now, find the icon **raw** and copy its link address (**do not** copy the URL of the page). This is mine:
# 
# https://github.com/EvansDataScience/data/blob/master/HSBfromGoogle.csv
# 
# Now let's get ready for Python.
# 
# [home](#home)

# ____
# <a id='part2'></a>
# 
# ## 2. Uploading files

# The file we are planing to read into Python is a data table. Python needs support from one of its libraries to deal with data tables: **PANDAS**
# 
# * Check if you already have Pandas.
# * If you do not have it, install it.

# In[9]:


# do I have it?
get_ipython().system('pip show pandas')


# In[10]:


# if you do not have it:
#!pip install pandas


# Now that I have it, I can read in the data, so that I can work on it:

# In[11]:


# call pandas
import pandas as pd # 'pd' is a nickname

# use a function from pandas to read the cloud data into a Python object
gitCloudRepo='https://github.com/EvansDataScience/data/raw/master/'
fileName="HSBfromGoogle.csv"
DFcsv=pd.read_csv(gitCloudRepo + fileName)


# If Python has not **complained**, that is, you got no error messages, then, you are good to continue!
# 
# The **DFcsv** Python object holds the data:

# In[12]:


DFcsv


# This object is of a particular type:

# In[13]:


type(DFcsv)


# The type is **Data Frame** (DF). We will see several functions that can be applied to DFs. Let me show you some basic ones.

# In[14]:


# dimensions (rows,columns)
DFcsv.shape


# In[15]:


# top / bottom
DFcsv.head(10) #tail()


# In[16]:


# column names
DFcsv.columns


# In[17]:


# access by index position
DFcsv.iloc[:,4]


# In[18]:


# access by index names
DFcsv.loc[:,'sctyp']


# In[19]:


# subdata frame
DFcsv[['sctyp']]


# And the most important for future sessions:

# In[20]:


DFcsv.info() # the data types Python has assigned


# Python will not care about the original data file (CSV, EXCEL. etc.), once they are read into Python you will have a DF.

# **Proprietary Sofware**
# 
# Several times, you may find that you are given a file that was previously prepared with proprietary software. The most common in the policy field are:
# 
# * SPSS (file extension: **sav**).
# * STATA (file extension: **dta**).
# * EXCEL (file extension: **xlsx** or **xls**).
# 
# Getting these files up and running might not bring much pre processing challenges. However, you may need different levels of effort to read them from **GitHub**: they will not be as easy to open as a CSV.
# 
# Download [these files](https://drive.google.com/drive/folders/1XxTztY6rFkGwbR7wUtO_xiD4xvBrFqJN?usp=share_link) into the repository where your CSV file is currently stored in your local machine, then commit and push.

# **Exercise:**
#     
# Open the other files (excel, spss, stata). 
# 
# **TIPS**
# 
# Check these functions: 
# * For STATA: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_stata.html
# * FOR EXCEL: 
#     - https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html
#     - https://openpyxl.readthedocs.io/en/stable/
#     - https://xlrd.readthedocs.io/en/latest/
# * FOR SPSS:
#     - https://pandas.pydata.org/docs/reference/api/pandas.read_spss.html
#     - https://github.com/Roche/pyreadstat
# 
# Opening SPSS is more challenging.
# 
# 
# Check if all the functions work well with the DFs created. Verify if the results are the same.

# [home](#home)
# 
# ____
# 
# <a id='part3'></a>
# 
# ## 3. Collecting data from APIs
# 
# Open data portals from the government and other organizations have APIs, a service that allows you to collect their data. Let's take a look a Seattle data about [Seattle Real Time Fire 911 Calls](https://data.seattle.gov/Public-Safety/Seattle-Real-Time-Fire-911-Calls/kzjm-xkqj).

# That page tells you how to get the data into pandas. But first, you need to install **sodapy**. Then you can continue:

# In[21]:


#!pip install sodapy


# Let's follow some steps, according to the API:

# In[22]:


from sodapy import Socrata

# Unauthenticated client (using 'None')

client = Socrata("data.seattle.gov", None)

# If you have credentials:
# client = Socrata(data.seattle.gov,
#                  MyAppToken,
#                  username="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("kzjm-xkqj", limit=2000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)


# You can see the results now:

# In[23]:


results_df


# Data from APIs may need some more pre processing than the previous files. Besides, you should study the API documentation to know how to interact with the portal. Not every open data portal behaves the same.

# [home](#home)
# ____
# <a id='part4'></a>
# 
# ## 4. Scraping

# Sometimes you are interested in data from the web. Let me get a table from wikipedia:

# In[24]:


from IPython.display import IFrame  
wikiLink="https://en.wikipedia.org/wiki/Democracy_Index" 
IFrame(wikiLink, width=700, height=300)


# I will use pandas to get the table, but you need to install these libraries first:
# * html5lib 
# * beautifulsoup4
# * lxml

# In[25]:


DFwiki=pd.read_html(wikiLink,header=0,flavor='bs4',attrs={'class': 'wikitable'})


# Pandas has this command **read_html** that will save lots of coding, above I just said:
# * The link to the webpage.
# * The position of the header.
# * The external library that will be used to extract the text (_flavor_).
# * The attributes of the table.

# DFwiki is not a data frame:

# In[26]:


type(DFwiki)


# The command **read_html** returned all the tables with the attribute _wikitable_. Since there may be more than one, a **list** of tables is returned. Lists are the most flexible container offered by Python:

# In[27]:


aList=[1,2,'a','*']
aList


# Lists have several interesting functions and properties:

# In[28]:


# amount of elements
len(aList)


# In[29]:


# get element
aList[2]


# In[30]:


# replace
aList[3]="**"
aList


# In[31]:


# add element
aList.append(4)
aList


# In[32]:


# erase element
del aList[0]
aList


# And the nicest of all: **list comprehension**

# In[33]:


# list of the squared first five positive integers (0 to 4)
easyList_1=[x**2 for x in range(5)]
easyList_1


# In[34]:


# list of multiples of 5 smaller than 50
easyList_2=[x for x in range(50) if x%5==0 and x>0]
easyList_2


# In[35]:


someNames=["Peter","John","Rob", "Ron", "Mike"]
easyList_3=[x for x in someNames if not x.startswith('R')]
easyList_3


# In[36]:


import math

someNumbers=[-1,4,6,-3]
easyList_4a=[math.pow(x,2) for x in someNumbers ]
easyList_4a


# In[37]:


# when using'else' write 'for' at the end
easyList_4b=[math.sqrt(x) if x >=0 else None for x in someNumbers]
easyList_4b


# Coming back to our example from wikipedia, we first should check how many DFs we have:

# In[38]:


len(DFwiki)


# Is ours the first one?

# In[39]:


# remember that Python starts counting in ZERO!
DFwiki[0]


# or the last one?

# In[40]:


DFwiki[4]


# Tables scrapped will bring different cleaning challenges. 
# 
# [home](#home)
# ____
# <a id='part5'></a>
# 
# ## 5. Social media data

# Social media offer APIs too that allow you to get _some_ data. To use this service, you need to register as a developer. For our Twitter example, you should go [here](https://developer.twitter.com/en).
# Once you are a confirmed developer, Twitter, Facebook and others will allow you to get _some_ of their data (the more you pay the more you get). 
# 
# Let's pay attention to Twitter. First, check if you have **tweepy**:

# In[41]:


get_ipython().system('pip show tweepy')


# In[42]:


#!pip install tweepy


# Tweepy is the key library, but you may need several other libraries according to your goals.

# In[43]:


import tweepy


# Let me introduce myself to Twitter:

# In[44]:


# credentials from a file
import json
keysAPI = json.load(open('APIkeys.txt','r'))

# getting info from the file
api_key = keysAPI['api_key']
api_key_secret = keysAPI['api_key_secret']
access_token = keysAPI['access_token']
access_token_secret = keysAPI['access_token_secret']

# introducing myself:
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api=tweepy.API(auth, wait_on_rate_limit=True,timeout=60,
               parser=tweepy.parsers.JSONParser())


# Let me ask for some tweets from a particular user:

# In[45]:


who='@WAStateGov'
howMany=100
gottenTweets = api.user_timeline(screen_name = who, 
                                 count = howMany, 
                                 include_rts = True,
                                 tweet_mode="extended")


# In the previous cases, I got a table (a data frame), you should always check what you have:

# In[46]:


type(gottenTweets)


# I have a list, then I could ask how many tweets I got (just to confirm):

# In[47]:


len(gottenTweets)


# Let me view what I have in the first tweet:

# In[48]:


gottenTweets[0]


# It will take some time to become familiar with a [tweet object structure](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet). Let's find out how each tweet is currently stored:

# In[49]:


type(gottenTweets[0])


# Now you know that each tweet is stored as a **dictionary**. 
# Dictionaries or **dicts** are very flexible and important structures in Python. Let me show you a simple one: 

# In[50]:


aDictExample={"name":"Peter",
             "speaks":['French', 'Spanish'],
             'country':'Morocco'}

# then
aDictExample


# Dicts are a basic structure in Python, and one that makes Python very appealing. Each element in Python can be accessed via **keys**. Our _aDictExample_ has these keys:

# In[51]:


aDictExample.keys()


# So, you access the info like this:

# In[52]:


aDictExample['speaks']


# Then, let's see our **gottenTweets** keys:

# In[53]:


gottenTweets[0].keys()


# In[54]:


# then:
gottenTweets[0]['created_at']


# In[55]:


gottenTweets[1]['created_at']


# We could prepare a data frame using the current tweets, first let's prepare a list of each of fields we want:

# In[56]:


# list comprehesions
dates=[t['created_at'] for t in gottenTweets]
ids=[t['id'] for t in gottenTweets]
rts=[t['retweet_count'] for t in gottenTweets]
likes=[t['favorite_count'] for t in gottenTweets]
text=[t['full_text'] for t in gottenTweets]
rtw=[t['full_text'].startswith('RT') for t in gottenTweets]


# Each of the objects created is a list (dates, ids,rts,likes and text). Let me show you one:

# In[57]:


rtw


# Let me create a data frame with those lists:

# In[58]:


dictOfColsAsLists={'dates':dates,'ids':ids,'rts':rts,
                   'likes':likes,'text':text,'rtw':rtw}
tweetsAsDF=pd.DataFrame(dictOfColsAsLists)


# In[59]:


tweetsAsDF


# You can know how many are retweets or not:

# In[60]:


tweetsAsDF[tweetsAsDF['rtw']==False].shape


# In[61]:


tweetsAsDF[tweetsAsDF['rtw']==True].shape


# [home](#home)
