import cv2
import sys
sys.path.append('Module-1')
from voice import *
sys.path.append('Module-2')
from OCR import *

sys.path.append('Module-3')
from Image_Captioning import *

sys.path.append('Module-4')
from reco import *

sys.path.append('../')
mode=1
count = 0
def cam():
    global mode
    global count
    # Load Camera
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        nm="frame"+str(count)+".jpg"
        cv2.imwrite(nm, frame)
        count+=1
        if(mode==1):
            voice(caption_this_image(nm))
        elif(mode==2):
            recognise(nm)
        elif(mode==3):
            ocr(nm)
        cv2.imshow("frame",frame)
        key = cv2.waitKey(1)
        if key == 49:
            mode=1
        elif key == 50:
            mode=2
        elif key == 51:
            mode=3
        elif key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    cam()
