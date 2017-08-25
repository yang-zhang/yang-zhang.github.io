
# coding: utf-8

# In[1]:

from secrets import REDDIT_USER_NAME, REDDIT_PASSWORD, APP_CLIENT_ID, APP_CLIENT_SECRET


# In[2]:

import praw
reddit = praw.Reddit(client_id=APP_CLIENT_ID, client_secret=APP_CLIENT_SECRET,
                     password=REDDIT_PASSWORD, user_agent="test:com.example.myredditapp:v0.0.0 (by /u/yang-zhang)",
                     username=REDDIT_USER_NAME)


# In[5]:

subreddit = reddit.subreddit('test')


# In[8]:

subreddit.description


# In[ ]:



