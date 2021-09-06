#!/usr/bin/env python
# coding: utf-8

# In[23]:


import numpy as np 
import cv2
import pandas as pd
import os


# In[7]:


# creating skeleton of the Yolov3 using weights and its configration
net = cv2.dnn.readNet("G://flicker_dataset//Yoloweights for cloth detection//yolov3-df2_15000.weights", "G://flicker_dataset//Yoloweights for cloth detection//yolov3-df2.cfg")

# classes are the object which can be detected by Yolov3
classes=[]
with open('G://flicker_dataset//Yoloweights for cloth detection//df2.names','r') as f:
    classes=f.read().splitlines()


# In[ ]:


# function returning class_ids detected by model
def fashion_dection(img):
    # Reading image which can be used for detection
    img= cv2.imread('G://flicker_dataset//Data//test//3361.jpg')
    height, width, _ =np.array(img).shape

    # converting image as per yolov3
    blob = cv2.dnn.blobFromImage(img,1/255,(416,416),(0,0,0),swapRB=True,crop=False)

    # Providing input
    net.setInput(blob)

    # Getting output 
    output_layers_names = net.getUnconnectedOutLayersNames()
    LayerOutputs = net.forward(output_layers_names)

    boxes=[]
    confidences=[]
    class_ids=[]
    # In these for loops we are eleminating the objects whose predction value less than 50%.
    # Also extrating the size of the bounding boxes
    for output in LayerOutputs:
        for detection in output:
            scores=detection[5:]
            class_id=np.argmax(scores)
            confidence=scores[class_id]
            if confidence > 0.1 :
                center_x=int(detection[0]*width)
                center_y=int(detection[1]*height)
                w = int(detection[2]*width)
                h = int(detection[3]*height)

                x=int(center_x - w/2)
                y=int(center_y - h/2)
                boxes.append([x,y,w,h])
                confidences.append(confidence)
                class_ids.append(class_id)
    return class_ids


# In[11]:


# Path of image dataset
des_path='G://flicker_dataset//Data//'
folders = ['train','test','validation']
#creating dictionary of class_ids
for fol in folders
    # loading the directory
    a=os.listdir(des_path+fol)
    dect={}
    for i in a:
        # reading the images
        img=cv2.imread(des_path+'//'+i)
        # Getting class_ids
        l=fashion_detection(img)
        # Appending them in dictionary
        for j in l:
            if j not in dect:
                dect[j]=1
            else:
                dect[j]+=1


# In[41]:


# sorting dictionary in decreasing order
dect=sorted(dect.keys(),key=lambda x:x[1],reverse=True)
# defining location for final result
name='G://licker_dataset//Image_1//Output//PartB'
clothes=[]
# Writing classses in clothes list using class_ids
for k in range(10):
    clothes.append(classes[dect[k][0]])
#creating dataframe and saving it as csv 
cloth=pd.DataFrame(clothes,columns=['Top 10 occurance'])
cloth=to_csv(name)
cloth

