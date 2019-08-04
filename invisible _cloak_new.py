import cv2
import numpy as np
import time

def emptyFunction():
    pass
def main():
    windowName = 'video'
    cv2.namedWindow(windowName)
    ilowH = 0
    ihighH = 179

    ilowS = 0
    ihighS = 255
    ilowV = 0
    ihighV = 255
    
    
    cv2.createTrackbar('lowH_mask1',windowName,ilowH, 179,emptyFunction)
    cv2.createTrackbar('highH_mask1',windowName,ihighH, 179,emptyFunction)

    cv2.createTrackbar('lowS_mask1',windowName,ilowS, 255,emptyFunction)
    cv2.createTrackbar('highS_mask1',windowName,ihighS, 255,emptyFunction)

    cv2.createTrackbar('lowV_mask1', windowName, ilowV ,255,emptyFunction)
    cv2.createTrackbar('highV_mask1', windowName ,ihighV, 255,emptyFunction)

    cv2.createTrackbar('lowH_mask2',windowName,ilowH, 179,emptyFunction)
    cv2.createTrackbar('highH_mask2',windowName,ihighH, 179,emptyFunction)

    cv2.createTrackbar('lowS_mask2',windowName,ilowS, 255,emptyFunction)
    cv2.createTrackbar('highS_mask2',windowName,ihighS, 255,emptyFunction)

    cv2.createTrackbar('lowV_mask2', windowName, ilowV, 255,emptyFunction)
    cv2.createTrackbar('highV_mask2', windowName ,ihighV, 255,emptyFunction)

    cap = cv2.VideoCapture(0)
    time.sleep(1)
    count = 0
    background = 0

    for i in range (60):
        return_val, background = cap.read()
        if return_val == False:
            continue
    background = np.flip(background, axis = 1)

    if cap.isOpened():
        ret, frame = cap.read()

    else:
        ret = False
    
    while ret:
        ret, frame = cap.read()
        count = count + 1
        frame = np.flip(frame, axis =1)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lowH_mask1 =  cv2.getTrackbarPos('lowH_mask1',windowName)
        highH_mask1 =  cv2.getTrackbarPos('highH_mask1',windowName)
        lowS_mask1 =  cv2.getTrackbarPos('lowS_mask1',windowName)
        highS_mask1 =  cv2.getTrackbarPos('highV_mask1',windowName)
        lowV_mask1 =  cv2.getTrackbarPos('lowV_mask1',windowName)
        highV_mask1 =  cv2.getTrackbarPos('highV_mask1',windowName)
        lowH_mask2 =  cv2.getTrackbarPos('lowH_mask2',windowName)
        highH_mask2 =  cv2.getTrackbarPos('highH_mask2',windowName)
        lowS_mask2 =  cv2.getTrackbarPos('lowS_mask2',windowName)
        highS_mask2 =  cv2.getTrackbarPos('highV_mask2',windowName)
        lowV_mask2 =  cv2.getTrackbarPos('lowV_mask2',windowName)
        highV_mask2 =  cv2.getTrackbarPos('highV_mask2',windowName)
        
        lower_red_mask1 = np.array([lowH_mask1, lowS_mask1, lowV_mask1])
        upper_red_mask1 = np.array([highH_mask1, highS_mask1, highV_mask1])

        mask1 = cv2.inRange(hsv, lower_red_mask1, upper_red_mask1)
        
        lower_red_mask2 = np.array([lowH_mask2, lowS_mask2, lowV_mask2])
        upper_red_mask2 = np.array([highH_mask2, highS_mask2, highV_mask2])
        mask2 = cv2.inRange(hsv, lower_red_mask2, upper_red_mask2)

        mask1 = mask1 + mask2
        mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3), np.uint8),iterations=2)
        mask1 = cv2.dilate(mask1, np.ones((3,3), np.uint8), iterations = 1)
        mask2 = cv2.bitwise_not(mask1)

        res1 = cv2.bitwise_and(background, background, mask = mask1)
        res2 = cv2.bitwise_and(hsv,hsv, mask = mask2)
        video = cv2.addWeighted(res1, 1, res2, 1,0)
        


        
#        cv2.imshow(windowName, video)
        cv2.imshow("frame", video)

        #cv2.imshow('mask1', mask1)
        #cv2.imshow('mask2', mask2)
        k = cv2.waitKey(10) 
        if k == 27: 
            break

    cv2.destroyAllWindows()
    cap.release()
if __name__ == "__main__":
    main()
