#!/usr/bin/env python
# coding: utf-8

# In[6]:


import matplotlib.pyplot as plt

colors = ['#FDEE58', '#4B77BE']

labels = ['Yes Fire', 'No Fire']
sizes = [71.5, 28.5]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
ax1.set_title('Fire Alarm Data')
plt.legend(labels, loc='lower left')
plt.show()


# In[ ]:




