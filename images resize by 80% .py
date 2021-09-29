import cv2
import glob
images=glob.glob('*.jpg')
for image in images: 
    original=cv2.imread(image,1)
    re=cv2.resize(original,(int(original.shape[1]/5),int(original.shape[0]/5)))
    cv2.imwrite('resized '+ image,re)
