import cv2
import time
#print(cv2.__version__)

#image = cv2.imread('image.png') 


vid = cv2.VideoCapture(1) 
cap = cv2.VideoCapture(1)
blur = int(input("How Much to Blur: "))
if (blur%2) == 0:
    blur += 1
for i in range(1,101):
    ret,frame1 = cap.read()
    median = cv2.medianBlur(frame1,blur) 
while(True): 
    cv2.imshow('Medium Blurring', median) #display the captured image
    if cv2.waitKey(1) & 0xFF == ord("q"): #save on pressing 'y' 
        cv2.imwrite('images/c1.png',median)
        cv2.destroyAllWindows()
    # Capture the video frame 
    # by frame 
    ret, frame2 = vid.read() 
    # Display the resulting frame 
    cv2.imshow('frame', frame2) 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
vid.release()
cap.release()



