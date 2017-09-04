
# coding: utf-8

# # PRAW Tutorial

# Use PRAW to use Reddit.

# For setup, see [here](http://nbviewer.jupyter.org/github/yang-zhang/yang-zhang.github.io/blob/master/ds_app/reddit/reddit_setup.ipynb).

# In[109]:

from secrets import REDDIT_USER_NAME, REDDIT_PASSWORD, APP_CLIENT_ID, APP_CLIENT_SECRET


# In[110]:

import praw
reddit = praw.Reddit(client_id=APP_CLIENT_ID, 
                     client_secret=APP_CLIENT_SECRET,
                     password=REDDIT_PASSWORD, 
                     user_agent="test:com.example.myredditapp:v0.0.0 (by /u/yang-zhang)",
                     username=REDDIT_USER_NAME)


# ## Reddit

# In[28]:

for submission in reddit.front.hot(limit=3):
    print(submission.title, '\n')


# In[29]:

all_ = reddit.subreddit('all')
for submission in all_.hot(limit=3):
    print(submission.title, '\n')


# ## Me

# In[30]:

me = reddit.user.me()
me


# In[ ]:




# In[ ]:

list(reddit.user.subreddits(limit=None))


# What articles have I saved?

# In[36]:

for saved in me.saved():
    if isinstance(saved, praw.models.Submission):
        print('TITLE:', saved.title)
    else:
        print('BODY:', saved.body)


# ## Subreddit

# In[57]:

subreddit = reddit.subreddit('datascience')


# In[58]:

print(subreddit.description)


# In[59]:

for submission in subreddit.top(limit=10):
    print(submission.title, '\n')


# Sum of subreddits

# In[60]:

subreddit = reddit.subreddit('datascience+python+learnpython')
for submission in subreddit.top(limit=5):
    print(submission.title, '\n')


# ## Submission

# In[93]:

submission


# In[99]:

submission.title


# In[95]:

print(submission.selftext)


# In[112]:

multi = reddit.multireddit('yang-zhang', 'work')


# In[115]:

for s in multi.top(limit=3):
    print(s.title)


# ## Redditor

# In[121]:

submission.author.id


# In[119]:

praw.models.Redditor

