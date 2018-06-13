#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 18:02:41 2018

@author: vladimir
"""

import cv2
from darkflow.net.build import TFNet
import matplotlib.pyplot as plt

# define the model options and run
options = {
        'model': 'cfg/tiny-yolo-voc.cfg',
        'load': 'bin/tiny-yolo-voc.weights',
        'threshold': 0.15,
#        'gpu': 0.3
        }

tfnet = TFNet(options)

# read the color image and covert to RGB
img = cv2.imread('./sample_img/sample_dog.jpg',cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# use YOLO to predict the image
result = tfnet.return_predict(img)


# pull out some info from the results

tl = (result[0]['topleft']['x'], result[0]['topleft']['y'])
br = (result[0]['bottomright']['x'], result[0]['bottomright']['y'])
label = result[0]['label'] + ': ' + str(int(result[0]['confidence']*100)) + '%'


# add the box and label and display it
img = cv2.rectangle(img, tl, br, (0, 255, 0), 7)
img = cv2.putText(img, label, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
plt.imshow(img)
plt.show()
