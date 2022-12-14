import cv2
import numpy as np
from HSV_similarity_detection import *

white_RGB_sample=[[215,214,220],
[217,215,228],
[219,217,230],
[217,212,217],
[213,216,223]
]
white_ideal=[[255,255,255]]
black_RGB_sample1=[[29,29,39],[30,29,37],[28,28,38],[48,47,61],[53,52,70],[53,52,66],[60,58,72]]
## if you have more than one range color, define more black_RGB_sample1 and black_RGB_sample2 and so on. the verticaly stack them using below line code
#for example when u use 0.jpg, black_RGB_sample1 array is extracted from it's pixcel but if you want extracting 6.jpg too so u need define black_RGB_sample2 as bellow
# there is a lot of web page for pick color of image's pixcels. for example i use this web page: https://imageresizer.com/color-picker
black_RGB_sample2=[[109,100,96],[109,99,97],[110,108,103],[117,105,97]]
black_ideal=[[0,0,0]]
black_HSV= np.vstack((avr_HSV(black_RGB_sample1),avr_HSV(black_RGB_sample2),avr_HSV(black_ideal)))
white_HSV= np.vstack((avr_HSV(white_RGB_sample),avr_HSV(white_ideal)))
image_name  = "0.jpg"
image_folder= "images/"
image_path = image_folder+image_name
loaded_image = cv2.imread(image_path)
is_background_black:bool=False
is_background_white:bool=False
Sensivity="uniform"
is_background_black,is_background_white,final_img = background_color(loaded_image,background_ratio=50,dist=40,sensivity=Sensivity, black_color=black_HSV, white_color=white_HSV)
#final_img=cv2.cvtColor(final_img, cv2.COLOR_GRAY2BGR)
cv2.imshow("final",final_img)
cv2.waitKey(0)
cv2.imwrite(image_path[0:-4]+"_removedbackground_"+Sensivity+image_path[-4:], final_img)