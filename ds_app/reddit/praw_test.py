
# coding: utf-8

# In[63]:

from secrets import REDDIT_USER_NAME, REDDIT_PASSWORD, APP_CLIENT_ID, APP_CLIENT_SECRET


# In[64]:

import praw
reddit = praw.Reddit(client_id=APP_CLIENT_ID, 
                     client_secret=APP_CLIENT_SECRET,
                     password=REDDIT_PASSWORD, 
                     user_agent="test:com.example.myredditapp:v0.0.0 (by /u/yang-zhang)",
                     username=REDDIT_USER_NAME)


# In[84]:

subreddit = reddit.subreddit('python')


# In[85]:

print(subreddit.description)


# In[67]:

for submission in subreddit.hot(limit=10):
    print(submission.title)
    print(submission.score)
    print(submission.id)
    print(submission.url)


# In[68]:

submission = reddit.submission(id='6qtmnu')
print(submission.title)


# In[69]:

redditor = submission.author
redditor.name


# In[70]:

redditor = reddit.redditor('yang-zhang')


# In[71]:

redditor.link_karma


# In[72]:

list(redditor.saved())


# In[73]:

submission.comment_sort = 'new'


# In[74]:

top_level_comments = list(submission.comments)


# In[75]:

top_level_comments[0]


# In[76]:

import pprint
pprint.pprint(vars(submission))


# In[77]:

reddit.front


# In[78]:

submission = reddit.submission(url='https://www.reddit.com/r/funny/comments/3g1jfi/buttons/')


# In[83]:

submission.url


# In[80]:

for top_level_comment in submission.comments:
    print(top_level_comment.body)b


# In[ ]:



