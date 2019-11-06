from SimpleCV import *
cam = Kinect()


while True:
    depth = cam.getDepth()
    depth.show()