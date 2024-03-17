import cv2
import os

img_path = "F:/python/projects/Pysw/imgprocessing/imgaes/gitss.jpg"

folder_path = "F:/python/projects/Pysw/imgprocessing/addedImages"


if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    
image = cv2.imread(img_path)

newfolder_path = os.path.join(folder_path, os.path.basename(img_path))
cv2.imwrite(newfolder_path, image)

print("Image Added folder", folder_path)