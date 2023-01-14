#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system(' pip install opencv-python')
get_ipython().system(' pip install pytesseract')
get_ipython().system(' pip install imutils')


# In[2]:


import cv2
import pytesseract
import imutils
import numpy as np
from PIL import Image
from pytesseract import image_to_string


# In[3]:


pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'


# In[12]:


image = cv2.imread("7.jpg")


# In[13]:


image=cv2.resize(image,(1000,650))


# In[14]:


cv2.imshow("Original Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[15]:


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# In[16]:


gray = cv2.bilateralFilter(gray, 11, 17, 17)


# In[17]:


r = cv2.selectROI( gray )
width_start, height_start, width_end, height_end = r
cropped_img = gray[height_start: height_start + height_end, width_start: width_start + width_end]
cv2.imwrite( 'CroppedImage.jpg', cropped_img )  # Saving Cropped Image
cv2.imshow('Cropped Image', cropped_img)
cv2.waitKey(0)


# In[18]:


imagem = cv2.bitwise_not(gray)


# In[19]:


gray_new = cv2.bilateralFilter(imagem, 11, 17, 17)
print( "Text Extraction = " , image_to_string( gray_new )) # Try 1 (BEST RESULT IN MOST CASES)

cv2.imshow("Bilateral Filter", gray_new )
cv2.waitKey(0)


# In[ ]:





# In[ ]:





# In[ ]:




