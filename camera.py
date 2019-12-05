import numpy as np
import cv2


class colorcheck():
    def __init__(self):
        #self.r = 0
        #self.g = 0
        #self.b = 0
        #self.shape = (0, 0, 0)
        self.size = 10
        

    def checkcamera(self):
        try:
            cap = cv2.VideoCapture(1)
        except:
            cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        self.shape = frame.shape
        self.cap = cap
        self.center_x = int(self.shape[0]/2)
        self.center_y = int(self.shape[1]/2)
        #print (frame.shape) #(480, 640, 3)

    def targetcolor(self, r, g, b):
        self.target_color = (r, g, b)
        self.r = r
        self.g = g
        self.b = b

    def colorchecking(self):
        while (True):
            ret, frame = self.cap.read()
            #print (frame.shape) #(480, 640, 3)
            #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            cv2.rectangle(frame, (self.center_y-self.size, self.center_x-self.size), \
                (self.center_y+self.size, self.center_x+self.size), (0, 255, 0), thickness=2)
            cv2.imshow('frame',frame)

            current_r = 0
            current_g = 0
            current_b = 0
            for i in range(0, 20):
                for j in range(0, 20):
                    tmp_r = frame[240+i, 240+j, 0]
                    tmp_g = frame[240+i, 240+j, 1]
                    tmp_b = frame[240+i, 240+j, 2]
                    current_r += tmp_r
                    current_g += tmp_g
                    current_b += tmp_b
            current_r = int(current_r / 400)
            current_g = int(current_g / 400)
            current_b = int(current_b / 400)
            if ((abs(current_r - self.r) < 10) and \
                (abs(current_g - self.g) < 10) and \
                (abs(current_b - self.b) < 10)):
                print ("color right")
            else:
                if ((current_r - self.r) >= 10):
                    print ("Red is too much")
                elif ((current_r - self.r) < -10):
                    print ("I need more red")
                else:
                    print ("red is ok")
                if ((current_g - self.g) >= 10):
                    print ("Green is too much")
                elif ((current_g - self.g) < -10):
                    print ("I need more green")
                else:
                    print ("green is ok")
                if ((current_b - self.b) >= 10):
                    print ("Blue is too much")
                elif ((current_b - self.b) < -10):
                    print ("I need more blue")
                else:
                    print ("blue is ok")
                print ("color now: ", (current_r, current_g, current_b))
                print ("target color: ", self.target_color)
                print ("\n")

            if cv2.waitKey(1) & 0xFF == ord('q'):
                
                self.cap.release()
                cv2.destroyAllWindows()
                break

if __name__ == "__main__":
    mixer = colorcheck()
    mixer.checkcamera()
    mixer.targetcolor(20, 30, 40)
    mixer.colorchecking()
