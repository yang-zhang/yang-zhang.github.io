
# coding: utf-8

# http://www.pythonchallenge.com/

# In[1]:

2**38


# In[15]:

riddle = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

def decode(riddle):
    ord_a = ord('a')
    print(''.join([chr(((ord(letter)-ord_a+2) % 26) + ord_a) if ord('a')<=ord(letter)<=ord('z') else letter for letter in riddle]))

decode(riddle)

decode('map')


# In[19]:

with open('mess02', 'r') as f:
    mess02 = f.read()

from collections import Counter
Counter(mess02)

''.join([i for i in mess02 if ord('a')<=ord(i)<=ord('z')])


# In[22]:

with open('mess03', 'r') as f:
    mess03 = f.read()

mess03[:100]

def is_small(c):
    return ord('a')<=ord(c)<=ord('z')

def is_big(c):
    return ord('A')<=ord(c)<=ord('Z')

is_big(mess03[2])

ms=mess03
for i in range(1, len(ms)):
    if not is_big(ms[i-1]) and     is_big(ms[i]) and     is_big(ms[i+1]) and     is_big(ms[i+2]) and     is_small(ms[i+3]) and     is_big(ms[i+4]) and     is_big(ms[i+5]) and     is_big(ms[i+6]) and     not is_big(ms[i+7]):
        print(ms[i+3])


# In[6]:

nothing = '12345'

for _ in range(400):
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + nothing

    u = urllib.request.urlopen(url)

    answer = u.read().decode("utf-8")

    nothing = answer.split(' ')[-1]
    
    print(nothing)


# http://www.pythonchallenge.com/pc/def/peak.html

# In[44]:

import pickle

