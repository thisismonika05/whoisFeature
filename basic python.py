#!/usr/bin/env python
# coding: utf-8

# In[3]:


n=20
m=45
prod=n*m
print(f'the product of {n} and {m} is {prod}')
print("hell",n)


# In[7]:


s="footer"
s=s[:3] + 'x' + s[4:] #changes can be easily made
print(s)


# In[8]:


s="foobar"
s=s.replace('b','x')
print(s)


# In[19]:


u="lalala"
v="la la la"
print(u.count("la"))
print(v.count("la"))


# In[23]:


p="My name is Monika"
print(p.partition('n'))
print(p.rsplit('n'))
print(p.rsplit()) #default value is whitespace


# In[24]:


#lists,tuples and dictionaries(Iterables)
#Python lists
a= ['foo',56,['yoyo',45,6.7]]
print(a)


# In[30]:


p=["yo","oh"]
q=["oh","yo"]
print(p==q)

#lists are ordered


# In[31]:


a=['string',2,'x',5]
print(a[::-1])


# In[37]:


a=['string',2,'x',5]
print(a[::-1])
a=['foo','bar','yoyo']
print(min(a))
print(max(a))
print(a*5)


# In[38]:


a=['string',2,'x',5]
print(a*5)


# In[39]:


num=[23,45,78]
num1=[34,67]
num2=[56,456,871]
print('Minimum is',min(num,num1,num2,key=len))


# In[45]:


a=['foo','bar','yoyo','oho','haha']
a[:3]=[]
print(a)
del a[0:2]
print(a)


# In[47]:


a=['a','b']
a.append(123)
print(a)


# In[49]:


a=['a','b']
a.append(['yolo',45,6.7])
print(a)


# In[51]:


a=['a','b']
b=['yolo',45,6.7]
a.append(b)
print(a)
print(a+b)


# In[52]:


a=['a','b']
b=['yolo',45,6.7]

print(a+b)


# In[55]:


#insert
a=['foo','bar','yoyo','oho','haha']
a.insert(2,'lol')
print(a)


# In[56]:


a.remove('oho')
print(a)


# In[62]:


#tuples are immutable
t=('foo','bar','yoyo','oho','haha')
reverse=[::-1]
print(t(reverse))


# In[67]:


#packing and unpacking
t=('foo','bar','yoyo','oho')
a=4
b=4
a,b,c,d=t
print(d)


# In[68]:


a,b=5,2
print(a,b)
b,a=a,b
print(a,b)


# In[78]:


friends={1:'phebe',2:'chandler',3:'Monica',4:'Ross',5:'joey',6:'rachel'}
print(friends)
t=('foo','bar','yoyo','oho')
dict = {'Name': 'mon', 1: [1, 2, 3, 4]}
print(dict)


# In[84]:


friends={1:'phebe',2:'chandler',3:'Monica',4:'Ross',5:'joey',6:'rachel'}
print(friends)
friends[2]="chandu"
print(friends)
friends[7]="gunther"
print(friends)
friends[8]={1:"cat",2:"food"}
print(friends)
print(friends[8])


# In[85]:


1 in friends


# In[86]:


9 in friends


# In[89]:


'Monica' in friends


# In[93]:


friends.items()


# In[94]:


friends.values()


# In[108]:


friends={1:'phebe',2:'chandler',3:'Monica',4:'Ross',5:'joey',6:'rachel',7:'gunther'}
friends.update('8':mike)
print(friends)


# In[113]:


a=10
b=20
if a<b:
    print(a)
    if b==20:
        print(b)


# In[117]:


#while loop
a=1
while a<=10:
    print(a)
    a=a+1
    


# In[118]:


#for loop
a=['do','teen','chaar']
i=1
for i in a:
    print(i)
#range example    
    
    


# In[119]:


a=input("enter a number")
print(a)


# In[127]:


k=int(input("enter first number"))
print(k)
j=int(input("enter second number"))
print(j)
prod=k*j
sum=k+j
if(prod<1000):
    print(prod)
elif(prod>=1000):
    print(sum)


# In[ ]:




