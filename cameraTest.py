import cv2
import time
#print(cv2.__version__)

#image = cv2.imread('image.png') 


vid = cv2.VideoCapture(1) 
cap = cv2.VideoCapture(1)
for i in range(1,101):
    ret,frame1 = cap.read()
while(True): 
    cv2.imshow('img1',frame1) #display the captured image
    if cv2.waitKey(1) & 0xFF == ord("q"): #save on pressing 'y' 
        cv2.imwrite('images/c1.png',frame1)
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



