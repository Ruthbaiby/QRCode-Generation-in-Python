#!/usr/bin/env python
# coding: utf-8

# In[69]:


#QR Code generation in Python


# # QR Code Generation

# In[70]:


pip install qrcode


# In[71]:


import qrcode
from PIL import Image


# In[72]:


#the data you want to encode in the QR Code
data= "https://github.com/Ruthbaiby"


# In[99]:


#Generate the QR Code
qr= qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)


# In[100]:


#Create an image from the QR Code
image= qr.make_image(fill="black", back_color="green")


# In[101]:


#save the image
image.save("qr_code.png")


# In[102]:


#open the image
image


# In[ ]:




