import cv2
import pickle
import cvzone
import numpy as np
#In further line we'll check the car is present or not for that solution will check the edges and corners
# if we don't have lots of ages then it's a car else not a car


#video feed
cap=cv2.VideoCapture("carPark.mp4")


with open("carparkposi", 'rb') as f:
    poslist=pickle.load(f)
width, height=107,48

def carParkingSpacecheck(imgPro):
    space_counter=0
    for pos in poslist:
        x,y=pos
        
        imgCrop=imgPro[y:y+height, x:x+width]
        #cv2.imshow(str(x*y), imgCrop)
        #let's count the pixel so we can determine that which have none pixels it's empty park
        count=cv2.countNonZero(imgCrop)
        cvzone.putTextRect(img, str(count), (x, y+height-3), scale=1, thickness=1, offset=0, colorR=(0,0,255))

        if count<900:
            color=(0,255,0)
            #place is available then should be more visible
            thickness=2
            space_counter+=1
        else:
            color=(0,0,255)
            thickness=1
        cv2.rectangle(img, pos, (pos[0]+width, pos[1]+height), color, thickness)
    cvzone.putTextRect(img, f'Free Spaces : {space_counter}/{len(poslist)}', (100,50), scale=2, thickness=1, offset=20, colorR=(0, 180, 0))


while True:
    
    if cap.get(cv2.CAP_PROP_POS_FRAMES)==cap.get(cv2.CAP_PROP_FRAME_COUNT):
        #Reseting the frame if it reaches to the total number of frame that the video have
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)
       

    
    success, img=cap.read()
    #In further line we'll check the car is present or not for that solution will check the edges and corners
    # if we don't have lots of ages then it's a car else not a car
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #sigmax as 1 in below method
    imgblur=cv2.GaussianBlur(imgGray, (3,3), 1)
    #we're using adapting threshold 25, 16 is block size
    imgThreshold=cv2.adaptiveThreshold(imgblur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)

    #median threshold to neglect some salt and paper or rempove some dots 
    imgMedian=cv2.medianBlur(imgThreshold,5)

    #some time these pixels or values may be little bit thin to solve make little thicker to diffrenciate the car and empty place
    #will use dilate, will gave a kernal
    kernal=np.ones((3,3), np.uint8)
    imgDilate=cv2.dilate(imgMedian, kernal, iterations=1)

    carParkingSpacecheck(imgDilate)
    #after processing is done and count is done then we can below two line comment and second one move above
    #for pos in poslist:
        #cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255,0,240), 2)
    cv2.imshow('image', img)
    #cv2.imshow("imageMedian", imgMedian)
    cv2.waitKey(1)

