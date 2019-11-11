#!/usr/bin/env python
# coding: utf-8

# In[1]:


import whois
import datetime
from urllib.parse import urlparse

url = 'google.com'
res=whois.whois(url)

    #to get the updation date
print(res.updation_date)

    #to get the creation date
print(res.creation_date)

    #to get the expiration gate
print(res.expiration_date)

    #to get registrar name
print(res.registrar)


# In[4]:


print(whois.__file__)


# In[5]:


import whois
import datetime
from urllib.parse import urlparse

def getFeatures(url, label): 
    result = []
    url = str(url)
    
    #add the url to feature set
    result.append(url)

    #Get domain information by asking whois
    url =''
    host = whois.whois(url)

    avg_month_time=365.2425/12.0

    #calculate creation age in months

    if host.creation_date == None or type(host.creation_date) is str :
        result.append(-1)
    else:
        if(type(host.creation_date) is list): 
            create_date=host.creation_date[-1]
        else:
            create_date=host.creation_date

        if(type(create_date) is datetime.datetime):
            today_date=datetime.datetime.now()
            create_age_in_mon=((today_date - create_date).days)/avg_month_time
            create_age_in_mon=round(create_age_in_mon)
            result.append(create_age_in_mon)
        else:
            result.append(-1)


    #calculate expiry age in months

    if(host.expiration_date==None or type(host.expiration_date) is str):
        result.append(-1)
    else:
        if(type(host.expiration_date) is list):
            expiry_date=host.expiration_date[-1]
        else:
            expiry_date=host.expiration_date
        if(type(expiry_date) is datetime.datetime):
            today_date=datetime.datetime.now()
            expiry_age_in_mon=((expiry_date - today_date).days)/avg_month_time
            expiry_age_in_mon=round(expiry_age_in_mon)
            result.append(expiry_age_in_mon)
        else:
            result.append(-1)

    #find the age of last update

    if(host.updated_date==None or type(host.updated_date) is str):
        result.append(-1)
    else:
        if(type(host.updated_date) is list):
            update_date=host.updated_date[-1]
        else:
            update_date=host.updated_date
        if(type(update_date) is datetime.datetime):
            today_date=datetime.datetime.now()
            update_age_in_days=((today_date - update_date).days)
            result.append(update_age_in_days)
        else:
            result.append(-1)

    #find the registrar_name hosting this domain
    if(host.registrar == None):
        result.append("None")
    else:
        result.append(host.registrar)


    


# In[2]:


import whois
host = 'google.com'
res=whois.whois(host)
print(res)


# In[ ]:




