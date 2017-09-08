
# coding: utf-8

# # Setup Reddit API

# In[1]:

import pprint

from secrets import REDDIT_USER_NAME, REDDIT_PASSWORD, APP_CLIENT_ID, APP_CLIENT_SECRET


# secrets.py
# ```
# REDDIT_USER_NAME = "yang-zhang"
# REDDIT_PASSWORD = "SECRET"
# 
# # My Example App
# APP_CLIENT_ID = "SECRET"
# APP_CLIENT_SECRET = "SECRET"
# ```

# ### Using requests

# In[2]:

import requests


# In[3]:

client_auth = requests.auth.HTTPBasicAuth(APP_CLIENT_ID, APP_CLIENT_SECRET)
post_data = {"grant_type": "password", "username":REDDIT_USER_NAME, "password": REDDIT_PASSWORD}
headers = {"User-Agent": "test:com.example.myredditapp:v0.0.0 (by /u/yang-zhang)"}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)


# In[4]:

access_token = response.json()['access_token']


# In[ ]:

headers = {"Authorization": "bearer %s" % access_token, "User-Agent": headers['User-Agent']}
response = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
pprint.pprint(response.json())


# ### Using praw

# In[6]:

import praw
reddit = praw.Reddit(client_id=APP_CLIENT_ID, client_secret=APP_CLIENT_SECRET,
                     password=REDDIT_PASSWORD, user_agent="test:com.example.myredditapp:v0.0.0 (by /u/yang-zhang)",
                     username=REDDIT_USER_NAME)


# In[7]:

# Create a submission to /r/test
reddit.subreddit('test').submit('Test Submission', url='https://reddit.com')


# In[8]:

# Comment on a known submission
submission = reddit.submission(url='https://www.reddit.com/comments/6vvlcm')
submission.reply('Super rad!')


# In[ ]:

# Output score for the first 256 items on the frontpage
for submission in reddit.front.hot(limit=256):
    print(submission.score)


# Reference:
# - https://github.com/reddit/reddit/wiki/OAuth2-Quick-Start-Example

# [Home](https://yang-zhang.github.io/)
