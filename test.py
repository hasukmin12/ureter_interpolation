import numpy as np
import os
import cv2
import copy
from PIL import Image
from interpolate_two_image import inter
from blob_detecter import blob_detecter


img_1 = '/home/has/Datasets/Ureter_dataset2/case_00000/pre_036.png'
img_2 = '/home/has/Datasets/Ureter_dataset2/case_00000/pre_041.png'

blob1, blob2 = blob_detecter(img_1,img_2)

print(blob1)
print(blob2)

print(blob1.min())

out_1 = inter(img_1,img_2,0.8)

cv2.imwrite('0.8shift_ureter.png', out_1)
print("img saved")

cv2.imshow("image", out_1)
cv2.waitKey()