puzzle = pickle.load(urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p'))

for i in range(len(puzzle)):
    print(''.join(j[0]*j[1] for j in puzzle[i]))


# http://www.pythonchallenge.com/pc/def/channel.html

# http://www.pythonchallenge.com/pc/def/channel.zip

# In[72]:

url = 'http://www.pythonchallenge.com/pc/def/channel.zip'
import requests, zipfile, io
r = requests.get(url)
z = zipfile.ZipFile(io.BytesIO(r.content))
comments = []

i = '90052'
fn = '%s.txt' % i

while True:
    try:
        data = z.read(fn).decode("utf-8")
        i = str(data).split(' ')[-1]
        comments.append(z.getinfo(fn).comment.decode("utf-8"))
        fn = '%s.txt' % i
    except:
        break


# In[74]:

print(''.join(comments))


# http://www.pythonchallenge.com/pc/def/hockey.html

# http://www.pythonchallenge.com/pc/def/oxygen.html

# In[138]:

from PIL import Image
import requests
import io
url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
im = Image.open(io.BytesIO(requests.get(url).content))

w, h = im.size

ans=[]
for i in range(43, 44):
    for j in range(0, w, 7):
        ans.append(chr(im.getpixel((j, i))[0]))

''.join(ans)


# In[123]:

''.join([chr(i) for i in [105, 110, 116, 101, 103, 114, 105, 116, 121]])


# http://www.pythonchallenge.com/pc/def/integrity.html

# In[129]:

import bz2
un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
print(bz2.decompress(un).decode('utf-8'), bz2.decompress(pw).decode('utf-8'))


# http://www.pythonchallenge.com/pc/return/good.html

# In[164]:

first=[
146,399,163,403,170,393,169,391,166,386,170,381,170,371,170,355,169,346,167,335,170,329,170,320,170,
310,171,301,173,290,178,289,182,287,188,286,190,286,192,291,194,296,195,305,194,307,191,312,190,316,
190,321,192,331,193,338,196,341,197,346,199,352,198,360,197,366,197,373,196,380,197,383,196,387,192,
389,191,392,190,396,189,400,194,401,201,402,208,403,213,402,216,401,219,397,219,393,216,390,215,385,
215,379,213,373,213,365,212,360,210,353,210,347,212,338,213,329,214,319,215,311,215,306,216,296,218,
290,221,283,225,282,233,284,238,287,243,290,250,291,255,294,261,293,265,291,271,291,273,289,278,287,
279,285,281,280,284,278,284,276,287,277,289,283,291,286,294,291,296,295,299,300,301,304,304,320,305,
327,306,332,307,341,306,349,303,354,301,364,301,371,297,375,292,384,291,386,302,393,324,391,333,387,
328,375,329,367,329,353,330,341,331,328,336,319,338,310,341,304,341,285,341,278,343,269,344,262,346,
259,346,251,349,259,349,264,349,273,349,280,349,288,349,295,349,298,354,293,356,286,354,279,352,268,
352,257,351,249,350,234,351,211,352,197,354,185,353,171,351,154,348,147,342,137,339,132,330,122,327,
120,314,116,304,117,293,118,284,118,281,122,275,128,265,129,257,131,244,133,239,134,228,136,221,137,
214,138,209,135,201,132,192,130,184,131,175,129,170,131,159,134,157,134,160,130,170,125,176,114,176,
102,173,103,172,108,171,111,163,115,156,116,149,117,142,116,136,115,129,115,124,115,120,115,115,117,
113,120,109,122,102,122,100,121,95,121,89,115,87,110,82,109,84,118,89,123,93,129,100,130,108,132,110,
133,110,136,107,138,105,140,95,138,86,141,79,149,77,155,81,162,90,165,97,167,99,171,109,171,107,161,
111,156,113,170,115,185,118,208,117,223,121,239,128,251,133,259,136,266,139,276,143,290,148,310,151,
332,155,348,156,353,153,366,149,379,147,394,146,399]

second=[
156,141,165,135,169,131,176,130,187,134,191,140,191,146,186,150,179,155,175,157,168,157,163,157,159,
157,158,164,159,175,159,181,157,191,154,197,153,205,153,210,152,212,147,215,146,218,143,220,132,220,
125,217,119,209,116,196,115,185,114,172,114,167,112,161,109,165,107,170,99,171,97,167,89,164,81,162,
77,155,81,148,87,140,96,138,105,141,110,136,111,126,113,129,118,117,128,114,137,115,146,114,155,115,
158,121,157,128,156,134,157,136,156,136]
from PIL import Image, ImageDraw
im = Image.new('RGB', (500, 500))
draw = ImageDraw.Draw(im)
draw.polygon(first, fill='white')
im


# http://www.pythonchallenge.com/pc/return/bull.html
# 
# a = [1, 11, 21, 1211, 111221,

# In[189]:

x = 111221

def look_and_say(x):
    x_str = str(x)

    d = x_str[0]
    result = [[1, d], ]
    i = 1
    while i < len(x_str):
        if x_str[i]==d:
            result[-1][0]+=1
        else:
            result.append([1, x_str[i]])
            d = x_str[i]
        i+=1
    return ''.join([str(j[0])+j[1] for j in result])


# In[201]:

x = 1
for i in range(30):
    x = look_and_say(x)


# In[202]:

len(x)


# http://www.pythonchallenge.com/pc/return/5808.html

# In[207]:

url = 'https://the-python-challenge-solutions.hackingnote.com/images/cave.jpg'
import requests
import io
from PIL import Image
im = Image.open(io.BytesIO(requests.get(url).content))
w, h = im.size
even = Image.new('RGB', (w//2, h//2))
odd = Image.new('RGB', (w//2, h//2))
for i in range(w):
    for j in range(h):
        p = im.getpixel((i, j))
        if (i+j)%2==0:
            even.putpixel((i//2, j//2), p)
        else:
            odd.putpixel((i//2, j//2), p)


# In[208]:

even


# http://www.pythonchallenge.com/pc/return/evil.html

# In[7]:

with open('evil2.gfx', 'rb') as f:
    data = f.read() 


# In[13]:

for i in range(5):
    open('%d.jpg' % i, 'wb').write(data[::5])


# In[22]:

from IPython.display import Image
Image("1.jpg")


# http://www.pythonchallenge.com/pc/return/disproportional.html

# In[25]:

import xmlrpc.client
conn = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
conn.system.listMethods()


# In[26]:

conn.phone('Bert')


# http://www.pythonchallenge.com/pc/return/italy.html

# In[29]:

io.BytesIO(requests.get(url).content)


# In[34]:

import requests
import io
from PIL import Image
im = Image.open('wire.png')
im.size


# In[37]:

def next_location_and_direction(current_location, direction, left_bound, right_bound, up_bound, low_bound):
    x, y = current_location
    nd = direction
    if direction=='right':
        if x+1<right_bound:
            nl = x+1, y
        else:
            right_bound -= 1
            nd='down'
            nl = x, y+1
    elif direction=='down':
        if y+1<low_bound:
            nl = x, y+1
        else:
            low_bound -= 1
            nd='left'
            nl = x-1, y
    elif direction=='left':
        if x-1>=left_bound:
            nl = x-1, y
        else:
            left_bound += 1
            nd='up'
            nl = x, y-1
    elif direction=='up':
        if y-1>=up_bound:
            nl = x, y-1
        else:
            up_bound += 1 
            nd='right'
            nl = x+1, y
    else:
        raise Exception('nonsense direction!')
#     print(nl, nd, left_bound, right_bound, up_bound, low_bound)
    return nl, nd, left_bound, right_bound, up_bound, low_bound
    
    


# In[38]:

w = 4
h = 4
location = (0, 0)
direction='right'

left_bound = 0
right_bound = w
up_bound = 1
low_bound = h
for i in range(w*h):
    location, direction, left_bound, right_bound, up_bound, low_bound = next_location_and_direction(location, direction, left_bound, right_bound, up_bound, low_bound)   


# In[39]:

from PIL import Image
im_new = Image.new('RGB', [100, 100])
w = 100
h = 100

left_bound = 0
right_bound = w
up_bound = 1
low_bound = h

location = (0, 0)
direction = 'right'
for i in range(im.size[0]):
    px = im.getpixel((i, 0))
    im_new.putpixel(location, px)
    location, direction, left_bound, right_bound, up_bound, low_bound =     next_location_and_direction(location, direction, left_bound, right_bound, up_bound, low_bound)
im_new.save('italy_out.jpg')
from IPython.display import Image as IPython_Image
IPython_Image("italy_out.jpg")


# http://www.pythonchallenge.com/pc/return/cat.html

# In[ ]:



