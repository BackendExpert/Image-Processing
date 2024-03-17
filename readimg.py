import cv2
import os

img_path = "F:/python/projects/Pysw/imgprocessing/imgaes/gitss.jpg"

img = cv2.imread(img_path)

if(img is not None):
    print('Image Read Successful')
else:
    print('ERROR')