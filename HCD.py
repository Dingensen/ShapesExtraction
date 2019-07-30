# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 12:32:56 2019

@author: Katarzyna Goch
modified by Felix Niebl
"""
import cv2
import numpy as np
import os
import Bird_Angle_calculator as computeAngles
import imutils #not standard in anaconda 2.7, install manually "conda install -c pjamesjoyce imutils"
from simplification.cutil import simplify_coords #not standard, install manually "pip install simplification"
#import csv

birdData = 'BirdSilhouettes'
birdShapeOutputFile = "birdShapes.txt"

#helping function to write the coordinates as tuples (https://stackoverflow.com/questions/10016352/convert-numpy-array-to-tuple)
def toTuple(a):
    try:
        return tuple(toTuple(i) for i in a)
    except TypeError:
        return a

#perhaps use Houghlines (https://docs.opencv.org/2.4/modules/imgproc/doc/feature_detection.html?highlight=cornerharris#canny86)
#or cv2.findcontours
def getTheCoordinateArray(file):
    img = cv2.imread(os.path.join(os.getcwd(),birdData,file))
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    gray = np.float32(gray)
    
    #create shape-mask from the image
    lower = np.array([0, 0, 0])
    upper = np.array([128, 128, 128])
    shapeMask = cv2.inRange(img, lower, upper)

    '''
    #shows the shape mask for each shape
    cv2.imshow("shapeMask", shapeMask)
    cv2.waitKey(0)
    '''
    
    #look for contours in the mask
    contours = cv2.findContours(shapeMask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    
    #format the list accordingly
    contours = contours[0]
    corners = []
    for vertex in contours:
        corners.append(vertex[0].tolist())
    
    #simpliufy the shape
    corners = simplify_coords(corners, 1.0)
    
    #NOTE: Felix here, removed following lines as they were causing my system to freeze up. seems to work without. I am not entirely sure what they do.
    #if cv2.waitKey(0) & 0xff == 27:
        #cv2.destroyAllWindows()
    #print(cv2.waitKey(0))
    cv2.destroyAllWindows()
    
    #Felix: changed this up so the coordinates get returned as a tuple (x,y) instead of a list [x,y] so it can work with the angle-calculation-script
    theCoordinates = []
    for vertex in corners:
        theCoordinates.append(toTuple(vertex))
    
    return theCoordinates

#### Run files ####

wd = os.getcwd()   
files = os.listdir(os.path.join(wd,birdData))

#Felix: created own file-writing procedure to make the file easier readable to the angle-calculator
birdShapeOutput = open(birdShapeOutputFile, "w+")
for file in files:
    #thrown-together code to make the output strings readable for the angle-calculator
    lines = getTheCoordinateArray(file)
    lines = str(lines)
    lines = lines[1:-1]
    
    #it is not as elegant, but i couldn't get it done properly with csv.writer()
    birdShapeOutput.write("[")
    birdShapeOutput.write(lines)
    birdShapeOutput.write("]\n")
    
birdShapeOutput.close()
    
#run the other script that calculates the angles
computeAngles.processBirdFile(birdShapeOutputFile)

"""
with open('shapes.txt', 'w') as writeFile:
    writer = csv.writer(writeFile, quoting=csv.QUOTE_NONE, escapechar=' ')
    for file in files:
        print(file)
        lines = getTheCoordinateArray(file)
        writer.writerow(lines)
"""