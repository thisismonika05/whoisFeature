#!/usr/bin/env python
# coding: utf-8

# In[1]:


from urllib.parse import urlparse
url='http://wikipedia.org'
obj=urlparse(url)
print(obj.scheme)
print(obj.netloc)
print(obj.hostname)
print(obj.geturl())


# In[7]:


import whois

for x in whois.whois('google.com'):
    print(x)


# In[ ]:




